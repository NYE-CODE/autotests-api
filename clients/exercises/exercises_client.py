from typing import TypedDict

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

from httpx import Response


class Exercise(TypedDict):
    """
    Описание структуры упражнения
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на получение списка упражнений.
    """
    exercises: list[Exercise]


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на получение упражнения.
    """
    exercises: Exercise


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на создание нового упражнения.
    """
    exercise: Exercise


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на обновление упражнения.
    """
    exercise: Exercise


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises.
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод для получения списка упражнений.
        :param query: Словарь с course_id.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id : str) -> Response:
        """
        Метод для получения упражнения.
        :param exercise_id : Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод для создания упражнения.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод для обновления упражнения.
        :param exercise_id: Индентификатор упражнения.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.
        :param exercise_id:
        :return:
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
