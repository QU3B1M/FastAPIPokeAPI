from tortoise.contrib.pydantic import pydantic_model_creator

from api.database.schemas import PokeType


PokeTypeOut = pydantic_model_creator(PokeType, name="PokeType")
PokeTypeIn = pydantic_model_creator(PokeType, name="PokeTypeIn", exclude_readonly=True)
