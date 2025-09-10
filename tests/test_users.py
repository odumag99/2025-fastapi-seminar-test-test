from fastapi.testclient import TestClient
import pytest

from src.dto import CreateUserRequest
from src.dto import UserResponse
from src.main import app

client = TestClient(app)

# Test for create user

def test_create_user(
    create_user_req: CreateUserRequest
):
    res = client.post("/api/users", json=create_user_req.model_dump())
    res_dto = UserResponse(**res.json())
    
    assert res.status_code == 201
    assert res_dto.user_id is not None
    assert res_dto.name == create_user_req.name
    assert res_dto.phone_number == create_user_req.phone_number
    assert res_dto.height == create_user_req.height

def test_create_user_with_bio(
    create_user_req_with_bio: CreateUserRequest
):
    res = client.post("/api/users", json=create_user_req_with_bio.model_dump())
    res_dto = UserResponse(**res.json())
    
    assert res.status_code == 201
    assert res_dto.user_id is not None
    assert res_dto.name == create_user_req_with_bio.name
    assert res_dto.phone_number == create_user_req_with_bio.phone_number
    assert res_dto.height == create_user_req_with_bio.height
    assert res_dto.bio == create_user_req_with_bio.bio
    
def test_create_user_invalid_number(
    create_user_req_invalid_number: dict[str, str | float]
):
    res = client.post("/api/users", json=create_user_req_invalid_number)
    
    assert res.status_code == 422

# 이름 없을 때

# Phone_number 없을 때

# Phone_number 형식 틀릴 때

# phone_number가 int로 주어졌을 때

# height가 없을 때

# height가 str으로 주어졌을 때

# bio가 500자를 넘을 때

# 두 가지 이상의 조건을 만족하지 못할 때

# Test for get user by id

def test_create_and_get_user_by_id(
    create_user_req: CreateUserRequest
):
    create_response = client.post("/api/users", json=create_user_req.model_dump())
    created_id = UserResponse(**create_response.json()).user_id
    
    res = client.get(f"/api/users/{created_id}")
    res_dto = UserResponse(**res.json())
    
    assert res.status_code == 200
    assert res_dto.user_id == created_id
    assert res_dto.name == create_user_req.name
    assert res_dto.phone_number == create_user_req.phone_number
    assert res_dto.height == create_user_req.height
    

# 없는 id로 조회할 때

# Test for get users with query string

def test_get_users(
    user_list: dict[int, dict]
):
    res = client.get("/api/users?min_height=100&max_height=200")
    list_response = [UserResponse(**r) for r in res.json()]
    
    assert res.status_code == 200
    assert len(list_response) == 20
    
    for user in list_response:
        assert (user.height >= 100 and user.height <= 200)
    
def test_get_users_with_query(
    user_list: dict[int, dict]
):
    res = client.get("/api/users?min_height=177&max_height=182")
    list_response = [UserResponse(**r) for r in res.json()]
    
    assert res.status_code == 200
    assert len(list_response) == 5
    
    for user in list_response:
        assert (user.height >= 177 and user.height <= 182)

# 조건 만족시키는 user가 없을 때