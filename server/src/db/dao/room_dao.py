from src.schemas.room_schema import RoomReadSchema


class RoomDAO:
    async def get_by_pk(self, pk_id: int) -> RoomReadSchema:
        pass
