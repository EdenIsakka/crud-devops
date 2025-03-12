
import sys
import os

# Agregar el directorio raíz al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from sqlalchemy.sql import text  # <-- Asegúrate de importar esto
from main import app, get_db

@pytest.fixture(autouse=True, scope="function")
def clear_db():
    db_gen = get_db()
    db = next(db_gen)
    try:
        for table in ["doctors", "enfermeras", "pacientes"]:
            db.execute(text(f"TRUNCATE TABLE {table} RESTART IDENTITY CASCADE"))
        db.commit()
        yield
    finally:
        try:
            next(db_gen)
        except StopIteration:
            pass
