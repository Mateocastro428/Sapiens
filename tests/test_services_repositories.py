import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.infrastructure.database import Base
from app.domain.models.user import User
from app.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository
from app.infrastructure.repositories.sqlalchemy_course_repository import SqlAlchemyCourseRepository
from app.infrastructure.repositories.sqlalchemy_inscripcion_repository import SqlAlchemyEnrollmentRepository
from app.infrastructure.auth.jwt_strategy import JWTAuthStrategy
from app.application.services.user_service import UserService
from app.application.services.course_service import CourseService
from app.application.services.enrollment_service import EnrollmentService


engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
SessionTest = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


@pytest.fixture()
def session():
    db = SessionTest()
    try:
        yield db
    finally:
        db.close()


def test_user_repository_and_service(session):
    user_repository = SqlAlchemyUserRepository(session)
    auth_strategy = JWTAuthStrategy()
    user_service = UserService(user_repository, auth_strategy)

    usuario = user_service.register_user("maria", "maria@example.com", "1234")
    assert usuario.id is not None
    assert usuario.email == "maria@example.com"

    token = user_service.authenticate_user("maria@example.com", "1234")
    assert token is not None

    current_user = auth_strategy.get_current_user(user_repository, token)
    assert current_user.email == "maria@example.com"

    fetched = user_service.get_user_by_id(usuario.id)
    assert fetched.username == "maria"

    actualizado = user_service.update_username(usuario.id, "mariana")
    assert actualizado.username == "mariana"

    usuarios = user_service.list_users()
    assert len(usuarios) == 1

    eliminado = user_service.delete_user(usuario.id)
    assert eliminado is True
    assert user_service.get_user_by_id(usuario.id) is None


def test_course_and_enrollment_service(session):
    course_repository = SqlAlchemyCourseRepository(session)
    enrollment_repository = SqlAlchemyEnrollmentRepository(session)
    course_service = CourseService(course_repository)
    enrollment_service = EnrollmentService(enrollment_repository, course_repository)

    curso = course_service.create_course("Matemáticas", "Curso básico de matemáticas")
    assert curso.id is not None

    curso_obtenido = course_service.get_course(curso.id)
    assert curso_obtenido.title == "Matemáticas"

    cursos = course_service.list_courses()
    assert len(cursos) == 1

    user_repository = SqlAlchemyUserRepository(session)
    user_repository.create(User(username="alumno", email="alumno@example.com", password="hash"))

    inscripcion = enrollment_service.enroll(usuario_id=1, curso_id=curso.id)
    assert inscripcion.usuario_id == 1
    assert inscripcion.curso_id == curso.id

    con_reinscripcion = enrollment_service.enroll(usuario_id=1, curso_id=curso.id)
    assert con_reinscripcion.id == inscripcion.id

    actualizado = course_service.update_course(curso.id, "Matemáticas Avanzadas", "Contenido actualizado")
    assert actualizado.title == "Matemáticas Avanzadas"

    eliminado = course_service.delete_course(curso.id)
    assert eliminado is True

    with pytest.raises(ValueError):
        enrollment_service.enroll(usuario_id=1, curso_id=999)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
