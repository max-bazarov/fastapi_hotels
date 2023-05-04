from datetime import datetime

from fastapi import Depends, Request
from jose import JWTError, jwt

from app.config import settings
from app.exceptions import (
    IncorrectTokenFormatException,
    TokenAbsentException,
    TokenExpireException,
    UserIsNotPresentException,
)
from app.users.service import UserService


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_HASH_KEY, settings.HASH_ALGORYTHM
        )
    except JWTError:
        raise IncorrectTokenFormatException

    expire: str = payload.get('exp')
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpireException

    user_id: str = payload.get('sub')
    if not user_id:
        raise UserIsNotPresentException
    user = await UserService.get_object_or_none(int(user_id))
    if not user:
        raise UserIsNotPresentException

    return user


# async def get_current_admin_user(current_user: Users = Depends(get_current_user)):
#     if current_user.role != 'admin':
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
#     return current_user
