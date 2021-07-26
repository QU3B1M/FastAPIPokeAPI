from fastapi import FastAPI

from api import api_routers, init_database

app = FastAPI()

app.include_router(api_routers)

init_database(app=app)
