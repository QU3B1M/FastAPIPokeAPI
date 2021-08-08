from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends

from api.models import AuthClaim, UserIn, UserOut
from api.repositories import UserRepository
from api.database.schemas import User
from api.security import Auth


router = APIRouter()


@router.post("/register", response_model=UserOut)
async def register(usr_in: UserIn):
    if await UserRepository.exists(username=usr_in.username):
        raise HTTPException(status_code=400, detail="Username already in use.")
    return await UserRepository.create(usr_in)


@router.post("/login")
async def login(auth: AuthClaim):
    user: User = await UserRepository.get(username=auth.username)
    if not user or not Auth.verify_password(auth.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username and/or password.")
    return Auth.login(user.id)


@router.get("/")
async def test(auth=Depends(Auth.auth_wrapper)):
    return f"Hola Bolo {auth}"
