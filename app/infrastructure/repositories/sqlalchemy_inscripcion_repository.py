from sqlalchemy.orm import Session
from typing import Optional
from app.domain.models.inscripcion import Inscripcion
from app.domain.ports.enrollment_repository import EnrollmentRepository


class SqlAlchemyEnrollmentRepository(EnrollmentRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, enrollment: Inscripcion) -> Inscripcion:
        self.db.add(enrollment)
        self.db.commit()
        self.db.refresh(enrollment)
        return enrollment

    def find_by_user_and_course(self, usuario_id: int, curso_id: int) -> Optional[Inscripcion]:
        return self.db.query(Inscripcion).filter(
            Inscripcion.usuario_id == usuario_id,
            Inscripcion.curso_id == curso_id
        ).first()
