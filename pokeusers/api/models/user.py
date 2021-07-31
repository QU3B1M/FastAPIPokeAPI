from tortoise.contrib.pydantic import pydantic_model_creator

from api.database.schemas import User


UserOut = pydantic_model_creator(User, name="User", exclude=("hashed_password"))
UserIn = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
