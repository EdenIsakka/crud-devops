import sys
import os
import pytest
from sqlalchemy import text
from main import app, get_db

# Fixture para limpiar las tablas en Neon antes de cada test
@pytest.fixture(autouse=True, scope="function")
def clear_db():
    # Obtén una sesión usando la dependencia original (que usa Neon)
    db_gen = get_db()
    db = next(db_gen)
    try:
        # Ejecuta TRUNCATE en cada tabla relevante
        # Asegúrate de usar el nombre exacto de las tablas en la base de datos (por ejemplo, "doctors", "enfermeras", "pacientes")
        for table in ["doctors", "enfermeras", "pacientes"]:
            db.execute(text(f"TRUNCATE TABLE {table} RESTART IDENTITY CASCADE"))
        db.commit()
        yield  # Aquí se ejecuta el test con la base limpia
    finally:
        try:
            next(db_gen)
        except StopIteration:
            pass
