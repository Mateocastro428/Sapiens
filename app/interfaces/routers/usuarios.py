from fastapi import APIRouter, Form, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.domain.models.user import User
from app.application.user_service import login_usuario
from passlib.context import CryptContext
from app.infrastructure.seguridad import crear_token, obtener_usuario_actual

ph = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


# 🔹 REGISTRO
@router.post("/registro")
def registrar(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    password_hash = ph.hash(password)

    nuevo_usuario = User(
        username=username,
        email=email,
        password=password_hash
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return {"mensaje": "Usuario registrado"}


# 🔹 LOGIN
@router.post("/inicio-sesion")
def inicio_sesion(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    usuario = login_usuario(db, email, password)

    if not usuario:
        return {"error": "Credenciales incorrectas"}

    token = crear_token({
        "sub": usuario.email
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# 🔹 RUTA PROTEGIDA
@router.get("/perfil")
def perfil(usuario=Depends(obtener_usuario_actual)):
    return {
        "mensaje": "Acceso autorizado",
        "usuario": usuario.username,
        "email": usuario.email
    }