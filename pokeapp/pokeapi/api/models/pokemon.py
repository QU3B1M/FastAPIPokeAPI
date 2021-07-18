from typing import List, Optional
from pydantic import BaseModel

from .poketype import PokeTypeBase
from .pokemove import PokeMoveBase


class PokemonBase(BaseModel):
    id: int
    name: str
    description: str


class PokemonIn(PokemonBase):
    pass
    # types_ids: List[int]
    # moves_ids: List[int]


class PokemonOut(PokemonBase):
    types: Optional[List[PokeTypeBase]]
    moves: Optional[List[PokeMoveBase]]
