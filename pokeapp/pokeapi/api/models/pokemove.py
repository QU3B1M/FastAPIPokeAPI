from pydantic import BaseModel

from ..database.schemas import PokeMoveCategories
from .poketype import PokeTypeBase


class PokeMoveBase(BaseModel):

    name: str
    category: PokeMoveCategories
    effect: str


class PokeMoveIn(PokeMoveBase):
    type_id: int


class PokeMoveOut(PokeMoveBase):
    type: PokeTypeBase
    id: int
