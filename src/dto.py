from pydantic import BaseModel, field_validator
import re

class CreateUserRequest(BaseModel):
    # Todo
    name: str
    phone_number: str
    bio: str | None = None
    height: int
    
    @field_validator('phone_number')
    def validate_phone_number(cls, v):
        if not re.match(r"^010-\d{4}-\d{4}$", v):
            raise ValueError("Invalid phone number format. Must be 010-XXXX-XXXX.")
        return v

    @field_validator('bio')
    def validate_bio(cls, v):
        if v and len(v) > 500:
            raise ValueError("Bio must be 500 characters or less.")
        return v

class UserResponse(BaseModel):
    # Todo
    user_id: int
    name: str
    phone_number: str
    bio: str | None = None
    height: int
