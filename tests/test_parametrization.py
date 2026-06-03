from urllib import request

import pytest

from _pytest.fixtures import SubRequest


@pytest.fixture(params=[
    "https://dev.env.com",
    "https://stag.env.com",
    "https://prod.env.com"
])
def host(request: SubRequest) -> str:
    return request.param

def test_host(host: str):
    print(f"Host: {host}")


class TestOperations:
    def test_user_with_operations(self):
        print("User with operations")

    def test_user_without_operations(self):
        print("User without operations")


users = {
    "+375331231212": "User with money on bank account",
    "+375331231213": "User without money on bank account",
    "+375331231214": "User without operations"
}

# @pytest.mark.parametrize(
#     "phone_number",
#     ["+375331231212", "+375331231213", "+375331231212"],
#     ids=[
#         "User with money on bank account",
#         "User without money on bank account",
#         "User without operations"
#     ]
# )

@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids= lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifiers(phone_number: str):
    pass