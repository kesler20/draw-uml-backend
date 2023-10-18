from draw_uml_backend.v1.server_automation import model_generation  # type: ignore
from draw_uml_backend.v1.server_automation import server_schema_generation  # type: ignore
import shutil
import os
from pathlib import Path
from fastapi import Body, UploadFile
from fastapi import File as FileType
from fastapi.responses import FileResponse
from draw_uml_backend.file import File
from draw_uml_backend._base import BASE_OUTPUT_RESPONSE_PATH
from draw_uml_backend.routines import *
from draw_uml_backend.app import app

# ----------------------------------- #
#                                     #
#         APPLICATIONS ENDPOINTS      #
#                                     #
# ------------------------------------#


@app.get("/v1/files/{filename}")
async def get_file(filename: str):
    file_path = os.path.join(BASE_OUTPUT_RESPONSE_PATH, filename)
    return FileResponse(file_path, filename=filename)


@app.get("/v1/files")
async def get_file_list():
    output_file = os.listdir(BASE_OUTPUT_RESPONSE_PATH)
    print("these are the following files", output_file)
    return {"response": output_file}


@app.get("/v1/servers")
async def get_servers():

    server_files = os.listdir("server_output")
    for file in os.listdir("tests_for_server_output"):
        server_files.append(file)

    print("these are the following files", server_files)
    return {"response": server_files}


@app.get("/v1/servers/{filename}")
async def get_server_file(filename: str):

    print("get design document file called")

    if Path(os.path.join("tests_for_server_output", filename)).exists():
        file_path = os.path.join("tests_for_server_output", filename)
    else:
        file_path = os.path.join("server_output", filename)

    return FileResponse(file_path, media_type="text/x-markdown", filename=filename)


@app.post("/v1/servers")
async def create_servers(draw_sql_code: UploadFile = FileType(...)):

    print(draw_sql_code.filename)

    with draw_sql_code.file as f:
        file_content = f.read()

    with open("drawSQL.sql", "w") as sql_file:
        sql_file.write(file_content.decode())

    model_generation.main()
    server_schema_generation.main()

    if Path("server_output").exists():
        shutil.rmtree("server_output")

    os.mkdir("server_output")
    os.rename("app.py", os.path.join("server_output", "app.py"))
    os.rename("models.py", os.path.join("server_output", "models.py"))
    os.rename("schema.py", os.path.join("server_output", "schema.py"))

    return {"response": "okay"}


@app.post("/v1/files/existing")
async def create_existing_diagram(dataclasses: bool = False, src=Body(...)):

    # refresh the output folder
    shutil.rmtree(BASE_OUTPUT_RESPONSE_PATH)
    os.mkdir(BASE_OUTPUT_RESPONSE_PATH)

    # write the diagram to the new code response  code path
    File(Path(source_code_path)).write(src)

    # get the number of objects created
    routine(0, existing=True, diagram=True, types=True, code=True, test=True, dataclass=dataclasses)

    return {"response": "okay"}


@app.post("/v1/files/new")
async def create_new_diagram(diagram=Body(...)):

    # refresh the output folder
    shutil.rmtree(BASE_OUTPUT_RESPONSE_PATH)
    os.mkdir(BASE_OUTPUT_RESPONSE_PATH)

    # write the diagram to the new code response  code path
    File(Path(new_code_response)).write_json(diagram)

    # get all the dataclasses : true within the response body
    dataclasses = list(
        filter(
            lambda index: index is not None,
            [
                index if object["data"]["dataclass"] == True else None
                for index, object in enumerate(diagram[0])
            ],
        )
    )

    # get the number of objects created
    for object_id in range(len(diagram[0])):

        # if the error was caught earlier then the `class_id` variable is still a string
        # and it will never be == an int
        routine(
            object_id,
            new=True,
            diagram=True,
            types=True,
            code=True,
            test=True,
            dataclass=True if object_id in dataclasses else False,
        )

    return {"response": "okay"}
