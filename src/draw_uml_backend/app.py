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

@app.get('/get/existing/python/code')
async def get_python_code():
    print("get python file called")
    return FileResponse(code_output_file, media_type="text/x-python", filename=code_output_file)


@app.get('/get/existing/python/test/io')
async def get_python_test_io():
    print("get python test io file called")
    return FileResponse(test_file_path_io, media_type="text/x-python", filename=test_file_path_io)


@app.get('/get/existing/python/test/side_effects')
async def get_python_test_side_effects():
    print("get python test side effects file called")
    return FileResponse(test_file_path_side_effects, media_type="text/x-python", filename=test_file_path_side_effects)


@app.get('/get/existing/markdown/diagram')
async def get_markdown_diagram():
    print("get design document file called")
    return FileResponse(documentation_path, media_type="text/x-markdown", filename=documentation_path)


@app.get('/get/existing/python/types')
async def get_python_types():
    print("get types file called")
    return FileResponse(types_file, media_type="text/x-python", filename=types_file)


@app.post('/create/new/python/files/dataclass')
async def create_new_diagram(diagram=Body(...)):
    # write the diagram to the new code response  code path
    File(Path(new_code_response)).write(json.dumps(diagram))
    routine(new=True, diagram=True, types=True, code=True, test=True, dataclass=True)
    return {"response": "okay"}


@app.post('/create/existing/python/files/dataclass')
async def create_existing_diagram(src=Body(...)):
    # write the diagram to the new code response  code path
    File(Path(source_code_path)).write(json.dumps(src))
    routine(existing=True, diagram=True, types=True, code=True, test=True, dataclass=True)
    return {"response": "okay"}
