from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

#MODELO DEL MENSAJE
class Mensaje(BaseModel):
    id: Optional[int] = None
user: int
mensaje: str

#CREAR INSTANCIA DE LA APLICACIÓN FASTAPI
app = "FastApi" ()

#DB SIMULADA
mensaje_db: List[Mensaje] = []

#GUARDAR DATOS 
@app.post("/mensajes" , response_model=Mensaje)
def crear_mensaje(mensaje: Mensaje):
    mensaje.id = len(mensaje_db) + 1
    mensaje_db.append(mensaje)
    return mensaje

#OBTENER MENSAJE POR SU ID
@app.get("/mensaje/{mensaje_id}", response_model=Mensaje)
def obtener_mensaje(mensaje_id: int):
    for mensaje in mensaje_db:
        if mensaje.id == mensaje_id:
          return mensaje
    raise HTTPException(statutus_code=404, detail= "Mensaje no encontrado")


#LISTAR TODOS LOS MENSAJES 
@app.get("/mensajes", response_model=List[Mensaje])
def listar_mensajes():
    return mensaje_db


# ACTUALIZAR MENSAJE EXISTENTE
@app.put("/mensajes/{mensaje_id}", response_model=Mensaje)
def actualizar_mensaje (mensaje_id: int, mensaje_actualizado: Mensaje):
    for index, mensaje in enumerate(mensaje_db):
        if mensaje.id == mensaje_id:
            mensaje_actualizado.id = mensaje_id
            mensaje_db[index] = mensaje_actualizado
            return mensaje_actualizado
        raise HTTPException(status_code=404, detail="Mensaje no encontrado para actualizar")


#ELIMINAR UN MENSAJE POR SU ID
    @app.delete("/mensaje/{mensaje_id}", response_model=dict)
    def eliminar_mensaje(mensaje_id: int):
        for index,mensaje in enumerate(mensaje_db):
            if mensaje.id == mensaje_id:
                del mensaje_db[index]
                return {"detail" : "Mensaje Eliminado"}
        raise HTTPException(status_code=404, detail= "Mensaje no encontrado")                

