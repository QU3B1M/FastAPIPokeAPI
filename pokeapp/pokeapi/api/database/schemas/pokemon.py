from enum import Enum
from typing import List

from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

from .base import BaseSchema
from .poketype import PokeType
from .pokemove import PokeMove


class PokeGenders(str, Enum):
    """Possibles Pokemon Genders."""

    male: str = "Male"
    female: str = "Female"


class Pokemon(BaseSchema):
    """Pokemon DataBase Model."""

    id: int = fields.IntField(pk=True)
    name: str = fields.CharField(max_length=100, unique=True)
    description: str = fields.TextField()
    # gender: PokeGenders = fields.CharEnumField(PokeGenders)
    types: List[PokeType] = fields.ManyToManyField("models.PokeType")
    moves: List[PokeMove] = fields.ManyToManyField("models.PokeMove")

    async def to_pydantic(self):
        """Returns a Pydantic version of the DataBase Model"""
        return await PydanticPokemon.from_tortoise_orm(self)

    async def dict(self) -> dict:
        """Returns an Dict version of the DataBase Model."""
        self.to_pydantic()


PydanticPokemon = pydantic_model_creator(Pokemon, name="Pokemon")
