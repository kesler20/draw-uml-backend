import shutil
import json
from pathlib import Path
from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
try:
    from draw_uml_backend.file import File
    from draw_uml_backend.routines import *
except ModuleNotFoundError:
    from src.draw_uml_backend.file import File
    from src.draw_uml_backend.routines import *

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
    allow_headers=["*"]
)

           
@app.get("/", tags=["root"])
async def read_root():
    response = RedirectResponse(url='/docs')
    return response


# ----------------------------------- #
#                                     #
#         APPLICATIONS ENDPOINTS      #
#                                     #
# ------------------------------------#


@app.get('/get/existing/{filename}')
async def get_file(filename: str):
    print("get design document file called")
    file_path = os.path.join(BASE_OUTPUT_RESPONSE_PATH,filename) 
    return FileResponse(file_path, media_type="text/x-markdown", filename=filename)

@app.get('/get/files')
async def get_file_list():
    output_file = os.listdir(BASE_OUTPUT_RESPONSE_PATH)
    print("these are the following files",output_file)
    return {"response" : output_file}

@app.post('/create/new/files/{dataclasses}')
async def create_new_diagram(dataclasses: bool, diagram=Body(...)):
    # refresh the output folder
    shutil.rmtree(BASE_OUTPUT_RESPONSE_PATH)
    os.mkdir(BASE_OUTPUT_RESPONSE_PATH)
    # write the diagram to the new code response  code path
    File(Path(new_code_response)).write_json(diagram)
    # get the number of objects created
    for object_id in range(len(diagram[0])):
        routine(object_id, new=True, diagram=True, types=True, code=True, test=True, dataclass=dataclasses)
    return {"response": "okay"}

@app.post('/create/existing/files/{dataclasses}')
async def create_existing_diagram(dataclasses: bool, src=Body(...)):
    # refresh the output folder
    shutil.rmtree(BASE_OUTPUT_RESPONSE_PATH)
    os.mkdir(BASE_OUTPUT_RESPONSE_PATH)
    # write the diagram to the new code response  code path
    File(Path(source_code_path)).write(src)
    # get the number of objects created
    routine(0, existing=True, diagram=True, types=True, code=True, test=True, dataclass=dataclasses)
    return {"response": "okay"}
