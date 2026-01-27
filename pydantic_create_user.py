from typing import Annotated

from pydantic import BaseModel, EmailStr, Field


Password = Annotated[str, Field(min_length=8)]  # Enforces minimum password length validation


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса создания пользователя.
    """
    email: EmailStr
    password: Password
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema
