from tortoise.contrib.pydantic import pydantic_model_creator

from api.database.schemas import PokeMove


PokeMoveOut = pydantic_model_creator(PokeMove, name="PokeMove")
PokeMoveIn = pydantic_model_creator(PokeMove, name="PokeMoveIn", exclude_readonly=True)
