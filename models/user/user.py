from sqlmodel import Field

from models.user.user_base import UserBase


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str
