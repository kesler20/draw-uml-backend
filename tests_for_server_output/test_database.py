from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sql_database_interface import SQLDatabaseInterface
from sqlalchemy.orm import declarative_base


# INSTANTIATE SQL DATABASE INTERFACE
sql_db_interface = SQLDatabaseInterface()
Base = declarative_base()
engine = sql_db_interface.engine


# DEFINE DATABASE MODELS
class User(Base):  # type: ignore
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")


class Item(Base):  # type: ignore
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")


# BUILD THE TABLES OF THE DATABASE
Base.metadata.create_all(bind=engine)
