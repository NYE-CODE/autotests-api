from pydantic import BaseModel, Field, ConfigDict
from typing import Any


class ValidationErrorSchema(BaseModel):
    """
    Описание структуры ошибки валидации.
    """
    model_config = ConfigDict(populate_by_name=True)

    type: str
    input: Any
    context: dict[str, Any] = Field(alias="ctx")
    message: str = Field(alias="msg")
    location: list[str] = Field(alias="loc")


class ValidationErrorResponseSchema(BaseModel):
    """
    Описание структуры ответа API с ошибками валидации.
    """
    model_config = ConfigDict(populate_by_name=True)

    details: list[ValidationErrorSchema] = Field(alias="detail")


class InternalErrorResponseSchema(BaseModel):
    """
    Описание структуры ответа API с внутренней ошибкой.
    """
    model_config = ConfigDict(populate_by_name=True)

    detail: str