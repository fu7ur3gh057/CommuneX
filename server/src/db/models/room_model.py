from src.db.models.base import PKIDMixin, TimeStampedMixin
from uuid import uuid4
from tortoise import fields, Model

from src.db.models.project_model import Project
from src.other.enums import RoleType


class Room(Model, PKIDMixin, TimeStampedMixin):
    project: fields.ForeignKeyRelation = fields.ForeignKeyField(
        model_name="models.Project", related_name="rooms", on_delete=fields.CASCADE
    )
    owner: fields.OneToOneRelation["Client"] = fields.OneToOneField(
        model_name="models.Client",
        related_name="owner",
        on_delete=fields.CASCADE,
    )
    membership: fields.ManyToManyRelation["User"] = fields.ManyToManyField(
        model_name="models.User", related_name="rooms"
    )
    is_active: fields.BooleanField = fields.BooleanField(default=False)

    class Meta:
        table = "rooms_room"

    async def to_pydantic(self):
        pass
