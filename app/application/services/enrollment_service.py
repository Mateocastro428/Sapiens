from typing import Optional
from app.domain.models.inscripcion import Inscripcion
from app.domain.ports.enrollment_repository import EnrollmentRepository
from app.domain.ports.course_repository import CourseRepository


class EnrollmentService:
    def __init__(self, enrollment_repository: EnrollmentRepository, course_repository: CourseRepository):
        self.enrollment_repository = enrollment_repository
        self.course_repository = course_repository

    def enroll(self, usuario_id: int, curso_id: int) -> Inscripcion:
        if self.course_repository.find_by_id(curso_id) is None:
            raise ValueError("Curso no encontrado")

        existente = self.enrollment_repository.find_by_user_and_course(usuario_id, curso_id)
        if existente:
            return existente

        nueva_inscripcion = Inscripcion(usuario_id=usuario_id, curso_id=curso_id)
        return self.enrollment_repository.create(nueva_inscripcion)
