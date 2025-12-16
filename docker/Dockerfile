FROM python:3.10

WORKDIR /app

# Copier tout le projet dans l'image
COPY .. /app

# Installer les dépendances : le fichier est dans /app/docker/
RUN pip install --no-cache-dir -r docker/requirements.txt

CMD ["uvicorn", "api.fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]
