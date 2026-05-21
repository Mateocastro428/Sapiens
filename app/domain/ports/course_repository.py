from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.course import Course


class CourseRepository(ABC):
    @abstractmethod
    def create(self, course: Course) -> Course:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, course_id: int) -> Optional[Course]:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[Course]:
        raise NotImplementedError

    @abstractmethod
    def update(self, course_id: int, title: str, description: str) -> Optional[Course]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, course_id: int) -> bool:
        raise NotImplementedError
