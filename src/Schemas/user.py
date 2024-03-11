from pydantic import BaseModel, Field
from typing import Optional

class Pedidos (BaseModel):
    id: Optional[str] = Field(None)
    Nombre: str
    Cedula: str
    Producto: str
    Cantidad: int
    Precio: int