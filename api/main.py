from fastapi import FastAPI
import uvicorn
import os
from api.database import init_db

app = FastAPI()

@app.on_event("startup")
def start():
    init_db()

if __name__ == "__main__":
    server_address = os.getenv("SERVER_ADDRESS", "0.0.0.0:8080")
    host, port = server_address.split(":")
    uvicorn.run(app, host=host, port=int(port))