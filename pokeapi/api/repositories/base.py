from typing import Generic, List, TypeVar

from pydantic import BaseModel
from tortoise.models import Model


DBModelType = TypeVar("DBModelType", bound=Model)
InModelType = TypeVar("InModelType", bound=BaseModel)
OutModelType = TypeVar("OutModelType", bound=BaseModel)


class BaseRepository(Generic[DBModelType, InModelType, OutModelType]):
    """Base Repository with all the default methods to handle any CRUD."""

    model: DBModelType
    pydantic: OutModelType

    @classmethod
    async def get(cls, **kwargs) -> DBModelType:
        """Default method to Retrieve an DataBase Record"""
        return await cls.pydantic.from_queryset_single(cls.model.get_or_none(**kwargs))

    @classmethod
    async def filter(cls, **kwargs) -> DBModelType:
        """Default method to Filter Records"""

        return await cls.pydantic.from_queryset(cls.model.filter(**kwargs))

    @classmethod
    async def get_all(cls) -> List[DBModelType]:
        """Default method to Retrieve a List of DataBase Records."""
        return await cls.pydantic.from_queryset(cls.model.all())

    @classmethod
    async def create(cls, obj_in: InModelType) -> DBModelType:
        """Default method to Create an DataBase Record."""

        if not isinstance(obj_in, dict):
            # Converts the object to a dict
            obj_in = obj_in.dict(exclude_unset=True)

        return await cls.pydantic.from_tortoise_orm(await cls.model.create(**obj_in))

    @classmethod
    async def update(cls, obj_in: OutModelType, **kwargs) -> DBModelType:
        """Default method to Update an DataBase Record."""

        if not isinstance(obj_in, dict):
            # Converts the object to a dict
            update_data = obj_in.dict(exclude_unset=True)

        return await cls.model.get(**kwargs).update(**update_data)

    @classmethod
    async def delete(cls, **kwargs) -> None:
        """Default method to Delete an DataBase Record."""
        return await cls.model.get(**kwargs).delete()

    @classmethod
    async def exists(cls, **kwargs) -> None:
        """Default method to check if exists an DataBase Record."""
        return await cls.model.exists(**kwargs)
