from datetime import datetime

from pydantic import BaseModel


class PKIDSchema(BaseModel):
    pk_id: int


class TimeStampedSchema(BaseModel):
    created_at: datetime
    updated_at: datetime | None = None
