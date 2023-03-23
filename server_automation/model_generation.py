from typing import List, Dict

SQL_TYPES = [
    "INT", "VARCHAR(255)"
]
ORM_TYPES = {
    "INT": "Integer",
    "VARCHAR(255)": "String(255)"
}

PYTHON_TYPES = {
    "Integer": "int",
    "String(255)": "str"
}

with open("drawSQL.sql") as db_spec:
    content = [clean_line.replace("\n", "")
               for clean_line in db_spec.readlines()]

db_model = """
from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from typing import Type


Base = declarative_base()
"""


# ========================= #
# BUILD THE INITIAL CLASSES #
# ========================= #


foreign_keys: List[str] = []

for line in content:

    if line.find("CREATE TABLE") != -1:
        table_name = line.replace("CREATE TABLE", "").replace(
            "`", "").replace("(", "").replace(" ", "")
        db_model += f'''

class {table_name}(Base):
    __tablename__ = "{table_name.lower()}s"'''

    elif line.find("`id`") != -1 and line.find("(`id`)") == -1:
        db_model += """
    id = Column(Integer, primary_key=True, index=True)"""

    elif line.find("ADD CONSTRAINT") != -1:
        foreign_keys.append(line)

    else:
        for type_ in SQL_TYPES:
            if line.find(type_) != -1:
                row_name = line.split(type_)[0].replace(
                    "`", "").replace(" ", "")
                db_model += f"""
    {row_name} = Column({ORM_TYPES[type_]}, nullable=False)"""

with open("models.py", "w") as out_file:
    out_file.write(db_model)

# ======================== #
# BUILD THE RELATIONSHIPS  #
# ======================== #

with open("models.py") as out_file:
    content: List[str] = [line.replace("\n", "")
                          for line in out_file.readlines()]

# INSERT DELIMETERS FOR THE FOREIGN KEY
db_model_lines = []
class_flag = ""
for index, line in enumerate(content):
    if line.find("class ") != -1:
        class_flag = line.split("class ")[1].split(
            "(Base)")[0].replace(" ", "")
    try:
        if content[index + 1].find("class ") != -1 and class_flag != "":
            db_model_lines.append(f"----{class_flag}\n")
    except IndexError:
        pass

    db_model_lines.append(line)

db_model_lines.append(f"----{class_flag}")

db_model = ""
for line in db_model_lines:
    db_model += line + "\n"

# foreign keys will look something like this
# ['    `Laboratory` ADD CONSTRAINT `laboratory_equipments_foreign` FOREIGN KEY(`equipments`) REFERENCES `Equipment`(`tag`);',
#  '    `Equipment` ADD CONSTRAINT `equipment_sensors_foreign` FOREIGN KEY(`sensors`) REFERENCES `Sensor`(`name`);']
# as such Laboratory is a parent of Equipment
# as such Equipment is a parent of Sensor
for foreign_key in foreign_keys:
    parent_table = foreign_key.split("ADD CONSTRAINT")[
        0].replace(" ", "").replace("`", "")
    child_table = foreign_key.split("REFERENCES")[1].split(
        "(")[0].replace(" ", "").replace("`", "")
    parent_relationships = f"""
    {child_table.lower()}s = relationship("{child_table}", back_populates="{parent_table.lower()}")
    """
    child_relationship = f"""
    {parent_table.lower()}_id = Column(Integer, ForeignKey("{parent_table.lower()}s.id"))
    {parent_table.lower()} = relationship("{parent_table}", back_populates="{child_table.lower()}s")
    """
    db_model = db_model.replace(
        f"----{child_table}", child_relationship).replace(f"----{parent_table}", parent_relationships)

with open("models.py", "w") as out_file:
    out_file.write(db_model)

# =============================== #
# ADD CONSTRUCTORS TO ORM CLASSES #
# =============================== #

with open("models.py") as out_file:
    content = out_file.readlines()

class_properties: Dict[str, List] = {}
class_flag = ""
for line in content:
    if line.find("class ") != -1:
        class_flag = line.split("class ")[1].split("(Base)")[0]
        class_properties[class_flag] = []

    if line.find("Column(") != -1 and line.find("id") == -1:
        property_ = line.split(" = Column(")[0].replace(" ", "")
        property_type = line.split("Column(")[1].split(",")[0]
        class_properties[class_flag].append(
            (property_, PYTHON_TYPES[property_type]))

new_content = []
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
                self_params += f"""
        self.{property_[0]} = {property_[0]}"""

            constructor = f"""

    def __init__(self, {params}) -> None:
{self_params}"""
            new_content.insert(index - 2, constructor + "\n")
            class_flag = line.split("class ")[1].split("(Base)")[0]

    new_content.append(line)


last_line = f"""

# BUILD THE TABLES OF THE DATABASE
Base.metadata.create_all(bind=create_engine(f"sqlite:///{__name__}.sqlite3", echo=True))
"""

with open("models.py", "w") as out_file:
    out_file.writelines(new_content)
    out_file.writelines([last_line])
