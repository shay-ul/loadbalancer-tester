FROM python:3.7-slim-buster

COPY app /app/
COPY requirements.txt /app/requirements.txt

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r app/requirements.txt

WORKDIR /app/
CMD ["python3", "main.py"]