from typing import Generic, List, TypeVar

from pydantic import BaseModel
from tortoise.models import Model


DBModelType = TypeVar("DBModelType", bound=Model)
CreateModelType = TypeVar("CreateModelType", bound=BaseModel)
UpdateModelType = TypeVar("UpdateModelType", bound=BaseModel)


class BaseRepository(Generic[DBModelType, CreateModelType, UpdateModelType]):
    """Base Repository with all the default methods to handle any CRUD."""

    model: DBModelType

    @classmethod
    async def get(cls, **kwargs) -> DBModelType:
        """Default method to Retrieve an DataBase Record"""
        return await cls.model.get_or_none(**kwargs)

    @classmethod
    async def filter(cls, **kwargs) -> DBModelType:
        """Default method to Filter Records"""

        return await cls.model.filter(**kwargs)

    @classmethod
    async def get_all(cls) -> List[DBModelType]:
        """Default method to Retrieve a List of DataBase Records."""
        return await cls.model.all()

    @classmethod
    async def create(cls, obj_in: CreateModelType) -> DBModelType:
        """Default method to Create an DataBase Record."""

        if not isinstance(obj_in, dict):
            # Converts the object to a dict
            obj_in = obj_in.dict(exclude_unset=True)

        return await cls.model.create(**obj_in)

    @classmethod
    async def update(cls, obj_in: UpdateModelType, **kwargs) -> DBModelType:
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
