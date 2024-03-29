from pathlib import Path
import os


def write_to_output1(content: str):
    with open("app.py", "a") as out_file:
        out_file.write(content)


def write_to_output2(content: str):
    with open("schema.py", "a") as out_file:
        out_file.write(content)


def create_server_setup():
    write_to_output1(
        """
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

sql_database_interface = SQLDatabaseInterface()

# ============ DEFINE SWAGGER ENDPOINT ==============
@app.get("/", tags=["root"])
async def read_root():
    response = RedirectResponse(url="/docs")
    return response  
"""
    )


def create_db_schema_setup():
    write_to_output2(
        """
from typing import Union, Optional, List
from pydantic import BaseModel
"""
    )


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

    res = "{"
    source = "}"
    if method == "create":
        write_to_output1(
            f"""

# {method} a `{resource}`
@app.{convert_to_http_method(method)}("/v1/{resource}s/", response_model= schema.{resource_name_with_capital}])
async def {method}_{resource}({resource}: schema.{resource_name_with_capital}, owner: schema.UserFind):
    return sql_db_interface.add_value(
        database.{resource_name_with_capital}(**{resource}.__dict__,owner=sql_interface.read_value(database.User, email=owner.email))
    )
"""
        )
    elif method == "read":
        write_to_output1(
            f"""
        
# {method} a `{resource}`
@app.{convert_to_http_method(method)}("/v1/{resource}s/{res}{resource}_id{source}", response_model=schema.{resource_name_with_capital})
async def {method}_{resource}({resource}_id : int):
    return sql_db_interface.read_value(database.{resource_name_with_capital}, id={resource}_id)
"""
        )
        write_to_output1(
            f"""
        
# {method} a `{resource}`
@app.{convert_to_http_method(method)}("/v1/{resource}s/", response_model=List[schema.{resource_name_with_capital}])
async def {method}_{resource}s(current_page_number: int = 1):
    return sql_db_interface.read_all_values_with_pagination(
        database.{resource_name_with_capital}, number_of_objects_per_page=5, current_page_number=current_page_number
    )
"""
        )

    elif method == "update":
        write_to_output1(
            f"""
        
# {method} a `{resource}`
@app.{convert_to_http_method(method)}("/v1/{resource}s/{res}{resource}_id{source}", response_model=List[schema.{resource_name_with_capital}])
async def {method}_{resource}({resource}_id : int, key: str, value : Any):
    return sql_db_interface.update_value(database.{resource_name_with_capital}, key, value id={resource}_id)
"""
        )
    elif method == "delete":
        write_to_output1(
            f"""
        
# {method} a `{resource}`
@app.{convert_to_http_method(method)}("/v1/{resource}s/{res}{resource}_id{source}", response_model=List[schema.{resource_name_with_capital}])
async def {method}_{resource}({resource}_id : int):
    sql_db_interface.delete_value(database.{resource_name_with_capital}, id={resource}_id)
    return sql_db_interface.read_all_values(database.{resource_name_with_capital})
"""
        )
    else:
        raise ValueError("unrecognised method")


def context_delimeter(context: str):
    write_to_output1(
        f"""
# =======================================#
#      {context.lower().swapcase()}      #
# =======================================#
"""
    )


def context_delimeter2(context: str):
    write_to_output2(
        f"""
# =======================================#
#      {context.lower().swapcase()}      #
# =======================================#
"""
    )


def create_db_schema(model: str):
    model_with_capital_letter = model[0].swapcase()
    for char in model[1:]:
        model_with_capital_letter += char

    write_to_output2(
        f"""

class {model_with_capital_letter}Base(BaseModel):
    title: str

class {model_with_capital_letter}Create({model_with_capital_letter}Base):
    title: str
    description: str

class {model_with_capital_letter}Find({model_with_capital_letter}Base):
    title: str

class {model_with_capital_letter}({model_with_capital_letter}Base):
    title : str
    description: str
    owner : User

    class Config:
        orm_mode = True

"""
    )


def main():

    resources = []
    methods = ["create", "read", "update", "delete"]
    with open("models.py") as models:
        content = models.readlines()

    for line in content:
        if line.find("class ") != -1:
            resources.append(line.split("class ")[1].split("(Base)")[0].replace(" ", "").lower())

    database_schema = resources
    server_methods = []
    for resource in resources:
        for method in methods:
            server_methods.append((method, resource))

    print(server_methods)

    if Path("app.py").exists():
        os.remove("app.py")

    if Path("schema.py").exists():
        os.remove("schema.py")

    create_server_setup()
    resource_flag = ""
    for method, resource in server_methods:
        if resource != resource_flag:
            context_delimeter(resource)
            resource_flag = resource
        create_server_methods(method, resource)

    create_db_schema_setup()
    for model in database_schema:
        context_delimeter2(model)
        create_db_schema(model)
