from enum import Enum

from tortoise import fields
from tortoise.models import Model


class PokeMoveCategories(str, Enum):
    """Possibles Pokemon moves Categories."""

    physical: str = "Physical"
    special: str = "Special"
    status: str = "Status"


class PokeGenders(str, Enum):
    """Possibles Pokemon Genders."""

    male: str = "Male"
    female: str = "Female"


class PokeType(Model):
    """PokeType DataBase Model."""

    name: str = fields.CharField(pk=True, max_length=100)


class PokeMove(Model):
    """PokeMove DataBase Model."""

    name: str = fields.CharField(max_length=100)
    effect: str = fields.TextField()
    type: PokeType = fields.ForeignKeyField("models.PokeType")
    category: PokeMoveCategories = fields.CharEnumField(PokeMoveCategories)


class Pokemon(Model):
    """Pokemon DataBase Model."""

    id: int = fields.IntField(pk=True)
    name: str = fields.CharField(max_length=100, unique=True)
    description: str = fields.TextField()
    gender: PokeGenders = fields.CharEnumField(PokeGenders)
    types: list[PokeType] = fields.ManyToManyField("models.PokeType")
    moves: list[PokeMove] = fields.ManyToManyField("models.PokeType")
