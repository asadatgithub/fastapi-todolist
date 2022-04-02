"""
Base Controller for all the operations
Developed by: Asad Kareem
Date: 10/03/2022
"""

from fastapi import APIRouter, HTTPException, status
from app.database.database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)
from app.models.model import Todo

router = APIRouter(tags=["Todos"])


@router.get("/api/todo")
async def get_todo():
    """
    Get the list of all todos
    """
    response = await fetch_all_todos()
    return response

@router.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title):
    """
    title: title of the todo
    returns the response if the todo with the title exists
    """
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.post("/api/todo/", response_model=Todo)
async def post_todo(todo: Todo):
    """
    Todo: A todo object
    returns response if the todo was inserted into the database
    """
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

@router.put("/api/todo/{title}/", response_model=Todo)
async def put_todo(title: str, desc: str):
    """
    Update a todo having a specified title with description
    """
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/api/todo/{title}")
async def delete_todo(title):
    """
    title: the title of the todo
    returns message if the todo was deleted
    """
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
