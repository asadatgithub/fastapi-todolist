"""
Developed by: Asad Kareem
Date: 10/03/2022
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.json() == {"message": "Hello Websential Developer!"}


def test_post():
    data = {"title": "Develop Something","description": "Have to work on the development of FastAPI"}
    respose = client.post("/api/todo/", json= data,)
    assert respose.status_code == 200
    assert respose.json() == data

def test_put():
    response = client.put("/api/todo/Develop%20Something/?desc=test%20description")
    assert response.status_code == 200
    response = client.put("/api/todo/NotFound/?desc=test%20description")
    assert response.status_code == 404

def test_get():
    response = client.get("http://127.0.0.1:8000/api/todo/string")
    assert response.status_code == 200
    assert response.json() == {"title": "string","description": "string"}

def test_get_all():
    response = client.get("http://127.0.0.1:8000/api/todo")
    assert response.status_code == 200

def test_delete():
    response = client.delete("http://127.0.0.1:8000/api/todo/Develop%20Something")
    response.status_code == 200
    response.json() == "Successfully deleted todo"
    response = client.delete("http://127.0.0.1:8000/api/todo/Develop%20Something%20NotInDatabase")
    response.status_code == 404