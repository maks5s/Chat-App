from typing import List

from fastapi import APIRouter, Response
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.exceptions import UserAlreadyExistsException, PasswordMismatchException, IncorrectEmailOrPasswordException
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UsersDAO
from app.users.schemas import SUserRegister, SUserAuth, SUserRead

router = APIRouter(prefix="/auth", tags=["Auth"])

templates = Jinja2Templates(directory='app/templates')


@router.get("/users", response_model=List[SUserRead])
async def get_users():
    users_all = await UsersDAO.find_all()
    return [{'id': user.id, 'name': user.name} for user in users_all]


@router.get("/", response_class=HTMLResponse, summary="Auth page")
async def get_categories(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})


@router.post("/register/")
async def register_user(user_data: SUserRegister) -> dict:
    user = await UsersDAO.find_one_or_none(email=user_data.email)
    if user:
        raise UserAlreadyExistsException

    if user_data.password != user_data.password_check:
        raise PasswordMismatchException("Passwords do not match")

    hashed_password = get_password_hash(user_data.password)

    await UsersDAO.add(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_password
    )

    return {"message": "You have been successfully registered"}


@router.post("/login/")
async def auth_user(response: Response, user_data: SUserAuth):
    check = await authenticate_user(email=user_data.email, password=user_data.password)
    if check is None:
        raise IncorrectEmailOrPasswordException

    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)

    return {'ok': True, 'access_token': access_token, 'refresh_token': None, 'message': 'Logged in successfully'}


@router.post("/logout/")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")

    return {'message': 'User logged out'}
