from tortoise import fields
from tortoise.models import Model


class PokeType(Model):
    """PokeType DataBase Model."""

    name: str = fields.CharField(pk=True, max_length=100)
