from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users_user" (
    "pk_id" BIGSERIAL NOT NULL PRIMARY KEY,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "email" VARCHAR(50) NOT NULL UNIQUE,
    "first_name" VARCHAR(100) NOT NULL,
    "last_name" VARCHAR(100) NOT NULL,
    "password" VARCHAR(255),
    "is_active" BOOL NOT NULL  DEFAULT True,
    "role_type" VARCHAR(5) NOT NULL  DEFAULT 'user'
);
COMMENT ON COLUMN "users_user"."role_type" IS 'ADMIN: admin\nSTAFF: staff\nUSER: user';
CREATE TABLE IF NOT EXISTS "projects_project" (
    "pk_id" BIGSERIAL NOT NULL PRIMARY KEY,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "title" VARCHAR(100) NOT NULL UNIQUE,
    "owner_id" BIGINT NOT NULL REFERENCES "users_user" ("pk_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "chat_clients" (
    "pk_id" BIGSERIAL NOT NULL PRIMARY KEY,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "external_id" VARCHAR(215) NOT NULL UNIQUE,
    "project_id" BIGINT NOT NULL REFERENCES "projects_project" ("pk_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "rooms_room" (
    "pk_id" BIGSERIAL NOT NULL PRIMARY KEY,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "is_active" BOOL NOT NULL  DEFAULT False,
    "project_id" BIGINT NOT NULL REFERENCES "projects_project" ("pk_id") ON DELETE CASCADE,
    "owner_id" BIGINT NOT NULL UNIQUE REFERENCES "chat_clients" ("pk_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "messages_message" (
    "pk_id" BIGSERIAL NOT NULL PRIMARY KEY,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "text" TEXT NOT NULL,
    "images" JSONB,
    "files" JSONB,
    "is_support" BOOL NOT NULL  DEFAULT False,
    "sender_id" INT NOT NULL,
    "room_id" BIGINT NOT NULL REFERENCES "rooms_room" ("pk_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "projects_project_users_user" (
    "projects_project_id" BIGINT NOT NULL REFERENCES "projects_project" ("pk_id") ON DELETE CASCADE,
    "user_id" BIGINT NOT NULL REFERENCES "users_user" ("pk_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "rooms_room_users_user" (
    "rooms_room_id" BIGINT NOT NULL REFERENCES "rooms_room" ("pk_id") ON DELETE CASCADE,
    "user_id" BIGINT NOT NULL REFERENCES "users_user" ("pk_id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
