from pydantic import BaseModel

from src.schemas.base_schema import PKIDSchema, TimeStampedSchema


class MessageSchema(PKIDSchema, TimeStampedSchema):
    text: str
    images: list[str] = []
    files: list[str] = []
    is_support: bool = False
    sender_id: int
    room: int


class MessageCreateSchema(BaseModel):
    text: str
    is_support: bool = False
    sender_id: int
    room: int
