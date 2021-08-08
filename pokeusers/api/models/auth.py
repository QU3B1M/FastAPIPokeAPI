from pydantic import BaseModel


class AuthClaim(BaseModel):
    """Model for the Login/Auth body."""

    username: str
    password: str
