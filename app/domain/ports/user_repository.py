from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.user import User


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def update_username(self, user_id: int, username: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        raise NotImplementedError
