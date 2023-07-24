# On part de l'image python:3.9-slim
FROM python:3.9-slim

# On se place dans ce dossier dans le conteneur
WORKDIR /usr/src/app

# On copie le fichier index.html
COPY index.html .

CMD ["python", "-m", "http.server", "8000"]