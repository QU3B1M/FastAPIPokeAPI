from tortoise.contrib.pydantic import pydantic_model_creator

from api.database.schemas import Pokemon


PokemonOut = pydantic_model_creator(Pokemon, name="Pokemon")
PokemonIn = pydantic_model_creator(Pokemon, name="PokemonIn", exclude_readonly=True)
