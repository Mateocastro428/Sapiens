from abc import ABC, abstractmethod
from typing import Optional
from app.domain.models.inscripcion import Inscripcion


class EnrollmentRepository(ABC):
    @abstractmethod
    def create(self, enrollment: Inscripcion) -> Inscripcion:
        raise NotImplementedError

    @abstractmethod
    def find_by_user_and_course(self, usuario_id: int, curso_id: int) -> Optional[Inscripcion]:
        raise NotImplementedError
