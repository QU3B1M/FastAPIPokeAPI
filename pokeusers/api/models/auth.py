from typing import Optional

from pydantic import BaseModel


class AuthClaim(BaseModel):
    """Model for the Login/Auth body."""

    username: str
    password: str


class AccessToken(BaseModel):
    """Model for the Access Token"""

    token_type: Optional[str] = "Bearer"
    access_token: str


class LoginToken(AccessToken):
    """Model for the login output."""

    refresh_token: str
