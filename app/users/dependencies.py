from datetime import datetime, timezone

from fastapi import Depends, Request
from jose import JWTError, jwt

from app.config import settings
from app.exceptions import (
    IncorrectTokenFormatException,
    TokenAbsentException,
    TokenExpiredException,
    UserNotExistsException,
)
from app.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise IncorrectTokenFormatException
    expire = payload.get('exp')
    if not expire:
        raise TokenExpiredException
    expire = datetime.fromtimestamp(expire, tz=timezone.utc)
    if expire < datetime.now(timezone.utc):
        raise TokenExpiredException
    user_id = int(payload.get('sub'))
    if not user_id:
        raise UserNotExistsException
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserNotExistsException

    return user
