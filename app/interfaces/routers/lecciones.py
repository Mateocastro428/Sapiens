from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.domain.models.leccion import Leccion

router = APIRouter(prefix="/lecciones", tags=["Lecciones"])


@router.post("/")
def crear_leccion(titulo: str, contenido: str, curso_id: int, db: Session = Depends(get_db)):
    nueva = Leccion(
        titulo=titulo,
        contenido=contenido,
        curso_id=curso_id
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return {"mensaje": "Lección creada"}


@router.get("/curso/{curso_id}")
def ver_lecciones(curso_id: int, db: Session = Depends(get_db)):
    return db.query(Leccion).filter(Leccion.curso_id == curso_id).all()