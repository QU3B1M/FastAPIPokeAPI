from .base import BaseRepository
from ..schemas import Pokemon


# TODO Update the BaseRepo Models as they are created
class PokemonRepository(BaseRepository[Pokemon, Pokemon, Pokemon]):
    """Repository that handles the Pokemon CRUD"""

    model: Pokemon = Pokemon

    @classmethod
    async def create(cls, obj_in: Pokemon) -> Pokemon:
        return await super().create(obj_in)
