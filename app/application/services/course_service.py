from typing import List, Optional
from app.domain.models.course import Course
from app.domain.ports.course_repository import CourseRepository


class CourseService:
    def __init__(self, repository: CourseRepository):
        self.repository = repository

    def create_course(self, title: str, description: str) -> Course:
        nuevo_curso = Course(title=title, description=description)
        return self.repository.create(nuevo_curso)

    def list_courses(self) -> List[Course]:
        return self.repository.list_all()

    def get_course(self, course_id: int) -> Optional[Course]:
        return self.repository.find_by_id(course_id)

    def update_course(self, course_id: int, title: str, description: str) -> Optional[Course]:
        return self.repository.update(course_id, title, description)

    def delete_course(self, course_id: int) -> bool:
        return self.repository.delete(course_id)
