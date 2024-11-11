from fastapi import APIRouter

from database.models.user_model import UserModel
from .models.user_route_request_models import CreateUserInputModel

from .services.user_service import UserService

user_router = APIRouter(
    prefix="/user",
    tags=["user"],
)

user_service = UserService()


@user_router.post('/')
def create_user(user: CreateUserInputModel):
    res: UserModel = user_service.create_user(user)
    return res


@user_router.get("/")
def get_users():
    res = user_service.get_users()
    return res


@user_router.get("/{user_id}")
def get_user(user_id: int):
    res: UserModel = user_service.get_user(user_id)
    return res
