from typing import Annotated

from typing import Union
from fastapi import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import mysql.connector
from pydantic import BaseModel

mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Alimentos"
)
cursor = mysql_conn.cursor()

class Alimento(BaseModel):
    id: int
    NombreYApellido: str
    Cedula: str
    Producto: str
    Cantidad: int
    Precio: float

#Creacion de una FastAPI
app = FastAPI()


#Esta son las rutas
@app.post("/Registro/")
async def CREATE(alimento: Alimento):
    query = "INSERT INTO RAlimentos (id_COMPRA, Nombre, Cedula, Producto, Cantidad, Precio) VALUES (%s,%s, %s, %s, %s, %s)"
    valores = (alimento.id,alimento.NombreYApellido,alimento.Cedula,alimento.Producto,alimento.Cantidad,alimento.Precio)
    cursor.execute(query, valores)
    mysql_conn.commit()
    return {"mensaje": "Registro creado"}

@app.get("/Registro/{id_COMPRA}")
async def SEARCH(id_alimento: int):
    query = "SELECT * FROM RAlimentos WHERE id_COMPRA = %s"
    cursor.execute(query, (id_alimento,))
    alimento = cursor.fetchone()
    if alimento:
        return {"id_COMPRA": alimento[0], "Nombre": alimento[1], "Cedula": alimento[2], "Producto": alimento[3], "Cantidad": alimento[4], "Precio": alimento[5]}
    else:
        raise HTTPException(status_code=404, detail="Compra no encontrado")

@app.put("/Registro/{id_COMPRA}")
async def UPDATE(id_alimento: int, alimento: Alimento):
    query = "UPDATE RAlimentos SET id_COMPRA = %s,Nombre = %s, Cedula = %s, Producto = %s, Cantidad = %s, Precio = %s WHERE id_COMPRA = %s"
    valores = (alimento.id,alimento.NombreYApellido, alimento.Cedula, alimento.Producto, alimento.Cantidad, alimento.Precio, id_alimento )
    cursor.execute(query, valores)
    mysql_conn.commit()
    return {"mensaje": "Detalles de la compra actualizados exitosamente"}

@app.delete("/Registro/{id_COMPRA}")
async def DELETE(id_alimento: int):
    query = "DELETE FROM RAlimentos WHERE id_COMPRA = %s"
    cursor.execute(query, (id_alimento,))
    mysql_conn.commit()
    return {"mensaje": "Compra borrada exitosamente"}
