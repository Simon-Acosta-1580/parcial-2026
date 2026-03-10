from fastapi import FastAPI
from models import Caballero

app = FastAPI()


db_caballeros = [
    {"id": 1, "name": "Seiya", "material": "Bronce", "attack": 85, "constelacion": "Pegaso"},
    {"id": 2, "name": "Ikki", "material": "Bronce", "attack": 95, "constelacion": "Fénix"},
    {"id": 3, "name": "Shaka", "material": "Oro", "attack": 100, "constelacion": "Virgo"}
]

@app.get("/showcaballeros")
def mostrarCaballeros():
    return db_caballeros

@app.get("/figthcaballero")
def pelea(id1: int, id2: int):
    caballero1 = None
    caballero2 = None

    for i in db_caballeros:
        if i["id"] == id1:
            caballero1 = i
            
    for i in db_caballeros:
        if i["id"] == id2:
            caballero2 = i

    if caballero1 is None or caballero2 is None:
        return {"error": "Uno de los caballeros no fue encontrado"}

    if caballero1["attack"] > caballero2["attack"]:
        ganador = caballero1["name"]
    elif caballero2["attack"] > caballero1["attack"]:
        ganador = caballero2["name"]
    else:
        ganador = "Empate"

    return {"resultado": f"El ganador es {ganador}"}

@app.get("/showconstelacion")
def mostrarconstelacion(id: int):
    resultado = "No encontrado"
    
    for i in db_caballeros:
        if i["id"] == id:
            resultado = i["constelacion"]
            break
            
    return {"constelacion": resultado}

@app.get("/showyourcaballero")
def mostraruncaballero(id: int):
    for i in db_caballeros:
        if i["id"] == id:
            return i
            
    return {"error": "Caballero no existe"}