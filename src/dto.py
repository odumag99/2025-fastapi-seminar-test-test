from pydantic import BaseModel
import re
from fastapi import HTTPException
from pydantic import BeforeValidator

class CreateUserRequest(BaseModel):
    # Todo
    name: str
    phone_number: str
    bio: str
    height: int

    @BeforeValidator
    def validate_phone_number(cls, v):
        if not re.match(r"^\d{3}-\d{4}-\d{4}$", v):
            raise HTTPException(status_code=400, detail="Invalid phone number format")
        return v

    @BeforeValidator
    def validate_bio(cls, v):
        if len(v) > 500:
            raise HTTPException(status_code=400, detail="Bio is too long")
        return v

class UserResponse(BaseModel):
    # Todo
    user_id: int
    name: str
    phone_number: str
    bio: str
    height: int