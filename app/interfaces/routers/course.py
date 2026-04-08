from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.domain.models.course import Course
from app.infrastructure.seguridad import obtener_usuario_actual

router = APIRouter(prefix="/cursos", tags=["Cursos"])


# 🔹 CREAR CURSO
@router.post("/")
def crear_curso(
    title: str = Form(...),
    description: str = Form(...),
    db: Session = Depends(get_db),
    usuario=Depends(obtener_usuario_actual)  # 🔐 protegido
):
    nuevo_curso = Course(
        title=title,
        description=description
    )

    db.add(nuevo_curso)
    db.commit()
    db.refresh(nuevo_curso)

    return {"mensaje": "Curso creado", "curso": nuevo_curso}


# 🔹 LISTAR CURSOS
@router.get("/")
def listar_cursos(
    db: Session = Depends(get_db),
    usuario=Depends(obtener_usuario_actual)
):
    return db.query(Course).all()


# 🔹 OBTENER CURSO
@router.get("/{curso_id}")
def obtener_curso(
    curso_id: int,
    db: Session = Depends(get_db),
    usuario=Depends(obtener_usuario_actual)
):
    curso = db.query(Course).filter(Course.id == curso_id).first()

    if not curso:
        return {"error": "Curso no encontrado"}

    return curso


# 🔹 ACTUALIZAR CURSO
@router.put("/{curso_id}")
def actualizar_curso(
    curso_id: int,
    title: str = Form(...),
    description: str = Form(...),
    db: Session = Depends(get_db),
    usuario=Depends(obtener_usuario_actual)
):
    curso = db.query(Course).filter(Course.id == curso_id).first()

    if not curso:
        return {"error": "Curso no encontrado"}

    curso.title = title
    curso.description = description

    db.commit()

    return {"mensaje": "Curso actualizado"}


# 🔹 ELIMINAR CURSO
@router.delete("/{curso_id}")
def eliminar_curso(
    curso_id: int,
    db: Session = Depends(get_db),
    usuario=Depends(obtener_usuario_actual)
):
    curso = db.query(Course).filter(Course.id == curso_id).first()

    if not curso:
        return {"error": "Curso no encontrado"}

    db.delete(curso)
    db.commit()

    return {"mensaje": "Curso eliminado"}