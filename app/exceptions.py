from fastapi import status, HTTPException


class TokenExpiredException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")


class TokenNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token not found")


UserAlreadyExistsException = HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

PasswordMismatchException = HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Password mismatch")

IncorrectEmailOrPasswordException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                                  detail="Incorrect email or password")

NoJwtException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is not valid")

NoUserIdException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User with this id not not found")

ForbiddenException = HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                   detail="You do not have permission to perform this action")
