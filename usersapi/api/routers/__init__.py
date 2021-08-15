from fastapi import APIRouter

from . import auth


api_routers = APIRouter()

api_routers.include_router(auth.router)
