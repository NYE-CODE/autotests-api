from pydantic import BaseModel, Field, ConfigDict, EmailStr
from tools.fakers import fake

class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание нового пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(alias="password", default_factory=fake.password)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.first_name)


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя.
    """
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя.
    """
    email: EmailStr | None = Field(default_factory=fake.email)
    lastName: str | None = Field(default_factory=fake.last_name)
    firstName: str | None = Field(default_factory=fake.first_name)
    middleName: str | None = Field(default_factory=fake.first_name)


class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа на обновление пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя.
    """
    user: UserSchema