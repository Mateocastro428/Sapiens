from fastapi import APIRouter, HTTPException
from app.models.contenido import Contenido
from typing import List, Optional

router = APIRouter(prefix="/contenidos", tags=["Contenidos"])

contenidos = []

# GET todos
@router.get("/", response_model=List[Contenido])
def obtener():
    return contenidos

# POST crear
@router.post("/", response_model=Contenido)
def crear(contenido: Contenido):
    contenidos.append(contenido.dict())
    return contenido

# GET por ID
@router.get("/{id}", response_model=Contenido)
def obtener_id(id: int):
    for c in contenidos:
        if c["id"] == id:
            return c

    raise HTTPException(status_code=404, detail="No encontrado")

# FILTRO
@router.get("/buscar/", response_model=List[Contenido])
def filtrar(tipo: Optional[str] = None):

    if tipo is None:
        return contenidos

    return [c for c in contenidos if c["tipo"] == tipo]