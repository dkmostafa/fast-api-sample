from Exceptions.generic_exception import GenericException
from Exceptions.not_found_exception import NotFoundException
from database.models.user_model import UserModel
from database.repositories.user_repository import UserRepository
from ..models.user_route_request_models import CreateUserInputModel


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_user_by_id(self, user_id: int) -> UserModel:
        user: UserModel = self.user_repository.get_by_id(user_id)
        if user:
            return user
        else:
            raise GenericException('User does not exist')

    def create_user(self, user_input: CreateUserInputModel) -> UserModel:
        try:
            user: UserModel = self.user_repository.save(user_input.model_dump())
            return user
        except Exception as e:
            raise GenericException(str(e))

    def get_users(self) -> list[UserModel]:
        users: list[UserModel] = self.user_repository.get_all()
        return users

    def get_user(self, user_id: int) -> UserModel:
        user: UserModel = self.user_repository.get_by_id(user_id)
        if not user:
            raise NotFoundException('User does not exist')
        return user
