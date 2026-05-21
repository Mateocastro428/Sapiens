from sqlalchemy.orm import Session
from typing import List, Optional
from app.domain.models.user import User
from app.domain.ports.user_repository import UserRepository


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def find_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def find_by_id(self, user_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()

    def list_all(self) -> List[User]:
        return self.db.query(User).all()

    def update_username(self, user_id: int, username: str) -> Optional[User]:
        usuario = self.find_by_id(user_id)
        if usuario is None:
            return None
        usuario.username = username
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def delete(self, user_id: int) -> bool:
        usuario = self.find_by_id(user_id)
        if usuario is None:
            return False
        self.db.delete(usuario)
        self.db.commit()
        return True
