from pydantic import BaseModel
from enum import Enum

class Material(str, Enum):
    BRONCE = "Bronce"
    PLATA = "Plata"
    ORO = "Oro"

class Caballero(BaseModel):
    id: int
    name: str
    material: Material
    attack: int
    constelacion: str
    