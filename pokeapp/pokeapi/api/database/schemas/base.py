from abc import abstractmethod

from tortoise.models import Model


class BaseSchema(Model):
    """Base DataBase Schema."""

    @abstractmethod
    async def to_pydantic(self):
        """Returns a Pydantic version of the DataBase Model."""
        pass

    @abstractmethod
    async def dict(self):
        """Returns an Dict version of the DataBase Model."""
        pass
