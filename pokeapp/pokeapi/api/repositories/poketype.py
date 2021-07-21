from api.database.schemas import PokeType
from api.models import PokeTypeIn, PokeTypeOut
from .base import BaseRepository


class PokeTypeRepository(BaseRepository[PokeType, PokeTypeIn, PokeTypeOut]):
    """Repository that handles the PokeType CRUD"""

    model: PokeType = PokeType
    pydantic: PokeTypeOut = PokeTypeOut
