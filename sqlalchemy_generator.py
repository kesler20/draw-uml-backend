from stdx.file import File

diagram_representation = File("sql_code_representation.json").get_json()


def convert_attribute_type_from_sql_to_python(attribute_type):
    PYTHON_TYPES = {
        "INT": "Integer",
        "VARCHAR(255)": "String(255)",
        "DATETIME": "DateTime",
        "BIGINT": "BigInteger",
        "BOOLEAN": "Boolean",
        "DATE": "Date",
        "FLOAT": "Float",
    }
    try:
        return PYTHON_TYPES[attribute_type]
    except KeyError:
        return "Integer"


def generate_class_definition(table_name: str):
    return f"""

class {table_name[0].upper()+table_name[1:-1]}(Base):
  __tablename__ = "{table_name}" """


def generate_class_body(attribute: str, attribute_type: str):
    return f"""
  {attribute} = Column({convert_attribute_type_from_sql_to_python(attribute_type)}, nullable=False)"""


def generate_foreign_key_relationship(relationship_metadata: str):
    """This will generate the foreign key relationship line of code

    Params
    ------
    relationship_metadata : str
      this is an array of string of the following form:
      `[foreign_key, foreign_key_type, reference_table_name]` for example `['laboratory_id', 'INT', 'laboratories']`
    """
    return f"""
  {relationship_metadata[0]} = Column({convert_attribute_type_from_sql_to_python(relationship_metadata[1])}, ForeignKey("{relationship_metadata[2]}.id"))"""


def generate_backref(reference_table: str, referee_table: str):
    """This will generate the sqlalchmey relationship definition line
    for instance

    Example
    -------
    ```python
    # when arguments are `owners` and `pets`
    pets = relationship("Pet",backref="owner")
    ```
    """
    return f"""
  {referee_table} = relationship("{referee_table[0].upper()+referee_table[1:-1]}", backref="{reference_table[:-1]}")"""


def generate_constructor(properties: str):
    properties = list(filter(lambda word: word !=
                      "id" and "_id" not in word, properties))
    arguments = ""
    constructor_body = ""
    for property_ in properties:
        arguments += f", {property_}"

        constructor_body += f"""self.{property_} = {property_}
    """

    return f"""
    
  def __init__(self{arguments}) -> None:
    {constructor_body if constructor_body != "" else "   pass"}
    """


output_class = """
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
"""

referenced_tables = {}
for table_name in diagram_representation.keys():
    for attribute in diagram_representation[table_name]:
        if len(attribute) > 2:
            if attribute[2] in referenced_tables.keys():
                referenced_tables[attribute[2]] = [
                    referenced_tables[attribute[2]], table_name]
            else:
                referenced_tables[attribute[2]] = table_name

for table_name in diagram_representation.keys():
    output_class += generate_class_definition(table_name)
    for attribute in diagram_representation[table_name]:
        if len(attribute) > 2:
            output_class += generate_foreign_key_relationship(attribute)
        else:
            output_class += generate_class_body(attribute[0], attribute[1])
    if table_name in referenced_tables.keys():
        if type(referenced_tables[table_name]) == list:
            for i in range(len(referenced_tables[table_name])):
                output_class += generate_backref(table_name,
                                                 referenced_tables[table_name][i])
        else:
            output_class += generate_backref(table_name,
                                             referenced_tables[table_name])

    properties = [property_[0]
                  for property_ in diagram_representation[table_name]]
    output_class += generate_constructor(properties)

File("output_code.py").write(output_class)
