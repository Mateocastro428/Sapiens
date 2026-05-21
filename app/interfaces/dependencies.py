from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.application.factories.service_factory import ServiceFactory
from app.infrastructure.auth.jwt_strategy import oauth2_scheme
from app.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository


def get_user_service(db: Session = Depends(get_db)):
    return ServiceFactory.user_service(db)


def get_course_service(db: Session = Depends(get_db)):
    return ServiceFactory.course_service(db)


def get_enrollment_service(db: Session = Depends(get_db)):
    return ServiceFactory.enrollment_service(db)


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    repository = SqlAlchemyUserRepository(db)
    return ServiceFactory.auth_strategy().get_current_user(repository, token)
