from enum import Enum
from typing import List

from tortoise import fields
from tortoise.models import Model

from .poketype import PokeType
from .pokemove import PokeMove


class Pokemon(Model):
    """Pokemon DataBase Model."""

    id: int = fields.IntField(pk=True)
    name: str = fields.CharField(max_length=100, unique=True)
    description: str = fields.TextField()
    types: List[PokeType] = fields.ManyToManyField("models.PokeType")
    moves: List[PokeMove] = fields.ManyToManyField("models.PokeMove")
