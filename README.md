FastAPI Items API
Une API REST simple construite avec FastAPI pour gérer des items.

Fonctionnalités
Créer un item

Lire tous les items

Lire un item spécifique

Mettre à jour un item

Supprimer un item

Tests unitaires avec pytest

Analyse de qualité du code avec flake8

Déploiement automatique via Render et GitHub Actions

Technologies utilisées
Python 3.11+

FastAPI

Uvicorn (serveur ASGI pour lancer l'application)

Pytest (tests unitaires)

Flake8 (analyse de code)

GitHub Actions (CI/CD)

Render (déploiement automatique)

Installation locale
Cloner le projet :
git clone https://github.com/abraham261/fastapi-items-api.git
cd fastapi-items-api
Créer un environnement virtuel :
python -m venv venv

venv\Scripts\activate     # Sur Windows

Installer les dépendances :
pip install -r requirements.txt
Lancer le serveur FastAPI :
uvicorn app.main:app --reload

Accéder à la documentation automatique :
Swagger UI : http://127.0.0.1:8000/docs
Redoc : http://127.0.0.1:8000/redoc

Lancer les tests
Pour exécuter tous les tests unitaires :
pytest

Analyser la qualité du code
Pour analyser le code avec flake8 :
flake8 .

Déploiement avec Render
Un fichier render.yaml est configuré pour un déploiement automatique.

À chaque push sur GitHub, Render détectera les changements et déploiera la nouvelle version.

CI/CD avec GitHub Actions
Le fichier .github/workflows/ci.yml est configuré pour :

Lancer les tests unitaires

Vérifier la qualité du code (flake8) à chaque push ou pull request

Auteur
Abraham261











