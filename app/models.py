from sqlalchemy import Column, Integer, String, Boolean, Date
from .database import Base

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    due_date = Column(Date, nullable=True)

class User(Base):
    __tablename__="Users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True) 
    password = Column(String, nullable=False)               
    email = Column(String, nullable=False, unique=True)     