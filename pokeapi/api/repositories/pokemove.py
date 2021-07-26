from api.database.schemas import PokeMove
from api.models import PokeMoveIn, PokeMoveOut
from .base import BaseRepository


class PokeMoveRepository(BaseRepository[PokeMove, PokeMoveIn, PokeMoveOut]):
    """Repository that handles the PokeMove CRUD"""

    model: PokeMove = PokeMove
    pydantic: PokeMoveOut = PokeMoveOut
