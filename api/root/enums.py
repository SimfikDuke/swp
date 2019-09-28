from enum import Enum, IntEnum
from dataclasses import dataclass
from typing import Optional


@dataclass
class DBConfig:
    server: str
    port: int
    name: str
    login: str
    password: str


class UserRole(IntEnum):
    User = 0
    Admin = 777
