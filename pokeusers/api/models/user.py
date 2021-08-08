from tortoise.contrib.pydantic import pydantic_model_creator

from api.database.schemas import User


UserBase = pydantic_model_creator(User, name="User", exclude=("hashed_password"))


class UserIn(UserBase):
    password: str
