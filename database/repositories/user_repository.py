from typing import List

from ..db_engine import get_session
from ..models.user_model import UserModel


class UserRepository:
    def __init__(self):
        self.session = get_session()

    def save(self, user_input: dict) -> UserModel:
        user = UserModel(
            **user_input
        )
        with self.session as session:
            session.add(user)
            session.commit()
            return user

    def get_by_id(self, id: int) -> UserModel:
        user: UserModel = self.session.query(UserModel).filter_by(id=id).first()
        return user

    def get_all(self) -> List[UserModel]:
        users: List[UserModel] = self.session.query(UserModel).all()
        return users
