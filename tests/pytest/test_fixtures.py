import pytest


@pytest.fixture(scope="session")
def settings():
    print("[SESSION] set settings")


@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс.")

@pytest.fixture(scope="function")
def user_client():
    print("[FUNCTION] create user client")

class TestUserFlow:
    def test_user_can_login(self, user, user_client):
        pass

    def test_user_can_create_course(self, user, user_client):
        pass


class TestAccountFlow:
    def test_user_account(self, user, user_client):
        pass