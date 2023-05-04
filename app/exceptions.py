from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Пользователь с таким email уже существует'


class IncorrectUserCredentials(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Неверные почта или пароль'


class TokenExpireException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Срок действия токена истек'


class TokenAbsentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Токен отсутствует'


class IncorrectTokenFormatException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Неверный формат токена'


class UserIsNotPresentException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED


class RoomCannotBeBooked(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Не осталось свободных номеров'
