# Sapiens

## Descripción

Sapiens es una aplicación web construida con FastAPI que incluye rutas de API, manejo de páginas estáticas, autenticación y persistencia en base de datos.

## Requisitos

- Python 3.11.x
- pip
- Git
- SQLite local o una base de datos compatible con `DATABASE_URL` (PostgreSQL recomendado para producción)

## Instalación del entorno virtual

Ejecuta los siguientes pasos desde la raíz del proyecto:

```bash
cd /workspaces/Sapiens
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```



## Configuración de variables de entorno locales

La aplicación puede usar `DATABASE_URL` para conectarse a la base de datos. Si no está definida, usará SQLite local en `./sapiens.db`.

Crea un archivo `.env` en la raíz del proyecto con las variables que necesitas:

```env
PORT=8000
DATABASE_URL=sqlite:///./sapiens.db
# Ejemplo PostgreSQL:
# DATABASE_URL=postgresql+psycopg://user:password@host:port/dbname
```

La app lee `DATABASE_URL` desde el entorno a través de `app/infrastructure/database.py`.




## Ejecutar la aplicación localmente

### Opción 1: Usar `startup.sh` con Gunicorn

```bash
bash startup.sh
```

### Opción 2: Usar Uvicorn en modo desarrollo

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Comprobar que la app está viva

Abre en el navegador o usa `curl`:

```bash
curl http://127.0.0.1:8000/api
```

Deberías recibir una respuesta JSON como:

```json
{"mensaje": "Sapiens API funcionando "}
```

## Ejecutar pruebas

Con el entorno virtual activado, ejecuta:

```bash
pytest -q
```

### Si quieres ejecutar tests específicos

```bash
pytest -q tests/test_services_repositories.py
```

## Flujo CI/CD

El repositorio ya incluye un workflow de GitHub Actions en `.github/workflows/main_sapiens-api-mateocastro.yml`.

- Se ejecuta en `push` y `pull_request` sobre `main`.
- Instala dependencias y corre `pytest -q`.
- El despliegue solo se ejecuta si el job de tests pasa correctamente.

## Despliegue en Railway

Esta aplicación FastAPI puede desplegarse directamente en Railway usando el `Procfile` o el `Dockerfile` incluidos.

### Opciones de despliegue

1. `Procfile`: usa el script de inicio existente `startup.sh`.
2. `Dockerfile`: crea una imagen basada en Python 3.11 y ejecuta el mismo comando.

### Pasos rápidos

- Conecta el repositorio en Railway.
- Asegúrate de que Railway use `PORT` y monte la aplicación desde la raíz del proyecto.
- Si usas addon de base de datos, define `DATABASE_URL` en Railway.

### Notas importantes

- Por defecto la app usa SQLite (`sqlite:///./sapiens.db`) si `DATABASE_URL` no está configurada.
- Para un entorno de producción real en Railway, es recomendable usar PostgreSQL y configurar `DATABASE_URL` con la cadena de conexión del addon.

### enlace
sapiens-production-a996.up.railway.app
