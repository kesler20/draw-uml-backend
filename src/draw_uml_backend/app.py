from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from src.draw_uml_backend.fast_prototyping.main import ClassBuilder
from src.draw_uml_backend.fast_prototyping.mainjs import JsClassBuilder
from src.draw_uml_backend.fast_prototyping.test_main import TestClassBuilder
from draw_uml_backend.protocol_database.database_client import DatabaseClient
from draw_uml_backend.protocol_database.database_interface import DatabaseInterface

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


@app.get('/python_file')
async def handle_get_python_file():
    print("get python file called")
    return FileResponse("file.py", media_type="text/x-python", filename="file.py")


@app.get('/python_test_file')
async def handle_get_python_test_file():
    print("get python test file called")
    return FileResponse("test_file.py", media_type="text/x-python", filename="test_file.py")


@app.get('/javascript_file')
async def handle_get_javascript_file():
    print("get javascript file called")
    return FileResponse("file.js", media_type="text/javascript", filename="file.js")


@app.get('/python')
async def handle_create():
    return FileResponse()


@app.post('/CREATE')
async def handle_create_new_diagram():
    print("create diagram")
    return {"response": "okay"}
