from pydantic import BaseModel

from ..database.schemas import PokeMoveCategories
from .poketype import PokeTypeBase


class PokeMoveBase(BaseModel):

    name: str
    effect: str
    type: PokeTypeBase
    category: PokeMoveCategories
