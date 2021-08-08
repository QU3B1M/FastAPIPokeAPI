from pydantic.main import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from api.database.schemas import User


UserOut = pydantic_model_creator(User, name="UserOut", exclude=("hashed_password",))
UserFull = pydantic_model_creator(User, name="UserFull")


class UserIn(BaseModel):
    username: str
    password: str
    email: str
