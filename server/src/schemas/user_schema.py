from pydantic import BaseModel

from src.other.enums import RoleType
from src.schemas.base_schema import PKIDSchema, TimeStampedSchema


class UserReadSchema(PKIDSchema, TimeStampedSchema):
    email: str
    first_name: str
    last_name: str
    is_active: bool = True
    role_type: RoleType = RoleType.USER


class UserUpdateSchema(BaseModel):
    first_name: str
    last_name: str


class UserCreateSchema(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str
    role_type: RoleType = RoleType.USER
