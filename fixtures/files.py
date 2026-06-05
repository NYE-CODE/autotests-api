import pytest
from pydantic import BaseModel

from clients.files.file_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.files.files_client import get_files_client, FilesClient
from fixtures.users import UserFixture


class FileFixture(BaseModel):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema


@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_files_client(function_user.authentication_user)


@pytest.fixture
def function_file(files_client: FilesClient):
    request = CreateFileRequestSchema("./testdata/files/image.png")
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)
