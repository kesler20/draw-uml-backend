import typing as types
from stdx.file import File

sql_code = File("sql_code.sql").readlines()

# build a json file containing the relationships and the metadata of the code
# we want to have each tablename indexing the various properties and then
# append the rest of the information such as primary and foreign keys
# it seems that the slq code generated has the name of the attribute followed by its type
# to simplify the analysis we can say that all the ids are primary keys
diagram_representation: types.Dict[str, types.List[types.List[str]]] = {}
class_index = -1
for line in sql_code:
    if "CREATE TABLE " in line:
        tablename = line.split("CREATE TABLE `")[1].split("`(")[0]
        diagram_representation[tablename] = []
        class_index += 1
    if "NOT NULL" in line:

        colum_name_and_type = list(filter(
            lambda word: word != "", line.split(" NOT NULL")[0].replace(
                "UNSIGNED", "").replace("`", "").split(" ")))
        if len(colum_name_and_type) > 2:
            colum_name_and_type = colum_name_and_type[:-1]

        class_name = list(diagram_representation.keys())[class_index]

        diagram_representation[class_name].append(colum_name_and_type)

    if "FOREIGN KEY" in line:
        foreign_key = line.split("FOREIGN KEY(`")[1].split("`)")[0]
        reference = line.split("REFERENCES `")[1].split("`(`id`)")[0]

        table_name = line.split(
            "` ADD CONSTRAINT ")[0].split(" `")[1]

        for index, attribute in enumerate(diagram_representation[table_name]):
            # attributes are an array of 2 strings, the name of the column and its type
            if attribute[0] == foreign_key:
                diagram_representation[table_name][index].append(reference)

File("sql_code_representation.json").write_json(diagram_representation)