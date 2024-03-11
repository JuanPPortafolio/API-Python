from fastapi import FastAPI
from src.Rutas.Code import data

app = FastAPI()

app.include_router(data)