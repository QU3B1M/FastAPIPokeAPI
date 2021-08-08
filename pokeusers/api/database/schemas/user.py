from tortoise import fields
from tortoise.models import Model


class User(Model):
    """User DataBase Model."""

    id: int = fields.BigIntField(pk=True)
    username: str = fields.CharField(max_length=100, unique=True)
    email: str = fields.CharField(max_length=255, unique=True)
    hashed_password: str = fields.CharField(max_length=255)
    is_active: bool = fields.BooleanField(default=False)

    # class PydanticMeta:
    #     exclude = ["hashed_password"]
