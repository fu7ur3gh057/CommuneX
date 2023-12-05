from fastapi.routing import APIRouter
from src.web.api import monitoring, users, projects, support, clients, rooms, messages

api_router = APIRouter()
api_router.include_router(router=monitoring.router, tags=["Monitoring"])
api_router.include_router(router=users.router, prefix="/users", tags=["Users"])
api_router.include_router(router=projects.router, prefix="/projects", tags=["Projects"])
api_router.include_router(router=support.router, prefix="/support", tags=["Support"])
api_router.include_router(router=clients.router, prefix="/clients", tags=["Clients"])
api_router.include_router(router=rooms.router, prefix="/rooms", tags=["Rooms"])
api_router.include_router(router=messages.router, prefix="/messages", tags=["Messages"])
