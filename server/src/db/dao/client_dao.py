from src.schemas.chat_schema import ClientReadSchema


class ClientDAO:
    async def get_by_pk(self, pk_id: int) -> ClientReadSchema | None:
        pass

    async def get_by_external_id(self, external_id: int) -> ClientReadSchema | None:
        pass
