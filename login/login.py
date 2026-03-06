from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

usuarios = []

@router.get("/registro", response_class=HTMLResponse)
def mostrar_formulario(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/registro")
def registrar_usuario(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):

    usuario = {
        "username": username,
        "email": email,
        "password": password
    }

    usuarios.append(usuario)

    return {"mensaje": "Usuario registrado", "usuario": usuario}