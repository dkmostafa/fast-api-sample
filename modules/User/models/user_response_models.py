from dataclasses import dataclass


@dataclass
class CreateUserResponse:
    id: int
    username: str
    name: str
