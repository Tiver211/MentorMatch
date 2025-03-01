FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 443
CMD ["uvicorn", "api.main:app", "--port", "443", "--host=0.0.0.0", "--root-path", "/api", "--ssl-certfile", "/api/ssl/cert.pem", "--ssl-keyfile", "/api/ssl/privkey.pem"]