# Desde esté programa ejecutaremos todos los programas creados para poder crear automaticamente
# la página web de MaBike



# Ejecutamos el programa de la API para crear el JSON
# from database.MongoAPI import ObtenerJson
# ObtenerJson()

# # Crear index.html
from ObtenerIndice import ObtenerIndice
ObtenerIndice()

# Crear index-Todas.html
from ObtenerIndice_Todas import ObtenerIndiceTodas
ObtenerIndiceTodas()

# Crear los indices de los tipos de bicis
from ObtenerIndiceTiposTodas import ObtenerIndiceTiposTodas
ObtenerIndiceTiposTodas()

# Obtener la página de la bicis unicas
from ObtenerBiciUnica import ObtenerBiciUnica
ObtenerBiciUnica()

# Crear Formulario
from ObtenerFormulario import ObtenerFormulario
ObtenerFormulario()

# Crear Carrito Vacio
from ObtenerCarritoVacio import ObtenerCarritoVacio
ObtenerCarritoVacio()

# Crear pagina de las localizaciones
from ObtenerLocalizaciones import CrearPaginasLocalizaciones
CrearPaginasLocalizaciones()
