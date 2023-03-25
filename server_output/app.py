
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

# =======================================#
#      ITEM      #
# =======================================#


# create a item
@app.post("/v1/items/", response_model=List[schema.Item])
async def create_item(item: schema.Item):
    item = sql_db_interface.add_value(
        database.Item()
    )
    return item

        
# read a item
@app.get("/v1/items/{item_id}", response_model=schema.Item)
async def read_item(item_id : int):
    return sql_db_interface.read_value(database.Item, id=item_id)

        
# read a item
@app.get("/v1/items/", response_model=List[schema.Item])
async def read_items(current_page_number: int = 1):
    return sql_db_interface.read_all_values_with_pagination(
        database.Item, number_of_objects_per_page=5, current_page_number=current_page_number
    )

        
# update a item
@app.put("/v1/items/{item_id}", response_model=List[schema.Item])
async def update_item(item_id : int):
    return sql_db_interface.update_value(database.Item, id=item_id)

        
# delete a item
@app.delete("/v1/items/{item_id}", response_model=List[schema.Item])
async def delete_item(item_id : int):
    sql_db_interface.delete_value(database.Item, id=item_id)
    return sql_db_interface.read_all_values(database.Item)

# =======================================#
#      USER      #
# =======================================#


# create a user
@app.post("/v1/users/", response_model=List[schema.User])
async def create_user(user: schema.User):
    user = sql_db_interface.add_value(
        database.User()
    )
    return user

        
# read a user
@app.get("/v1/users/{user_id}", response_model=schema.User)
async def read_user(user_id : int):
    return sql_db_interface.read_value(database.User, id=user_id)

        
# read a user
@app.get("/v1/users/", response_model=List[schema.User])
async def read_users(current_page_number: int = 1):
    return sql_db_interface.read_all_values_with_pagination(
        database.User, number_of_objects_per_page=5, current_page_number=current_page_number
    )

        
# update a user
@app.put("/v1/users/{user_id}", response_model=List[schema.User])
async def update_user(user_id : int):
    return sql_db_interface.update_value(database.User, id=user_id)

        
# delete a user
@app.delete("/v1/users/{user_id}", response_model=List[schema.User])
async def delete_user(user_id : int):
    sql_db_interface.delete_value(database.User, id=user_id)
    return sql_db_interface.read_all_values(database.User)
