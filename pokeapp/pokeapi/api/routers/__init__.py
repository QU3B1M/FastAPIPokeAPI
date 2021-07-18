from fastapi import APIRouter

from . import pokemon, pokemove, poketype

api_routers = APIRouter()

api_routers.include_router(pokemon.router)
