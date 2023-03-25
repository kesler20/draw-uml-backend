import os
from pathlib import Path
from typing import List, Dict, Any

SQL_TYPES = ["BIGINT", "VARCHAR(100)", "VARCHAR(255)", "BOOLEAN"]
ORM_TYPES = {
    "BIGINT": "Integer",
    "VARCHAR(255)": "String(255)",
    "VARCHAR(100)": "String(255)",
    "BOOLEAN": "Boolean",
}

PYTHON_TYPES = {"Integer": "int", "String(255)": "str", "Boolean": "bool"}


def main():
    with open("drawSQL.sql") as db_spec:
        content = [clean_line.replace("\n", "") for clean_line in db_spec.readlines()]

    db_model = """from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from typing import TypedDict, List, Optional


Base = declarative_base()
    """

    # ========================= #
    # BUILD THE INITIAL CLASSES #
    # ========================= #

    foreign_keys: List[str] = []
    class_flag = ""
    for line in content:

        if line.find("CREATE TABLE") != -1:
            table_name = (
                line.replace("CREATE TABLE", "").replace("`", "").replace("(", "").replace(" ", "")
            )
            db_model += f'''

class {table_name}(Base):
    __tablename__ = "{table_name.lower()}s"'''
            class_flag = table_name

        elif line.find("`id`") != -1 and line.find("(`id`)") == -1:
            db_model += """
    id = Column(Integer, primary_key=True, index=True)"""

        elif line.find("ADD CONSTRAINT") != -1:
            # write them to a comment at the top of the file?
            foreign_keys.append(line)

        else:
            for type_ in SQL_TYPES:
                if line.find(type_) != -1:
                    row_name = line.split(type_)[0].replace("`", "").replace(" ", "")
                    if row_name.find("_id") != -1:
                        db_model += f"""
    {row_name} = Column({ORM_TYPES[type_]}, ForeignKey("{row_name.replace("_id","")}s.id"))"""

                    elif row_name[-1] == "_":
                        db_model += f"""
    {row_name[:-1]} = relationship("{row_name.replace(row_name[0], row_name[0].swapcase())[:-1]}", back_populates="")"""
                    else:
                        db_model += f"""
    {row_name} = Column({ORM_TYPES[type_]}, nullable=False)"""

    with open("models.py", "w") as out_file:
        out_file.write(db_model)

    # =============================== #
    # ADD CONSTRUCTORS TO ORM CLASSES #
    # =============================== #

    with open("models.py") as out_file:
        content = out_file.readlines()

    class_properties: Dict[str, List[Any]] = {}
    class_flag = ""
    for line in content:
        if line.find("class ") != -1:
            class_flag = line.split("class ")[1].split("(Base)")[0]
            class_properties[class_flag] = []

        if line.find("id") == -1:
            if line.find("Column(") != -1:
                property_ = line.split(" = Column(")[0].replace(" ", "")
                property_type = line.split("Column(")[1].split(",")[0]
                class_properties[class_flag].append((property_, PYTHON_TYPES[property_type]))
            else:
                if line.find("relationship(") != -1:
                    property_ = line.split("= relationship(")[0].replace(" ", "")
                    property_type = line.split("relationship(")[1].split(",")[0].replace('"', "")
                    class_properties[class_flag].append(
                        (property_, property_.replace(property_[0], property_[0].swapcase()))
                    )
                else:
                    pass
    content.append("\n")
    content.append("\n")
    content.append("\n")
    content.append("\n")
    content.append("\n")
    content.append("\nclass \n")

    new_content: List[str] = []
    class_flag = ""
    for index, line in enumerate(content):
        if line.find("class ") != -1:
            if class_flag == "":
                class_flag = line.split("class ")[1].split("(Base)")[0]
            else:
                params = ""
                self_params = ""
                for property_ in class_properties[class_flag]:
                    if property_ == class_properties[class_flag][-1]:
                        params += f"{property_[0]} : {property_[1]}"
                    else:
                        params += f"{property_[0]} : {property_[1]}, "
                    self_params += f"""self.{property_[0]} = {property_[0]}
        """

                constructor = f"""
    def __init__(self, {params}) -> None:
        {self_params}"""

                new_content.insert(index - 1, constructor + "\n")
                class_flag = line.split("class ")[1].split("(Base)")[0]

        new_content.append(line)

    last_line = f"""

# BUILD THE TABLES OF THE DATABASE
Base.metadata.create_all(bind=create_engine(f"sqlite:///{__name__}.sqlite3", echo=True))
    """

    with open("models.py", "w") as out_file:
        out_file.writelines(new_content)
        out_file.writelines([last_line])

    cleaned_outfile = []

    with open("models.py", "r+") as out_file:
        for line in out_file.readlines():
            if line != "class \n":
                cleaned_outfile.append(line)

    if Path("models.py").exists():
        os.remove("models.py")

    with open("models.py", "a") as out_file:
        for line in cleaned_outfile:
            out_file.write(line)
