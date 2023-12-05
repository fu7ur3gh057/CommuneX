import socketio

from src.db.dao.client_dao import ClientDAO
from src.db.dao.message_dao import MessageDAO
from src.db.dao.project_dao import ProjectDAO
from src.db.dao.room_dao import RoomDAO
from src.db.dao.user_dao import UserDAO
from src.schemas.chat_schema import ClientCreateSchema
from src.schemas.message_schema import MessageCreateSchema


class RoomNamespace(socketio.AsyncNamespace):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.user_dao = UserDAO()
        self.project_dao = ProjectDAO()
        self.room_dao = RoomDAO()
        self.client_dao = ClientDAO()
        self.message_dao = MessageDAO()

    async def on_enter(self, sid: str, data: dict) -> None:
        is_member = data.get("is_member", False)
        external_id = data.get("external_id", None)
        if not external_id:
            return None
        # Enter as member
        if is_member:
            await self.enter_room(sid=sid, room=external_id)
            return None
        project = data.get("project", None)
        client = await self.client_dao.get_by_external_id(external_id)
        if not client:
            # create client
            schema = ClientCreateSchema(external_id=external_id, project=project)
            await self.client_dao.create(data=schema)
        await self.enter_room(sid=sid, room=external_id)

    async def on_message(self, sid: str, data: dict) -> None:
        schema = MessageCreateSchema(**data)
        message = await self.message_dao.create(data=schema)
        await self.emit(event="BROADCAST", to=message.room, data=message.model_dump())

    async def on_exit(self, sid: str, data: dict) -> None:
        await self.leave_room(sid=sid, room=data["room"])
