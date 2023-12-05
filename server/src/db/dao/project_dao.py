from src.db.models.project_model import Project
from src.schemas.project_schema import ProjectReadSchema, ProjectCreateSchema


class ProjectDAO:
    async def get_by_pk(self, pk_id: int) -> ProjectReadSchema:
        project = await Project.get(pk_id=pk_id)
        return await project.to_pydantic()

    async def get_all(self) -> list[ProjectReadSchema]:
        pass

    async def create(self, data: ProjectCreateSchema) -> ProjectReadSchema:
        project = await Project.create(**data.model_dump())
        return await project.to_pydantic()

    async def add_members(self) -> ProjectReadSchema:
        pass

    async def remove_members(self) -> ProjectReadSchema:
        pass

    async def update(self) -> ProjectReadSchema:
        pass

    async def filter(self) -> list[ProjectReadSchema]:
        pass

    async def delete(self) -> bool:
        pass
