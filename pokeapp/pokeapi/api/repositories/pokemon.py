from api.database.schemas import Pokemon
from api.models import PokemonIn, PokemonOut
from .base import BaseRepository


class PokemonRepository(BaseRepository[Pokemon, PokemonIn, PokemonOut]):
    """Repository that handles the Pokemon CRUD"""

    model: Pokemon = Pokemon
    pydantic: PokemonOut = PokemonOut
