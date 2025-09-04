import fastapi
from fastapi import HTTPException
from src.dto import CreateUserRequest, UserResponse
from fastapi import Query

app = fastapi.FastAPI()

user_db = {}


@app.post("/api/user")
def create_user(request: CreateUserRequest) -> UserResponse:
    # Todo

    return 0


@app.get("/api/user/{user_id}")
def get_user(
    # Todo
    
) -> UserResponse:
    # Todo

    return 0


@app.get("/api/user/")
def get_users(
    # Todo

) -> list[UserResponse]:
    # Todo

    return 0