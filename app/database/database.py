"""
Developed by: Asad Kareem
Date: 10/03/2022
"""

from app.models.model import Todo
import asyncio

from motor.motor_asyncio import (
    AsyncIOMotorClient as MotorClient,
)

client = MotorClient('mongodb://localhost:27017')
client.get_io_loop = asyncio.get_running_loop

database = client.TodoList
collection = database.todo

async def fetch_one_todo(title):
    """
    Find the todo having specified title
    """
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    """
    Get the list of all todo list
    """
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    """
    Insert a todo into the database
    """
    document = todo
    await collection.insert_one(document)
    
    return document


async def update_todo(title, desc):
    """
    Update a todo with specific title and description
    """
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document

async def remove_todo(title):
    """
    Remove a todo having specified title
    """
    await collection.delete_one({"title": title})
    return True
