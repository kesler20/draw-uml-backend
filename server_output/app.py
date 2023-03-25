
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

# =======================================#
#      ITEM      #
# =======================================#


# create a item
@app.post("/v1/items/", response_model=List[schema.Item])
async def create_item(item: schema.Item):
  items = []
  # do something
  return items

        
# read a item
@app.get("/v1/items/{item_id}", response_model=schema.Item)
async def read_item(item_id : int):
  item = []
  # do something
  return item

        
# update a item
@app.put("/v1/items/{item_id}", response_model=List[schema.Item])
async def update_item(item_id : int):
  items = []
  # do something
  return items

        
# delete a item
@app.delete("/v1/items/{item_id}", response_model=List[schema.Item])
async def delete_item(item_id : int):
  items = []
  # do something
  return items

# =======================================#
#      USER      #
# =======================================#


# create a user
@app.post("/v1/users/", response_model=List[schema.User])
async def create_user(user: schema.User):
  users = []
  # do something
  return users

        
# read a user
@app.get("/v1/users/{user_id}", response_model=schema.User)
async def read_user(user_id : int):
  user = []
  # do something
  return user

        
# update a user
@app.put("/v1/users/{user_id}", response_model=List[schema.User])
async def update_user(user_id : int):
  users = []
  # do something
  return users

        
# delete a user
@app.delete("/v1/users/{user_id}", response_model=List[schema.User])
async def delete_user(user_id : int):
  users = []
  # do something
  return users
