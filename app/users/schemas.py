from pydantic import BaseModel, EmailStr, Field


class SUserRegister(BaseModel):
    email: EmailStr = Field(..., description="Email address")
    password: str = Field(..., min_length=5, max_length=50, description="Password 5 to 50 characters")
    password_check: str = Field(..., min_length=5, max_length=50, description="Password 5 to 50 characters")
    name: str = Field(..., min_length=3, max_length=50, description="User name 3 to 50 characters")


class SUserAuth(BaseModel):
    email: EmailStr = Field(..., description="Email address")
    password: str = Field(..., min_length=5, max_length=50, description="Password 5 to 50 characters")


class SUserRead(BaseModel):
    id: int = Field(..., description="User id")
    name: str = Field(..., min_length=3, max_length=50, description="Name 3 to 50 characters")