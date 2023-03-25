
from typing import Union, Optional, List
from pydantic import BaseModel

# =======================================#
#      ITEM      #
# =======================================#


class ItemBase(BaseModel):
    title: str
    description: Optional[str]


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# =======================================#
#      USER      #
# =======================================#


class UserBase(BaseModel):
    title: str
    description: Optional[str]


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

