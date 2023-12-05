from pydantic import BaseModel

from src.schemas.base_schema import PKIDSchema, TimeStampedSchema


class ProjectReadSchema(PKIDSchema, TimeStampedSchema):
    owner: int
    title: str
    membership: list[int]


class ProjectCreateSchema(BaseModel):
    owner: int
    title: str
