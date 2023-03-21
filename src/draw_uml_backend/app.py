import shutil
import os
from typing import Any
from pathlib import Path
from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from draw_uml_backend.file import File
from draw_uml_backend._base import BASE_OUTPUT_RESPONSE_PATH
from draw_uml_backend.routines import *

# ---------------------------------------------------#
#                                                    #
#     INITIALIZE APPLICATION AND CONFIGURATIONS      #
#                                                    #
# ---------------------------------------------------#

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["root"])
async def read_root():
    response = RedirectResponse(url="/docs")
    return response


# ----------------------------------- #
#                                     #
#         APPLICATIONS ENDPOINTS      #
#                                     #
# ------------------------------------#


@app.get("/v1/files/{filename}")
async def get_file(filename: str):
    print("get design document file called")
    file_path = os.path.join(BASE_OUTPUT_RESPONSE_PATH, filename)
    return FileResponse(file_path, media_type="text/x-markdown", filename=filename)


@app.get("/v1/files")
async def get_file_list():
    output_file = os.listdir(BASE_OUTPUT_RESPONSE_PATH)
    print("these are the following files", output_file)
    return {"response": output_file}


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
    print(diagram[0][0]["dataclass"])
    dataclasses = list(
        filter(
            lambda index: index is not None,
            [
                index if object["dataclass"] == True else None
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
