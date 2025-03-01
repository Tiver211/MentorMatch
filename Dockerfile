FROM python:3.11-slim

WORKDIR /app

RUN apt-get update \
   && apt-get install -y --no-install-recommends gcc libpq-dev \
   && apt-get clean \
   && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip --no-cache-dir install -r requirements.txt

COPY . /app

EXPOSE 80
CMD ["uvicorn", "api.main:app", "--port", "80", "--host=0.0.0.0", "--root-path", "/api"]