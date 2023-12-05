import socketio

from src.db.dao.client_dao import ClientDAO
from src.db.dao.message_dao import MessageDAO
from src.db.dao.project_dao import ProjectDAO
from src.db.dao.room_dao import RoomDAO
from src.db.dao.user_dao import UserDAO


class RoomNamespace(socketio.AsyncNamespace):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.user_dao = UserDAO()
        self.project_dao = ProjectDAO()
        self.room_dao = RoomDAO()
        self.client_dao = ClientDAO()
        self.message_dao = MessageDAO()

    async def on_enter(self, sid: str, data: dict) -> None:
        print(f"Created new room {sid}")
        await self.enter_room(sid=sid, room=sid)
        is_member = data["is_member"]
        external_id = data["external_id"]
        if not is_member:
            await self.enter_room(sid=sid, room=external_id)
            return None
        project = data["project"]
        client = self.client_dao.get_by_external_id(external_id)
        if not client:
            # create client
            pass

    async def on_message(self, sid: str, data: dict) -> None:
        pass

    async def on_exit(self, sid: str, data: dict) -> None:
        pass
