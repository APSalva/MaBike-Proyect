# Importamos las librerias 
from ObtenerIndiceHTML import ObtenerIndiceHTML
from CrearArchivo import *

# Creamos una función para crear el indice del html
def CrearIndiceHTML():
    try:
        CrearArchivo("docs/index.html",ObtenerIndiceHTML())
    except TimeoutError:
        print("Tiempo de espera agotado")
CrearIndiceHTML()