from datetime import datetime, timedelta

from fastapi import HTTPException, status, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError
from passlib.context import CryptContext

from settings import Settings
from api.models import LoginToken, AccessToken


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
    def hash_password(cls, password: str) -> str:
        """Retrieves a hashed password."""
        return cls._context.hash(password)

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        """Verifies a password."""
        return cls._context.verify(plain_password, hashed_password)

    @classmethod
    def encode_token(cls, username: str) -> str:
        """Generates a JWT Token."""
        payload = {
            "exp": datetime.utcnow() + timedelta(days=0, minutes=5),
            "iat": datetime.utcnow(),
            "scope": "access_token",
            "sub": str(username),
        }
        return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)

    @staticmethod
    def decode_token(token: str) -> str:
        """Retrieve an decoded JWT Token."""
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
    def encode_refresh_token(cls, username: str):
        payload = {
            "exp": datetime.utcnow() + timedelta(days=0, hours=10),
            "iat": datetime.utcnow(),
            "scope": "refresh_token",
            "sub": str(username),
        }
        return jwt.encode(payload, settings.secret_key, settings.algorithm)

    @classmethod
    def refresh_token(cls, refresh_token: str):
        try:
            payload = jwt.decode(
                refresh_token, settings.secret_key, algorithms=[settings.algorithm]
            )
            if payload["scope"] != "refresh_token":
                raise HTTPException(status_code=401, detail="Invalid scope for token")
            username = payload["sub"]
            return AccessToken(access_token=cls.encode_token(username))
        except ExpiredSignatureError:
            raise CredentialException(detail="Refresh Token has expired")
        except JWTError as e:
            raise CredentialException(detail=str(e))

    @classmethod
    def generate_tokens(cls, username: str) -> str:
        """Retrieves the acces_token/refresh_token pair."""
        access_token = cls.encode_token(username)
        refresh_token = cls.encode_refresh_token(username)
        return LoginToken(access_token=access_token, refresh_token=refresh_token)

    @classmethod
    def authenticate(
        cls, auth: HTTPAuthorizationCredentials = Security(security)
    ) -> str:
        """Dependency to authenticate Users."""
        return cls.decode_token(auth.credentials)
