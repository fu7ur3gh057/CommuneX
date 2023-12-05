from typing import Any

from src.db.models.base import PKIDMixin, TimeStampedMixin
from uuid import uuid4
from tortoise import fields, Model


class Message(Model, PKIDMixin, TimeStampedMixin):
    text: fields.TextField = fields.TextField()
    images: fields.JSONField = fields.JSONField(null=True)
    files: fields.JSONField = fields.JSONField(null=True)
    # Sender
    sender_id: fields.IntField = fields.IntField()
    is_member: fields.BooleanField = fields.BooleanField(default=False)
    # Room
    room: fields.ForeignKeyRelation = fields.ForeignKeyField(
        model_name="models.Room", related_name="messages", on_delete=fields.CASCADE
    )

    class Meta:
        table = "messages_message"

    async def add_images(self, images: list[str]) -> None:
        self.images = images
        await self.save()

    async def add_files(self, files: list[str]) -> None:
        self.files = files
        await self.save()

    # async def get_sender(self):
    #     if self.is_support:
    #         return await Support.get(pk_id=self.sender_id)
    #     else:
    #         return await Client.get(pk_id=self.sender_id)
