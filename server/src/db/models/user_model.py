from src.db.models.base import PKIDMixin, TimeStampedMixin
from uuid import uuid4
from tortoise import fields, Model

from src.other.enums import RoleType
from src.schemas.user_schema import UserReadSchema


class User(Model, PKIDMixin, TimeStampedMixin):
    email: fields.CharField = fields.CharField(max_length=50, unique=True, null=False)
    first_name: fields.CharField = fields.CharField(max_length=100, null=False)
    last_name: fields.CharField = fields.CharField(max_length=100, null=False)
    password: fields.CharField = fields.CharField(max_length=255, null=True)
    is_active: fields.BooleanField = fields.BooleanField(default=True)
    role_type: fields.CharEnumField = fields.CharEnumField(
        RoleType, default=RoleType.USER
    )

    class Meta:
        table = "users_user"

    def to_pydantic(self) -> UserReadSchema:
        return UserReadSchema(
            pk_id=self.pk_id,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            is_active=self.is_active,
            role_type=self.role_type,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
