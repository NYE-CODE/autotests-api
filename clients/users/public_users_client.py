from typing import TypedDict

from clients.api_client import APIClient

from httpx import Response


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание нового пользователя.
    """
    email: str
    password: str
    firstName: str
    lastName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    API-клиент для публичной работы пользователя.
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод создает пользователя.

        :param request: словарь с email, password, firstName, lastName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/users', json=request)
