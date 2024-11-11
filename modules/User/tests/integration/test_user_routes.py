import pytest
from faker import Faker
from fastapi.testclient import TestClient
from database.db_engine import Base, get_session, engine
from database.models.user_model import UserModel
from database.repositories.user_repository import UserRepository
from ...models.user_response_models import CreateUserResponse

from ...user_routes import user_router


@pytest.fixture()
def session():

    Base.metadata.create_all(engine)
    try:
        with get_session() as session:
            yield session
    finally:
        Base.metadata.drop_all(engine)


@pytest.fixture()
def seeded_users_session(session):
    faker = Faker()

    user_repo = UserRepository()
    for i in range(1, 6):
        seeded_user = {
            "username": faker.user_name(),
            "name": faker.name()
        }
        user_repo.save(seeded_user)


user_client = TestClient(user_router)


def test_create_user_success(session):
    response = user_client.post("/user", json={
        "name": "test_user_creation",
        "username": "test_user_creation@gmail.com",
    })

    json_response = response.json()
    CreateUserResponse(**json_response)
    assert response.status_code == 200


def test_get_users(seeded_users_session):
    response = user_client.get("/user")
    json_response = response.json()
    assert response.status_code == 200
    assert len(json_response) > 1
    assert isinstance(json_response, list)


def test_get_user_by_id(seeded_users_session):
    response = user_client.get("/user/1")
    json_response = response.json()
    UserModel(**json_response)
    assert response.status_code == 200
