import pytest
from faker import Faker
from unittest.mock import MagicMock

from Exceptions.not_found_exception import NotFoundException
from database.models.user_model import UserModel
from modules.User.services.user_service import UserService

faker = Faker()


@pytest.fixture
def user_service():
    mock_user_repository = MagicMock()
    mock_user_repository.get_by_id.return_value = UserModel(
        name=faker.name(),
        username=faker.user_name()
    )

    user_service = UserService()
    user_service.user_repository = mock_user_repository

    return user_service


def test_get_user_success(user_service):
    response = user_service.get_user(1)
    assert isinstance(response, UserModel)


def test_get_user_not_found():
    mock_user_repository = MagicMock()
    mock_user_repository.get_by_id.return_value = None
    user_service = UserService()
    user_service.user_repository = mock_user_repository

    with pytest.raises(NotFoundException) as excinfo:
        user_service.get_user(1)
    assert str(excinfo.value) == 'User does not exist'
