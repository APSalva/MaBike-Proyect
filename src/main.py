# Desde esté programa ejecutaremos todos los programas creados para poder crear automaticamente
# la página web de MaBike



# Ejecutamos el programa de la API para crear el JSON
# from database.MongoAPI import ObtenerJson
# ObtenerJson()

# # Crear index.html
from Presentacion.ObtenerIndice import ObtenerIndice
ObtenerIndice()

# Crear index-Todas.html
from Presentacion.ObtenerIndice_Todas import ObtenerIndiceTodas
ObtenerIndiceTodas()

# Crear los indices de los tipos de bicis
from Presentacion.ObtenerIndiceTiposTodas import ObtenerIndiceTiposTodas
ObtenerIndiceTiposTodas()

# Obtener la página de la bicis unicas
from Presentacion.ObtenerBiciUnica import ObtenerBiciUnica
ObtenerBiciUnica()

# Crear Formulario
from Presentacion.ObtenerFormulario import ObtenerFormulario
ObtenerFormulario()

# Crear Carrito Vacio
from Presentacion.ObtenerCarritoVacio import ObtenerCarritoVacio
ObtenerCarritoVacio()

# Crear pagina de las localizaciones
from Presentacion.ObtenerLocalizaciones import ObtenerLocalizaciones
ObtenerLocalizaciones()