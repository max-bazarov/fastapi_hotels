from fastapi import APIRouter, Depends, Response

from app.exceptions import IncorrectUserCredentials, UserAlreadyExistsException
from app.users.auth import (
    authenticate_user,
    create_access_token,
    get_password_hash,
)
from app.users.dependencies import get_current_user
from app.users.models import User
from app.users.schemas import UserAuthSchema
from app.users.service import UserService

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/register')
async def register_user(user_data: UserAuthSchema):
    existing_user = await UserService.get_object_or_none(email=user_data.email)

    if existing_user:
        raise UserAlreadyExistsException

    hashed_password = get_password_hash(user_data.password)
    await UserService.create(
        email=user_data.email, hashed_password=hashed_password
    )


@router.post('/login')
async def login_user(response: Response, user_data: UserAuthSchema):
    user = await authenticate_user(user_data.email, user_data.password)
    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie('booking_access_token', access_token, httponly=True)
    return {'access_token': access_token}


@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('booking_access_token')


@router.get('/me')
async def get_user_me(current_user: User = Depends(get_current_user)):
    return current_user


# @router.get('/all')
# async def get_all_users(current_user: Users = Depends(get_current_admin_user)):
#     return await UserService.get_all()
