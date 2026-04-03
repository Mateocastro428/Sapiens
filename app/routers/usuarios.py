from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from app.models.usuario import Usuario

router = APIRouter(tags=["Usuarios"])

templates = Jinja2Templates(directory="templates")

usuarios = []

@router.get("/registro", response_class=HTMLResponse)
def formulario(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/registro")
def registrar(username: str = Form(...), email: str = Form(...), password: str = Form(...)):

    usuario = Usuario(
        id=len(usuarios)+1,
        username=username,
        email=email,
        password=password
    )

    usuarios.append(usuario.dict())

    return {"mensaje": "Usuario registrado", "usuario": usuario}