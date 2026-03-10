from fastapi import FastAPI
from models import Caballero

app = FastAPI()

@app.get("/showcaballeros")
def mostrarCaballeros(int:id):
    pass

@app.get("/figthcaballero")
def pelea(int:id1, int: id2):
    pass

@app.get("/showconstelacion")
def mostrarconstelacion(int: id):
    pass

@app.get("/showyourcaballero")
def mostraruncaballero(int:id):
    pass