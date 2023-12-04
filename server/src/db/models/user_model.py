from src.db.models.base import PKIDMixin, TimeStampedMixin
from uuid import uuid4
from tortoise import fields, Model

from src.other.enums import RoleType


class User(Model, PKIDMixin, TimeStampedMixin):
    email = fields.CharField(max_length=50, unique=True, null=False)
    password = fields.CharField(max_length=255, null=True)
    is_active = fields.BooleanField(default=True)
    role_type = fields.CharEnumField(RoleType, default=RoleType.USER)

    class Meta:
        table = "users_user"

    async def to_pydantic(self):
        pass