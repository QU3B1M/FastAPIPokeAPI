from fastapi import FastAPI

from api.database.db import init_db, close_db
from api.routers import api_routers

app = FastAPI()

app.include_router(api_routers)


@app.on_event("startup")
async def startup_event():
    """Event that runs before the app starts."""
    await init_db()


@app.on_event("shutdown")
async def shutdown_event():
    """Event that runs after the app stops."""
    await close_db()
