import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app  # Assure-toi que `app` est correctement importé
from app.models import Base

# URL de la base de données pour les tests (ici une base SQLite en local)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Configuration de la base de données pour les tests
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialisation de la base de données
def init_db():
    Base.metadata.create_all(bind=engine)

# Fixture pour initialiser la base de données avant les tests
@pytest.fixture(scope="module")
def setup_db():
    init_db()
    yield
    # Optionnel : nettoyer la base de données après les tests (si nécessaire)
    Base.metadata.drop_all(bind=engine)

# Fixture pour obtenir un client de test
@pytest.fixture
def client(setup_db):
    with TestClient(app) as client:
        yield client
