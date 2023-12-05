from pydantic import BaseModel

from src.schemas.base_schema import PKIDSchema, TimeStampedSchema
from src.schemas.user_schema import UserReadSchema


class ClientReadSchema(PKIDSchema, TimeStampedSchema):
    external_id: str
    project: int


class ClientCreateSchema(BaseModel):
    external_id: str
    project: int
