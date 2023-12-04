from uuid import uuid4

from tortoise import fields


class PKIDMixin:
    pk_id = fields.BigIntField(pk=True, index=True, unique=True)


class UUIDMixin:
    uuid = fields.UUIDField(unique=True, index=True, default=uuid4)


class TimeStampedMixin:
    updated_at = fields.DatetimeField(auto_now_add=True)
    created_at = fields.DatetimeField(auto_now=True)
