from datetime import datetime, timedelta
from typing import Any, Optional

from fastapi import HTTPException, status, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel

from settings import Settings


settings = Settings()


class Token(BaseModel):
    """Model for the login output."""

    token_type: Optional[str] = "Bearer"
    access_token: str


class CredentialException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_401_UNAUTHORIZED,
        detail: Any = "Could not validate credentials",
    ) -> None:
        self.headers = {"WWW-Authenticate": "Bearer"}
        super().__init__(status_code, detail=detail, headers=self.headers)


class Auth:

    _security = HTTPBearer()
    _context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def hash_password(cls, password: str) -> str:
        """Retrieves a hashed password."""
        return cls._context.hash(password)

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        """Verifies a password."""
        return cls._context.verify(plain_password, hashed_password)

    @classmethod
    def encode_token(cls, user_id: Any) -> str:
        payload = {
            "exp": datetime.utcnow() + timedelta(days=0, minutes=5),
            "iat": datetime.utcnow(),
            "sub": str(user_id),
        }
        return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)

    @staticmethod
    def decode_token(token: str) -> str:
        try:
            payload = jwt.decode(
                token, settings.secret_key, algorithms=[settings.algorithm]
            )
            return payload["sub"]
        except ExpiredSignatureError:
            raise CredentialException(detail="Signature has expired")
        except JWTError as e:
            raise CredentialException(detail=str(e))

    @classmethod
    def login(cls, user_id: Any) -> str:
        token = cls.encode_token(user_id)
        return Token(access_token=token)

    @classmethod
    def auth_wrapper(
        cls, auth: HTTPAuthorizationCredentials = Security(_security)
    ) -> str:
        return cls.decode_token(auth.credentials)
