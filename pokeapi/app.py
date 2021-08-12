import uvicorn
from fastapi import FastAPI

from api import api_routers, init_database
from settings import Settings


settings = Settings()
app = FastAPI(
    openapi_url=f"{settings.api_prefix}/openapi.json",
    docs_url=f"{settings.api_prefix}/docs",
)

app.include_router(api_routers, prefix=settings.api_prefix)
init_database(app=app)


if __name__ == "__main__":
    # Start main server loop
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True if settings.app_mode == "Development" else False,
    )
