from typing import Optional
from fastapi import APIRouter, Request, Depends, Cookie, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import os

from app.application.page_service import get_index_context, get_page_context
from app.application.factories.service_factory import ServiceFactory
from app.infrastructure.database import get_db
from app.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", "..", ".."))
TEMPLATES_DIR = os.path.join(PROJECT_ROOT, "templates")

if not os.path.exists(TEMPLATES_DIR):
    raise Exception(f"No existe la carpeta templates en: {TEMPLATES_DIR}")

templates = Jinja2Templates(directory=TEMPLATES_DIR)

@router.get("/")
def index(request: Request):
    context = {"request": request}
    context.update(get_index_context())
    context.update(get_page_context("home"))
    return templates.TemplateResponse("index.html", context)

@router.get("/index.html")
def index_html(request: Request):
    context = {"request": request}
    context.update(get_index_context())
    context.update(get_page_context("home"))
    return templates.TemplateResponse("index.html", context)

@router.get("/metodologia")
def metodologia(request: Request):
    context = {"request": request}
    context.update(get_page_context("metodologia"))
    return templates.TemplateResponse("metodologia.html", context)

@router.get("/metodologia.html")
def metodologia_html(request: Request):
    context = {"request": request}
    context.update(get_page_context("metodologia"))
    return templates.TemplateResponse("metodologia.html", context)

@router.get("/registro")
def registro(request: Request):
    context = {"request": request}
    context.update(get_page_context("registro"))
    return templates.TemplateResponse("registro.html", context)

@router.get("/registro.html")
def registro_html(request: Request):
    context = {"request": request}
    context.update(get_page_context("registro"))
    return templates.TemplateResponse("registro.html", context)

@router.get("/eras")
def eras(request: Request):
    context = {"request": request}
    context.update(get_page_context("eras"))
    return templates.TemplateResponse("eras.html", context)

@router.get("/eras.html")
def eras_html(request: Request):
    context = {"request": request}
    context.update(get_page_context("eras"))
    return templates.TemplateResponse("eras.html", context)

@router.get("/progreso")
def progreso(
    request: Request,
    access_token: Optional[str] = Cookie(None),
    db=Depends(get_db)
):
    if not access_token:
        return RedirectResponse(url="/registro", status_code=status.HTTP_303_SEE_OTHER)

    repository = SqlAlchemyUserRepository(db)
    try:
        usuario = ServiceFactory.auth_strategy().get_current_user(repository, access_token)
    except HTTPException:
        return RedirectResponse(url="/registro?error=credenciales", status_code=status.HTTP_303_SEE_OTHER)

    context = {"request": request, "usuario": usuario}
    context.update(get_page_context("progreso"))
    return templates.TemplateResponse("progreso.html", context)

@router.get("/progreso.html")
def progreso_html(
    request: Request,
    access_token: Optional[str] = Cookie(None),
    db=Depends(get_db)
):
    if not access_token:
        return RedirectResponse(url="/registro", status_code=status.HTTP_303_SEE_OTHER)

    repository = SqlAlchemyUserRepository(db)
    try:
        usuario = ServiceFactory.auth_strategy().get_current_user(repository, access_token)
    except HTTPException:
        return RedirectResponse(url="/registro?error=credenciales", status_code=status.HTTP_303_SEE_OTHER)

    context = {"request": request, "usuario": usuario}
    context.update(get_page_context("progreso"))
    return templates.TemplateResponse("progreso.html", context)
