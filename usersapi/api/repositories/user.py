from api.database.schemas import User
from api.models import UserIn, UserFull
from api.core import Auth
from .base import BaseRepository


class UserRepository(BaseRepository[User, UserIn, UserFull]):
    """Repository that handles the User CRUD"""

    model: User = User
    pydantic: UserFull = UserFull

    @classmethod
    async def create(cls, usr_in: UserIn) -> UserFull:
        """Creates a User with his password hashed."""
        hashed_pwd: str = Auth.hash_password(usr_in.password)

        return await User.create(**usr_in.dict(), hashed_password=hashed_pwd)
