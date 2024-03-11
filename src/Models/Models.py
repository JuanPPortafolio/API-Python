from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String
from src.Config.DB import meta,engine

RAlimentos = Table("RAlimentos", meta, 
                   Column("id", Integer, primary_key=True), 
                   Column("Nombre", String(100)),
                   Column("Cedula",String(100)),
                   Column("Producto", String(100)),
                   Column("Cantidad", Integer),
                   Column("Precio", Integer))

meta.create_all(engine)