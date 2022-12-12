from ObtenerIndiceTiposCarretera import * 
from ObtenerIndiceTiposCiudad import *
from ObtenerIndiceTiposMtb import *
from ObtenerIndiceTiposE_bike import *

def ObtenerIndiceTiposTodas():
    ObtenerIndiceTiposCarretera()
    ObtenerIndiceTiposCiudad()
    ObtenerIndiceTiposEbike()
    ObtenerIndiceTiposMtb()

ObtenerIndiceTiposTodas()