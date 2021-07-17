from .base import BaseRepository
from ..models import PokeType


# TODO Update the BaseRepo Models as they are created
class PokeTypeRepository(BaseRepository[PokeType, PokeType, PokeType]):
    """Repository that handles the PokeType CRUD"""

    model: PokeType = PokeType
