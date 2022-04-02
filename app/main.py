"""
Developed by: Asad Kareem
Date: 10/03/2022
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.user_controller import router


app = FastAPI()
app.include_router(router)
origins = [
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    """
    Function to greet a developer using this skeleton
    :return: dictionary containing a message
    """
    return {"message": "Hello Websential Developer!"}
