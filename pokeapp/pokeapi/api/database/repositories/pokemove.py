from .base import BaseRepository
from ..models import PokeMove


# TODO Update the BaseRepo Models as they are created
class PokeMoveRepository(BaseRepository[PokeMove, PokeMove, PokeMove]):
    """Repository that handles the PokeMove CRUD"""

    model: PokeMove = PokeMove
