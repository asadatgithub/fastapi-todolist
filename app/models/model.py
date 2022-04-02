"""
Developed by: Asad Kareem
Date: 10/03/2022
"""
from pydantic import BaseModel

class Todo(BaseModel):
    """
    Base model for todo list
    title: title of the todo
    description: description of the todo
    """
    title: str
    description: str
