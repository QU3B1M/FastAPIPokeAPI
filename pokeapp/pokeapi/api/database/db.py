from tortoise import Tortoise

from settings import Settings


settings = Settings()


async def init_db():
    """Initializes the database connection"""
    await Tortoise.init(
        db_url=settings.database_url,
        modules={"models": settings.database_models},
    )
    await Tortoise.generate_schemas()


async def close_db():
    """Closes the database connection"""
    await Tortoise.close_connections()
