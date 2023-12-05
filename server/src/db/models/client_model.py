from tortoise import fields, Model

from src.db.models.base import PKIDMixin, TimeStampedMixin
from src.db.models.message_model import Message
from src.db.models.room_model import Room


# class Support(Model, PKIDMixin, TimeStampedMixin):
#     user: fields.OneToOneRelation[User] = fields.OneToOneField(
#         model_name="models.User",
#         related_name="support",
#         on_delete=fields.CASCADE,
#     )
#
#     class Meta:
#         table = "chat_support"
#
#     async def get_rooms(self) -> list[Room] | None:
#         rooms = await Room.filter(support_team=[self])
#         return rooms
#
#     async def get_messages(self) -> list[Message] | None:
#         messages = await Message.filter(is_support=True, sender_id=self.pk_id).all()
#         return messages
#
#     async def to_pydantic(self):
#         pass


class Client(Model, PKIDMixin, TimeStampedMixin):
    external_id: fields.CharField = fields.CharField(max_length=215, unique=True)
    project: fields.ForeignKeyRelation = fields.ForeignKeyField(
        model_name="models.Project", related_name="clients", on_delete=fields.CASCADE
    )

    class Meta:
        table = "chat_clients"

    async def get_room(self) -> Room | None:
        room = await Room.get(owner=self)
        return room

    async def get_messages(self) -> list[Message] | None:
        messages = await Message.filter(is_support=False, sender_id=self.pk_id).all()
        return messages

    async def to_pydantic(self):
        pass
