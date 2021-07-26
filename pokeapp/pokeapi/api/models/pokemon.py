from typing import List

from tortoise.contrib.pydantic import pydantic_model_creator

from api.database.schemas import Pokemon


# Base Pokemon Pydantic Model created from the Tortoise-ORM Model.
PokemonBase = pydantic_model_creator(Pokemon, name="PokemonIn", exclude_readonly=True)
# Outgoing Pokemon Pydantic Model created from the Tortoise-ORM Model.
PokemonOut = pydantic_model_creator(Pokemon, name="Pokemon")


class PokemonIn(PokemonBase):
    """Incoming Pokemon Pydantic Model."""

    types_ids: List[int]
    moves_ids: List[int]


class PokemonUpdate(PokemonBase):
    """Update Pokemon Pydantic Model."""

    types_to_add: List[int]
    moves_to_add: List[int]
    types_to_del: List[int]
    moves_to_del: List[int]
