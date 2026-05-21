from fastapi import APIRouter, Depends, HTTPException, status
from app.interfaces.dependencies import get_enrollment_service, get_current_user
from app.application.services.enrollment_service import EnrollmentService

router = APIRouter(prefix="/inscripciones", tags=["Inscripciones"])


@router.post("/{curso_id}")
def inscribirse(
    curso_id: int,
    service: EnrollmentService = Depends(get_enrollment_service),
    usuario=Depends(get_current_user)
):
    try:
        service.enroll(usuario.id, curso_id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
    return {"mensaje": "Inscrito correctamente"}