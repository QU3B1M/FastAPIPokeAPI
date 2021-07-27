from enum import Enum

from tortoise import fields
from tortoise.models import Model

from .poketype import PokeType


class PokeMoveCategories(str, Enum):
    """Possibles Pokemon moves Categories."""

    physical: str = "Physical"
    special: str = "Special"
    status: str = "Status"


class PokeMove(Model):
    """PokeMove DataBase Model."""

    id: int = fields.BigIntField(pk=True)
    name: str = fields.CharField(max_length=100)
    effect: str = fields.TextField()
    type: PokeType = fields.ForeignKeyField("models.PokeType")
    category: PokeMoveCategories = fields.CharEnumField(PokeMoveCategories)

    class PydanticMeta:
        exclude = ["pokemons"]
