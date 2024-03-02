from typing import Union
from fastapi import FastAPI

#Creacion de una FastAPI
app = FastAPI()

#Esta son las rutas
@app.get("/")
def read_root():
    return {"Hello": "World!"}

@app.get("/Pinguino")
def Pinguino():
    return {"Pinwino:)" : "🐧"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/calculadora")
def calcular(OP_1: float , OP_2: float):
    return {"suma": OP_1 + OP_2}