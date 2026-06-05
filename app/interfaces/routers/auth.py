from fastapi import APIRouter, Form, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from app.interfaces.dependencies import get_user_service
from app.application.services.user_service import UserService
from app.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository

router = APIRouter()


@router.post("/registro")
def registrar_usuario(
    nombre: str = Form(...),
    apellido: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    nivel: str = Form(None),
    terminos: str = Form(None),
    service: UserService = Depends(get_user_service)
):
    existing = service.repository.find_by_email(email)
    if existing:
        return RedirectResponse(url="/registro?error=correo_existe", status_code=status.HTTP_303_SEE_OTHER)
    username = f"{nombre} {apellido}".strip()
    if len(password or "") < 8:
        return RedirectResponse(url="/registro?error=pass_corta", status_code=status.HTTP_303_SEE_OTHER)

    username = f"{nombre} {apellido}".strip()
    service.register_user(username=username, email=email, password=password)
    token = service.authenticate_user(email, password)
    if not token:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="No se pudo generar token")

    response = RedirectResponse(url="/progreso", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie("access_token", token, httponly=True, samesite="lax")
    return response


@router.post("/login")
def iniciar_sesion(
    email: str = Form(...),
    password: str = Form(...),
    service: UserService = Depends(get_user_service)
):
    token = service.authenticate_user(email, password)
    if not token:
        return RedirectResponse(url="/registro?error=credenciales", status_code=status.HTTP_303_SEE_OTHER)

    response = RedirectResponse(url="/progreso", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie("access_token", token, httponly=True, samesite="lax")
    return response


@router.post("/logout")
def cerrar_sesion():
    response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie("access_token")
    return response
