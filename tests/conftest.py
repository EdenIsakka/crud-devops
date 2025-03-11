import sys
import os
import pytest

# Agrega el directorio raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import models  # Se importa todo el módulo models
from database import SQLALCHEMY_DATABASE_URL
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(autouse=True, scope="function")
def clear_db():
    # Crea las tablas si no existen
    Base.metadata.create_all(bind=engine)

    connection = engine.connect()
    trans = connection.begin()
    session = TestingSessionLocal(bind=connection)

    try:
        # Elimina los datos de cada tabla
        session.query(models.Doctor).delete()
        session.query(models.Enfermera).delete()
        session.query(models.Paciente).delete()
        session.commit()
        yield
    finally:
        trans.rollback()
        connection.close()
