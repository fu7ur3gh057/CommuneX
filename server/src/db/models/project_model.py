from src.db.models.base import PKIDMixin, TimeStampedMixin
from uuid import uuid4
from tortoise import fields, Model

from src.schemas.project_schema import ProjectReadSchema


class Project(Model, PKIDMixin, TimeStampedMixin):
    owner: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        model_name="models.User",
        related_name="owner_projects",
        on_delete=fields.CASCADE,
    )
    # support: fields.ManyToManyRelation[]
    title: fields.CharField = fields.CharField(max_length=100, unique=True, null=False)
    membership: fields.ManyToManyRelation["User"] = fields.ManyToManyField(
        model_name="models.User",
        related_name="support_projects",
    )

    class Meta:
        table = "projects_project"

    async def to_pydantic(self) -> ProjectReadSchema:
        membership = [user.pk_id for user in await self.membership.all()]
        return ProjectReadSchema(
            owner=self.owner.pk_id, members=membership, title=self.title
        )
