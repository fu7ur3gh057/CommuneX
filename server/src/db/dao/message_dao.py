from src.schemas.message_schema import MessageReadSchema, MessageCreateSchema


class MessageDAO:
    async def get_by_pk(self, pk_id: int) -> MessageReadSchema | None:
        pass

    async def get_all(self) -> list[MessageReadSchema]:
        pass

    async def get_sender(self, message_id: int, is_sender: bool) -> None:
        pass

    async def create(self, data: MessageCreateSchema) -> MessageReadSchema:
        pass
