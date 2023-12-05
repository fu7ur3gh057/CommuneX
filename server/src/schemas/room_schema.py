from pydantic import BaseModel

from src.schemas.base_schema import PKIDSchema, TimeStampedSchema


class RoomReadSchema(PKIDSchema, TimeStampedSchema):
    project: int
    owner: int
    membership: list[int] = []
    is_active: bool = False
