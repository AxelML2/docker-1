FROM python:3.9-slim

WORKDIR /opt/demo/
COPY . .

RUN pip install -r requirements.txt & pip3 install requests


ENTRYPOINT python app.py