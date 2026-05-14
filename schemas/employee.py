from pydantic import BaseModel, EmailStr
from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    EMPLOYEE = "employee"

class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: UserRole = UserRole.EMPLOYEE


class EmployeeOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole
    is_active: bool

class PasswordChangeRequest(BaseModel):
    old_password : str
    new_password  : str    

    model_config = {
        "from_attributes": True
    }        