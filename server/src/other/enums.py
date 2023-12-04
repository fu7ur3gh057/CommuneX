from enum import Enum


class RoleType(str, Enum):
    ADMIN = "admin"
    STAFF = "staff"
    USER = "user"


class NotificationType(str, Enum):
    SYSTEM = "system"
    MESSAGE = "message"


class FileType(str, Enum):
    AUDIO = "audio"
    IMAGE = "image"
    VIDEO = "video"
    DOCUMENT = "document"
    OTHER = "other"


class SocketEmit(str, Enum):
    JOIN = "join"
    BROADCAST = "broadcast"
    LEAVE = "leave"
