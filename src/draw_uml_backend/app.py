from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from draw_uml_backend.file import File
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

@app.get('/get/python/code')
async def handle_get_python_file():
    print("get python file called")
    return FileResponse(code_output_file, media_type="text/x-python", filename=code_output_file)

@app.get('/get/python/test/io')
async def handle_get_python_test_file():
    print("get python test file called")
    return FileResponse(test_file_path_io, media_type="text/x-python", filename=test_file_path_io)

@app.get('/get/python/test/side_effects')
async def handle_get_python_test_file():
    print("get python test file called")
    return FileResponse(test_file_path_side_effects, media_type="text/x-python", filename=test_file_path_side_effects)

@app.get('/get/markdown/diagram')
async def handle_get_javascript_file():
    print("get design document file called")
    return FileResponse(documentation_path, media_type="text/x-markdown", filename=documentation_path)

@app.get('/get/python/types')
async def handle_get_javascript_file():
    print("get types file called")
    return FileResponse(types_file, media_type="text/x-python", filename=types_file)

@app.post('/create/new/python/files/dataclass')
async def handle_diagram_data(diagram=Body(...)):
    # write the diagram to the new code response  code path
    File(new_code_response).write(diagram)
    routine(new=True, diagram=True, types=True, code=True, test=True, dataclass=True)
    return {"response": "okay"}

@app.post('/create/existing/python/files/dataclass')
async def handle_diagram_data(src=Body(...)):
    # write the diagram to the new code response  code path
    File(source_code_path).write(src)
    routine(existing=True, diagram=True, types=True, code=True, test=True, dataclass=True)
    return {"response": "okay"}
