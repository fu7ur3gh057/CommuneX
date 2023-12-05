from pydantic import BaseModel

from src.schemas.base_schema import PKIDSchema, TimeStampedSchema


class MessageReadSchema(PKIDSchema, TimeStampedSchema):
    text: str
    images: list[str] = []
    files: list[str] = []
    is_member: bool = False
    sender_id: int
    room: int


class MessageCreateSchema(BaseModel):
    text: str
    is_member: bool = False
    sender_id: int
    room: int
