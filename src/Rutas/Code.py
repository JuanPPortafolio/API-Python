from fastapi import APIRouter
from src.Config.DB import conn
from src.Models.Models import RAlimentos
from src.Schemas.user import Pedidos

#Creacion de una FastAPI
data = APIRouter()

@data.get("/Pedido")
def get_PEDIDOS():
    return conn.execute(RAlimentos.select()).fetchall()

@data.post("/Pedido")
def set_PEDIDO(pedido : Pedidos):
        new_pedido = {"Nombre": pedido.Nombre, "Cedula": pedido.Cedula,"Producto": pedido.Producto,"Cantidad": pedido.Cantidad,"Precio": pedido.Precio}
        result = conn.execute(RAlimentos.insert().values(new_pedido))
        conn.commit()
        print(result.lastrowid)
        return conn.execute(RAlimentos.select().where(RAlimentos.c.id == result.lastrowid)).first
       
    
@data.get("/Pedido/{id}")
def get_PEDIDO(id: str):
    conn.execute(RAlimentos.select().where(RAlimentos.c.id == id)).first()