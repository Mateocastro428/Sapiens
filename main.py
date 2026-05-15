from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from app.interfaces.routers.usuarios import router as usuarios_router
from app.interfaces.routers.course import router as cursos_router
from app.interfaces.routers.lecciones import router as lecciones_router
from app.interfaces.routers.inscripciones import router as inscripciones_router
from app.application.page_service import get_index_context, get_page_context

from app.infrastructure.database import Base, engine

app = FastAPI(title="Sapiens API")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(BASE_DIR, "static")
templates_dir = os.path.join(BASE_DIR, "templates")

if not os.path.exists(static_dir):
    raise Exception(f"No existe la carpeta static en: {static_dir}")

if not os.path.exists(templates_dir):
    raise Exception(f"No existe la carpeta templates en: {templates_dir}")

# Montar toda la carpeta static en /static (para CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

templates = Jinja2Templates(directory=templates_dir)

@app.get("/")
def index(request: Request):
    context = {"request": request}
    context.update(get_index_context())
    context.update(get_page_context("home"))
    return templates.TemplateResponse("index.html", context)

@app.get("/index.html")
def index_html(request: Request):
    context = {"request": request}
    context.update(get_index_context())
    context.update(get_page_context("home"))
    return templates.TemplateResponse("index.html", context)

@app.get("/metodologia")
def metodologia(request: Request):
    context = {"request": request}
    context.update(get_page_context("metodologia"))
    return templates.TemplateResponse("metodologia.html", context)

@app.get("/metodologia.html")
def metodologia_html(request: Request):
    context = {"request": request}
    context.update(get_page_context("metodologia"))
    return templates.TemplateResponse("metodologia.html", context)

@app.get("/registro")
def registro(request: Request):
    context = {"request": request}
    context.update(get_page_context("registro"))
    return templates.TemplateResponse("registro.html", context)

@app.get("/registro.html")
def registro_html(request: Request):
    context = {"request": request}
    context.update(get_page_context("registro"))
    return templates.TemplateResponse("registro.html", context)

@app.get("/eras")
def eras(request: Request):
    context = {"request": request}
    context.update(get_page_context("eras"))
    return templates.TemplateResponse("eras.html", context)

@app.get("/eras.html")
def eras_html(request: Request):
    context = {"request": request}
    context.update(get_page_context("eras"))
    return templates.TemplateResponse("eras.html", context)

@app.get("/progreso")
def progreso(request: Request):
    context = {"request": request}
    context.update(get_page_context("progreso"))
    return templates.TemplateResponse("progreso.html", context)

@app.get("/progreso.html")
def progreso_html(request: Request):
    context = {"request": request}
    context.update(get_page_context("progreso"))
    return templates.TemplateResponse("progreso.html", context)

@app.get("/acerca")
def acerca(request: Request):
    context = {"request": request}
    context.update(get_page_context("acerca"))
    return templates.TemplateResponse("acerca.html", context)

@app.get("/acerca.html")
def acerca_html(request: Request):
    context = {"request": request}
    context.update(get_page_context("acerca"))
    return templates.TemplateResponse("acerca.html", context)

@app.get("/api")
def api_status():
    return {"mensaje": "Sapiens API funcionando 🚀"}


app.include_router(cursos_router)
app.include_router(lecciones_router)
app.include_router(inscripciones_router)
app.include_router(usuarios_router)


Base.metadata.create_all(bind=engine)