from fastapi import HTTPException, status
from fastapi.security import HTTPBearer
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError
from passlib.context import CryptContext

from settings import Settings


settings = Settings()


class CredentialException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_401_UNAUTHORIZED,
        detail: str = "Could not validate credentials",
    ) -> None:
        self.headers = {"WWW-Authenticate": "Bearer"}
        super().__init__(status_code, detail=detail, headers=self.headers)


class Auth:

    security = HTTPBearer()
    _context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        """Verifies a password."""
        return cls._context.verify(plain_password, hashed_password)

    @staticmethod
    def decode_token(token: str) -> str:
        """Retrieve an decoded JWT Token."""
        try:
            payload = jwt.decode(
                token, settings.secret_key, algorithms=[settings.algorithm]
            )
            if payload["scope"] != "access_token":
                raise CredentialException(detail="Invalid token scope.")
            return payload["sub"]
        except ExpiredSignatureError:
            raise CredentialException(detail="Signature has expired.")
        except JWTError as e:
            raise CredentialException(detail=str(e))
