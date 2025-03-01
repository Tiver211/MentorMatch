FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 80
CMD ["uvicorn", "api.main:app", "--port", "80", "--host=0.0.0.0", "--root-path", "/api", "--ssl-certfile", "/ssl/cert.pem", "--ssl-keyfile", "/ssl/fullchain.pem"]