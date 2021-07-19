from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

from .base import BaseSchema


class PokeType(BaseSchema):
    """PokeType DataBase Model."""

    id: int = fields.BigIntField(pk=True)
    name: str = fields.CharField(max_length=100, unique=True)
    description: str = fields.TextField()

    async def to_pydantic(self):
        """Returns a Pydantic version of the DataBase Model"""
        return await _PydanticPokeType.from_tortoise_orm(self)

    async def dict(self):
        """Returns an Dict version of the DataBase Model."""
        poketype: _PydanticPokeType = await self.to_pydantic()
        return poketype.dict()


_PydanticPokeType = pydantic_model_creator(PokeType, name="PokeType")
