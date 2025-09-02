from pydantic import BaseModel
import re
from fastapi import HTTPException
from pydantic import BeforeValidator

class CreateUserRequest(BaseModel):
    # Todo
    pass

class UserResponse(BaseModel):
    # Todo
    pass