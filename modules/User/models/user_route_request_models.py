from pydantic import BaseModel


class CreateUserInputModel(BaseModel):
    username: str
    name: str
