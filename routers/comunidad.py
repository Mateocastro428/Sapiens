from fastapi import APIRouter
from models.comunidad import Amistad, Mensaje

router = APIRouter(prefix="/comunidad", tags=["Comunidad"])

amistades = []
mensajes = []

@router.post("/amigos")
def agregar_amigo(amistad: Amistad):
    amistades.append(amistad.dict())
    return {"mensaje": "Amigo agregado", "data": amistad}

@router.get("/amigos")
def listar_amigos():
    return amistades

@router.post("/mensajes")
def enviar_mensaje(mensaje: Mensaje):
    mensajes.append(mensaje.dict())
    return {"mensaje": "Mensaje enviado", "data": mensaje}

@router.get("/mensajes")
def listar_mensajes():
    return mensajes