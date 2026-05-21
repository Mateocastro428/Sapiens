from typing import List, Optional
from app.domain.models.user import User
from app.domain.ports.user_repository import UserRepository
from app.infrastructure.auth.strategy import AuthStrategy


class UserService:
    def __init__(self, repository: UserRepository, auth_strategy: AuthStrategy):
        self.repository = repository
        self.auth_strategy = auth_strategy

    def register_user(self, username: str, email: str, password: str) -> User:
        password_hash = self.auth_strategy.hash_password(password)
        nuevo_usuario = User(username=username, email=email, password=password_hash)
        return self.repository.create(nuevo_usuario)

    def authenticate_user(self, email: str, password: str) -> Optional[str]:
        usuario = self.auth_strategy.authenticate(self.repository, email, password)
        if not usuario:
            return None
        return self.auth_strategy.create_token(usuario.email)

    def list_users(self) -> List[User]:
        return self.repository.list_all()

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.repository.find_by_id(user_id)

    def update_username(self, user_id: int, username: str) -> Optional[User]:
        return self.repository.update_username(user_id, username)

    def delete_user(self, user_id: int) -> bool:
        return self.repository.delete(user_id)

    def profile(self, user: User) -> dict:
        return {
            "mensaje": "Acceso autorizado",
            "usuario": user.username,
            "email": user.email
        }
