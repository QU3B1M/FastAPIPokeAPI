from fastapi.param_functions import Security
from fastapi.security.http import HTTPAuthorizationCredentials

from .auth import Auth


class Deps:
    @staticmethod
    def authorize(auth: HTTPAuthorizationCredentials = Security(Auth.security)) -> str:
        """Dependency to authorize Users."""
        return Auth.decode_token(auth.credentials)
