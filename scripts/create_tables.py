import os
import sys
import glob
import importlib.util
from sqlalchemy import inspect

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from app.infrastructure.database import Base, engine

MODELS_DIR = os.path.join(ROOT_DIR, "app", "domain", "models")
MODELS_DIR = os.path.normpath(MODELS_DIR)

def import_model_file(path):
    name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(f"models.{name}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    pattern = os.path.join(MODELS_DIR, "*.py")
    files = [p for p in glob.glob(pattern) if not p.endswith("__init__.py")]
    for f in files:
        import_model_file(f)
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Tablas en la base de datos:")
    for t in tables:
        print("- ", t)

if __name__ == "__main__":
    main()
