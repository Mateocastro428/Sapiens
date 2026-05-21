from abc import ABC, abstractmethod
from typing import Optional
from app.domain.models.user import User
from app.domain.ports.user_repository import UserRepository


class AuthStrategy(ABC):
    @abstractmethod
    def hash_password(self, plain_password: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def create_token(self, subject: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def authenticate(self, repository: UserRepository, email: str, password: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def get_current_user(self, repository: UserRepository, token: str) -> User:
        raise NotImplementedError
