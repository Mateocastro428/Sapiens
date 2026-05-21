from datetime import datetime, timedelta
from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.auth.jwt_strategy import JWTAuthStrategy, oauth2_scheme
from app.infrastructure.database import get_db
from app.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository


auth_strategy = JWTAuthStrategy()


def crear_token(data: dict):
    return auth_strategy.create_token(data.get("sub", ""))


def obtener_usuario_actual(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    repository = SqlAlchemyUserRepository(db)
    return auth_strategy.get_current_user(repository, token)
