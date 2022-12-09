# Importamos las librerias 
from ObtenerIndiceHTML import ObtenerIndiceHTML
from CrearArchivo import *

# Creamos una función para crear el indice del html
def CrearIndiceHTML():
    CrearArchivo("docs/index.html",ObtenerIndiceHTML())
CrearIndiceHTML()