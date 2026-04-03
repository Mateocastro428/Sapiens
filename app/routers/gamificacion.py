from fastapi import APIRouter
from app.models.gamificacion import Logro, Nivel

router = APIRouter(prefix="/gamificacion", tags=["Gamificación"])
logros = []
niveles = [
    {"nivel": 1, "nombre": "Principiante", "puntos_minimos": 0},
    {"nivel": 2, "nombre": "Estudiante", "puntos_minimos": 50},
    {"nivel": 3, "nombre": "Historiador", "puntos_minimos": 100}
]

@router.get("/Niveles")
def obtener_niveles():
    return niveles

@router.post("/logros")
def crear_logro(logro: Logro):
    logros.append(logro.dict())
    return {"mensaje": "Logro creado", "data": Logro}

@router.get("/logros")
def listar_logros():
    return logros