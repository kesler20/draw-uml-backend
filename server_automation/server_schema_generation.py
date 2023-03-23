import os


def write_to_output1(content: str):
    with open("app.py", "a") as out_file:
        out_file.write(content)


def write_to_output2(content: str):
    with open("schema.py", "a") as out_file:
        out_file.write(content)


def create_server_setup():
    write_to_output1("""
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import schema
import uvicorn
from fastapi.responses import RedirectResponse
from . import __version__


# ============ INSTANTIATE APP OBJECT ===============
app = FastAPI(
    title="python_app_template",
    description="A python template application",
    version=__version__,
)


# Allow Cross-Origin Resource Sharing (CORS) to allow requests from a different domain
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============ DEFINE SWAGGER ENDPOINT ==============
@app.get("/", tags=["root"])
async def read_root():
    response = RedirectResponse(url="/docs")
    return response  
""")


def create_db_schema_setup():
    write_to_output2("""
from typing import Union, Optional, List
from pydantic import BaseModel
""")


def convert_to_http_method(method: str):
    """This converts method from create -> post

    Parameters
    ----------

    method : str
      this can be one of `create`, `read`, `update`

    Returns
    -------
    str
      returns one of `post`, `get` or `method` if its 
      not found in the `value` map

    """
    value = {"create": "post", "read": "get", "update": "put"}
    return value[method.lower()] if method in list(value.keys()) else method


def create_server_methods(method: str, resource: str):
    resource_name_with_capital = resource[0].swapcase()
    for char in resource[1:]:
        resource_name_with_capital += char

    if method == "create":
        write_to_output1(f"""

# {method} a {resource}
@app.{convert_to_http_method(method)}("/v1/{resource}s/", response_model=List[schema.{resource_name_with_capital}])
async def {method}_{resource}({resource}: schema.{resource_name_with_capital}):
  {resource}s = []
  # do something
  return {resource}s
""")
    elif method == "read":
        write_to_output1(f"""
        
# {method} a {resource}
@app.{convert_to_http_method(method)}("/v1/{resource}s/{resource}_id", response_model=schema.{resource_name_with_capital})
async def {method}_{resource}({resource}_id : int):
  {resource} = []
  # do something
  return {resource}
""")
    elif method == "update":
        write_to_output1(f"""
        
# {method} a {resource}
@app.{convert_to_http_method(method)}("/v1/{resource}s/{resource}_id", response_model=List[schema.{resource_name_with_capital}])
async def {method}_{resource}({resource}_id : int):
  {resource}s = []
  # do something
  return {resource}s
""")
    elif method == "delete":
        write_to_output1(f"""
        
# {method} a {resource}
@app.{convert_to_http_method(method)}("/v1/{resource}s/{resource}_id", response_model=List[schema.{resource_name_with_capital}])
async def {method}_{resource}({resource}_id : int):
  {resource}s = []
  # do something
  return {resource}s
""")
    else:
        raise ValueError("unrecognised method")


def context_delimeter(context: str):
    write_to_output1(f"""
# =======================================#
#      {context.lower().swapcase()}      #
# =======================================#
""")


def context_delimeter2(context: str):
    write_to_output2(f"""
# =======================================#
#      {context.lower().swapcase()}      #
# =======================================#
""")


def create_db_schema(model: str):
    model_with_capital_letter = model[0].swapcase()
    for char in model[1:]:
        model_with_capital_letter += char

    write_to_output2(f"""

class {model_with_capital_letter}Base(BaseModel):
    title: str
    description: Optional[str]


class {model_with_capital_letter}Create({model_with_capital_letter}Base):
    pass


class {model_with_capital_letter}({model_with_capital_letter}Base):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

""")


database_schema = ["user", "items", "profile"]
server_methods = [("create", "user"), ("create", "items"),
                  ("create", "profile")]
os.remove("app.py")
os.remove("schema.py")

create_server_setup()
for method, resource in server_methods:
    context_delimeter(resource)
    create_server_methods(method, resource)

create_db_schema_setup()
for model in database_schema:
    context_delimeter2(model)
    create_db_schema(model)
