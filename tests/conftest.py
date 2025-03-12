import sys
import os
import pytest
from sqlalchemy import text
from main import app, get_db

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
