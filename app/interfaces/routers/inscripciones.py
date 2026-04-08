from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.domain.models.inscripcion import Inscripcion
from app.infrastructure.seguridad import obtener_usuario_actual

router = APIRouter(prefix="/inscripciones", tags=["Inscripciones"])


@router.post("/{curso_id}")
def inscribirse(
    curso_id: int,
    db: Session = Depends(get_db),
    usuario=Depends(obtener_usuario_actual)
):
    nueva = Inscripcion(
        usuario_id=usuario.id,
        curso_id=curso_id
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return {"mensaje": "Inscrito correctamente"}