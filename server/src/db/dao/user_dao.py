from src.db.models.user_model import User
from src.other.enums import RoleType
from src.schemas.user_schema import UserReadSchema, UserCreateSchema


class UserDAO:
    async def get_by_pk(self, pk_id: int) -> UserReadSchema | None:
        user = await User.get(pk_id=pk_id)
        return user.to_pydantic()

    async def get_all(self) -> list[UserReadSchema]:
        users = await User.all()
        return [user.to_pydantic() for user in users]

    async def filter(
            self, email: str | None = None, role_type: RoleType | None = None
    ) -> list[UserReadSchema]:
        query = await User.all()
        if email:
            query = query.filter(email=email)
        if role_type:
            query = query.filter(role_type=role_type)
        return [user.to_pydantic() for user in query]

    async def create(self, data: UserCreateSchema) -> UserReadSchema | None:
        user = await User.create(**data.model_dump())
        return user.to_pydantic()

    async def update(self) -> None:
        pass

    async def delete(self, pk_id: int) -> bool:
        user = await self.get_by_pk(pk_id=pk_id)
        if not user:
            return False
        await user.delete()
        return True
