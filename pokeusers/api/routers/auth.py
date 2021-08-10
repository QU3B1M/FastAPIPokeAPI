from fastapi import APIRouter, HTTPException, Depends, Security
from fastapi.security.http import HTTPAuthorizationCredentials

from api.models import AuthClaim, LoginToken, AccessToken, UserIn, UserOut
from api.repositories import UserRepository
from api.database.schemas import User
from api.security import Auth


router = APIRouter()


@router.post("/register", response_model=UserOut)
async def register(usr_in: UserIn):
    if await UserRepository.exists(username=usr_in.username):
        raise HTTPException(status_code=400, detail="Username already in use.")
    return await UserRepository.create(usr_in)


@router.get("/refresh_token", response_model=AccessToken)
async def refresh_token(auth: HTTPAuthorizationCredentials = Security(Auth.security)):
    return Auth.refresh_token(auth.credentials)


@router.post("/login", response_model=LoginToken)
async def login(auth: AuthClaim):
    user: User = await UserRepository.get(username=auth.username)
    if not user or not Auth.verify_password(auth.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username and/or password.")
    return Auth.generate_tokens(user.username)


@router.get("/")
async def test(auth=Depends(Auth.authenticate)):
    return f"Hola Bolo {auth}"
