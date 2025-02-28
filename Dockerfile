FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 80
CMD ["uvicorn", "api.main:app", "--port", "80", "--host=0.0.0.0", "--root-path", "/api"]