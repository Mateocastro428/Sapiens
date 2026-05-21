from sqlalchemy.orm import Session
from typing import List, Optional
from app.domain.models.course import Course
from app.domain.ports.course_repository import CourseRepository


class SqlAlchemyCourseRepository(CourseRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, course: Course) -> Course:
        self.db.add(course)
        self.db.commit()
        self.db.refresh(course)
        return course

    def find_by_id(self, course_id: int) -> Optional[Course]:
        return self.db.query(Course).filter(Course.id == course_id).first()

    def list_all(self) -> List[Course]:
        return self.db.query(Course).all()

    def update(self, course_id: int, title: str, description: str) -> Optional[Course]:
        curso = self.find_by_id(course_id)
        if curso is None:
            return None
        curso.title = title
        curso.description = description
        self.db.commit()
        self.db.refresh(curso)
        return curso

    def delete(self, course_id: int) -> bool:
        curso = self.find_by_id(course_id)
        if curso is None:
            return False
        self.db.delete(curso)
        self.db.commit()
        return True
