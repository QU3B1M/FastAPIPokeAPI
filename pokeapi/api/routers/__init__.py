from fastapi import APIRouter, Depends

from api.core import Deps
from . import pokemon, pokemove, poketype

api_routers = APIRouter(
    dependencies=[
        Depends(Deps.authorize),
    ]
)

api_routers.include_router(pokemon.router)
api_routers.include_router(pokemove.router)
api_routers.include_router(poketype.router)
