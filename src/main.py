import fastapi

from fastapi import status
from src.dto import CreateUserRequest, UserResponse
from fastapi import Query

app = fastapi.FastAPI()


user_db = {}


@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def create_user(request: CreateUserRequest) -> UserResponse:
    user_id = len(user_db) + 1
    user_db[user_id] = request.model_dump()

    return UserResponse(
        user_id=user_id,
        name=request.name,
        phone_number=request.phone_number,
        bio=request.bio,
        height=request.height
    )



@app.get("/api/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int) -> UserResponse:
    user = user_db.get(user_id)
    if user is None:
        raise ValueError("User not found")
    return UserResponse(
        user_id=user_id,
        **user
    )


@app.get("/api/users", status_code=status.HTTP_200_OK)
def get_user(
    min_height: int = Query(...),
    max_height: int = Query(...)
) -> list[UserResponse]:
    users = [
        UserResponse(
            user_id=user_id,
            **user
        )
        for user_id, user in user_db.items()
        if min_height <= user["height"] <= max_height
    ]
    return users