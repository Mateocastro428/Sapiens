from fastapi import APIRouter, Form, Depends, HTTPException, status
from app.interfaces.dependencies import get_user_service, get_current_user
from app.application.services.user_service import UserService
from app.domain.models.user import User

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/registro")
def registrar(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    service: UserService = Depends(get_user_service)
):
    existing = service.repository.find_by_email(email)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El correo ya está registrado")

    service.register_user(username, email, password)
    return {"mensaje": "Usuario registrado"}


@router.post("/inicio-sesion")
def inicio_sesion(
    email: str = Form(...),
    password: str = Form(...),
    service: UserService = Depends(get_user_service)
):
    token = service.authenticate_user(email, password)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas")

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/perfil")
def perfil(usuario: User = Depends(get_current_user), service: UserService = Depends(get_user_service)):
    return service.profile(usuario)


@router.get("/")
def listar_usuarios(service: UserService = Depends(get_user_service)):
    return service.list_users()


@router.get("/{user_id}")
def obtener_usuario(user_id: int, service: UserService = Depends(get_user_service)):
    usuario = service.get_user_by_id(user_id)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario


@router.put("/{user_id}")
def actualizar_usuario(
    user_id: int,
    username: str = Form(...),
    service: UserService = Depends(get_user_service)
):
    usuario = service.update_username(user_id, username)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return {"mensaje": "Usuario actualizado"}


@router.delete("/{user_id}")
def eliminar_usuario(user_id: int, service: UserService = Depends(get_user_service)):
    resultado = service.delete_user(user_id)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado"}
