from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from app.domain.schemas.user import UsuarioCreate

router = APIRouter(tags=["Usuarios"])

templates = Jinja2Templates(directory="templates")

usuarios = []

@router.get("/registro", response_class=HTMLResponse)
def formulario(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/registro")
def registrar(username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    user_data = UsuarioCreate(
        username=username,
        email=email,
        password=password
    )
    usuarios.append(user_data)
    return {"mensaje": "Usuario registrado", "usuario": user_data}