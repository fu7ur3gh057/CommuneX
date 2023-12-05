import json
import time

from fastapi import APIRouter, Request, Depends

from src.db.dao.user_dao import UserDAO
from src.schemas.user_schema import UserReadSchema, UserCreateSchema, UserUpdateSchema

router = APIRouter()


@router.get("/{pk_id}")
async def get_user_view(
    pk_id: int, user_dao: UserDAO = Depends()
) -> UserReadSchema | None:
    return await user_dao.get_by_pk(pk_id=pk_id)


@router.get("/all")
async def get_all_users_view(user_dao: UserDAO = Depends()):
    return await user_dao.get_all()


@router.patch("/")
async def update_user_view(
    pk_id: int, data: UserUpdateSchema, user_dao: UserDAO = Depends()
) -> UserReadSchema:
    pass


@router.post("/")
async def create_user_view(
    data: UserCreateSchema, user_dao: UserDAO = Depends()
) -> UserReadSchema:
    return await user_dao.create(data=data)


@router.delete("/")
async def delete_user_view(pk_id: int, user_dao: UserDAO = Depends()):
    return await user_dao.delete(pk_id=pk_id)
