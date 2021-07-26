from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from settings import Settings


settings = Settings()


def init_database(app: FastAPI):
    """Initializes the database connection"""
    register_tortoise(
        app,
        db_url=settings.database_url,
        modules={
            "models": settings.database_models,
        },
        generate_schemas=True,
        add_exception_handlers=True,
    )


Tortoise.init_models(models_paths=settings.database_models, app_label="models")
