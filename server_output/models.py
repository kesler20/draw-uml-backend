from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from typing import TypedDict, List, Optional


Base = declarative_base()
    

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("Owner", back_populates="")

    def __init__(self, owner : Owner) -> None:
        self.owner = owner
        

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    items = relationship("Items", back_populates="")



    def __init__(self, name : str, items : Items) -> None:
        self.name = name
        self.items = items
        





# BUILD THE TABLES OF THE DATABASE
Base.metadata.create_all(bind=create_engine(f"sqlite:///draw_uml_backend.server_automation.model_generation.sqlite3", echo=True))
    