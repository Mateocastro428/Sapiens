from app.application.services.user_service import UserService
from app.application.services.course_service import CourseService
from app.application.services.enrollment_service import EnrollmentService
from app.infrastructure.auth.jwt_strategy import JWTAuthStrategy
from app.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository
from app.infrastructure.repositories.sqlalchemy_course_repository import SqlAlchemyCourseRepository
from app.infrastructure.repositories.sqlalchemy_inscripcion_repository import SqlAlchemyEnrollmentRepository


class ServiceFactory:
    @staticmethod
    def auth_strategy() -> JWTAuthStrategy:
        return JWTAuthStrategy()

    @staticmethod
    def user_service(db) -> UserService:
        user_repository = SqlAlchemyUserRepository(db)
        return UserService(user_repository, ServiceFactory.auth_strategy())

    @staticmethod
    def course_service(db) -> CourseService:
        course_repository = SqlAlchemyCourseRepository(db)
        return CourseService(course_repository)

    @staticmethod
    def enrollment_service(db) -> EnrollmentService:
        enrollment_repository = SqlAlchemyEnrollmentRepository(db)
        course_repository = SqlAlchemyCourseRepository(db)
        return EnrollmentService(enrollment_repository, course_repository)
