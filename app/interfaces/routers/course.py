from fastapi import APIRouter, Depends, Form, HTTPException, status
from app.interfaces.dependencies import get_course_service, get_current_user
from app.application.services.course_service import CourseService

router = APIRouter(prefix="/cursos", tags=["Cursos"])


# 🔹 CREAR CURSO
@router.post("/")
def crear_curso(
    title: str = Form(...),
    description: str = Form(...),
    service: CourseService = Depends(get_course_service),
    usuario=Depends(get_current_user)
):
    curso = service.create_course(title, description)
    return {"mensaje": "Curso creado", "curso": curso}


# 🔹 LISTAR CURSOS
@router.get("/")
def listar_cursos(
    service: CourseService = Depends(get_course_service),
    usuario=Depends(get_current_user)
):
    return service.list_courses()


# 🔹 OBTENER CURSO
@router.get("/{curso_id}")
def obtener_curso(
    curso_id: int,
    service: CourseService = Depends(get_course_service),
    usuario=Depends(get_current_user)
):
    curso = service.get_course(curso_id)
    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso no encontrado")
    return curso


# 🔹 ACTUALIZAR CURSO
@router.put("/{curso_id}")
def actualizar_curso(
    curso_id: int,
    title: str = Form(...),
    description: str = Form(...),
    service: CourseService = Depends(get_course_service),
    usuario=Depends(get_current_user)
):
    curso = service.update_course(curso_id, title, description)
    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso no encontrado")
    return {"mensaje": "Curso actualizado"}


# 🔹 ELIMINAR CURSO
@router.delete("/{curso_id}")
def eliminar_curso(
    curso_id: int,
    service: CourseService = Depends(get_course_service),
    usuario=Depends(get_current_user)
):
    eliminado = service.delete_course(curso_id)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso no encontrado")
    return {"mensaje": "Curso eliminado"}