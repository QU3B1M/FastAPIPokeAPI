from tortoise import fields
from tortoise.models import Model


class PokeType(Model):
    """PokeType DataBase Model."""

    id: int = fields.BigIntField(pk=True)
    name: str = fields.CharField(max_length=100, unique=True)
    description: str = fields.TextField()

    class PydanticMeta:
        exclude = ["pokemons", "pokemoves"]
