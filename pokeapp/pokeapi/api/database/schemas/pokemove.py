from enum import Enum

from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

from .base import BaseSchema
from .poketype import PokeType


class PokeMoveCategories(str, Enum):
    """Possibles Pokemon moves Categories."""

    physical: str = "Physical"
    special: str = "Special"
    status: str = "Status"


class PokeMove(BaseSchema):
    """PokeMove DataBase Model."""

    id: int = fields.BigIntField(pk=True)
    name: str = fields.CharField(max_length=100)
    effect: str = fields.TextField()
    type: PokeType = fields.ForeignKeyField("models.PokeType")
    category: PokeMoveCategories = fields.CharEnumField(PokeMoveCategories)

    async def to_pydantic(self):
        """Returns a Pydantic version of the DataBase Model"""
        return await PydanticPokeMove.from_tortoise_orm(self)

    async def dict(self):
        """Returns an Dict version of the DataBase Model."""
        pokemove: PydanticPokeMove = await self.to_pydantic()
        return {**pokemove.dict(), "type": await self.type}


PydanticPokeMove = pydantic_model_creator(PokeMove, name="PokeMove")
