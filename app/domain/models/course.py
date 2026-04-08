from sqlalchemy import Column, Integer, String, Text
from app.infrastructure.database import Base
from sqlalchemy.orm import relationship

lecciones = relationship("Leccion", backref="curso")  

class Course(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)