from CrearArchivo import *
from diccionario import *

def ObtenerLocalizaciones(tipo):
    localizaciones = {
        "palma": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4105.190004941448!2d2.644686118983553!3d39.57273834424209!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1297925c84e499ef%3A0xf99a2d445c5467f2!2sDecathlon%20City!5e0!3m2!1ses!2ses!4v1670770665085!5m2!1ses!2ses",
        "inca": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3749.4730180662054!2d2.9166508151664217!3d39.718769126910864!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xca69ee7494f05c08!2sCFS%20Joves%20d&#39;Inca!5e0!3m2!1ses!2ses!4v1670763552087!5m2!1ses!2ses",
        "manacor": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d8210.99845887956!2d3.2039150717698632!3d39.56751606987178!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12964900035ca6d1%3A0x35298c1f82804327!2sPolideportivo%20Municipal%20Na%20Capellera!5e0!3m2!1ses!2ses!4v1670770748224!5m2!1ses!2ses",
        "calvia": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12303.609481056235!2d2.497202729052716!3d39.56180888233132!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12978a4bcecb9adb%3A0x76527120d9ddb6f0!2sPalau%20d&#39;Esports%20de%20Calvi%C3%A0%20Melani%20Costa!5e0!3m2!1ses!2ses!4v1670770793943!5m2!1ses!2ses",
        "alcudia": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2229.310276303939!2d3.1205986375000045!3d39.85253044274763!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12962c9f2c8dc1b9%3A0xf477fa6709c33ad5!2sActive%20Alcudia!5e0!3m2!1ses!2ses!4v1670770861753!5m2!1ses!2ses",
        "marratxi" : "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15045.781876841358!2d2.728300294436573!3d39.62851064546667!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1297eb243faaaaab%3A0x1dd7c1556873e88f!2sMallorca%20Fashion%20Outlet!5e0!3m2!1ses!2ses!4v1670770385091!5m2!1ses!2ses"
        }

    link = localizaciones.get(tipo)
    PagLocalizaciones = f"""
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>MaBike-Bicicletas Palma</title>
        <meta charset="UTF-8">
        <meta name="description" content="La mejor web de bicis de Mallorca">
        <meta name="author" content="Juan Tur y Ana Pérez">
        <meta name="date" content="12/11/2022">
        <meta name="generator" content="Visual Studio Code">
        <meta name="last-modified" content="29 de Noviembre de 2022">
        <meta name="keyword" content="bicis, ciclismo, MaBike, Mallorca">
        <base target="_blank">
        <link rel="shortcut icon" href="Img/icon.png">
        <link rel='stylesheet' href="style1.css" type="text/css">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <header class="barraNav">
            <div class="logo">
                <img src="img/icon.png" weight="80px" height="80x" alt="icono-MaBike">
            </div>
            <nav class="barraNav">
                <ul class="barraNav">
                    <li><a href="../index.html"><img src="/docs/Img/play.png" wight="25px" height="25px" alt="Atrás"></a></li>
                        <li><a href="../formulario-registro.html">Regístrate <img src="/docs/Img/registro.png" wight="25px" height="25px"alt="Registrate"></a></li>
                        <li><a href="../Carrito-vacio.html">Carrito <img src="/docs/Img/carrito.png" wight="25px" height="25px" alt="Carrito"></a></li>
                        <li><a href="https://www.correos.es/es/es/herramientas/localizador/envios">Envío a Domicilio <img src="/docs/Img/envio.png" wight="25px" height="25px" alt="Envio a Domicilio"></a></li>
                        <li><a href="../localizaciones-palma.html">Recogida en Tienda <img src="/docs/Img/tienda.png" wight="25px" height="25px" alt="Recogida en Tienda"></a></li>
                        <li><a href="https://www.palma.cat/portal/BICIPALMA/RecursosWeb/DOCUMENTOS/9/12_47262_2.pdf">Términos y Condiciones <img src="/docs/Img/terminos.png" wight="25px" height="25px" alt="Términos y Condiciones"></a></li>
                </ul>
            </nav>
        </header>
        <div class="maps">
        <h2>Localizaciones de Tiendas</h2>
        <ul class="maps">
            <li><a href="localizaciones-palma.html">Palma |</a></li>
            <li><a href="localizaciones-inca.html">Inca |</a></li>
            <li><a href="localizaciones-manacor.html">Manacor |</a></li>
            <li><a href="localizaciones-calvia.html">Calviá |</a></li>
            <li><a href="localizaciones-alcudia.html">Alcudia |</a></li>
            <li><a href="localizaciones-marratxi.html">Marratxí |</a></li>
        </ul>
        </div>
        <div class="maps2">
            <iframe src="{link}" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
    </body>
</html>"""
    crear_archivo = open(f"""docs/localizaciones-{tipo}.html""","w", encoding="UTF-8")
    crear_archivo.write(PagLocalizaciones)


def CrearPaginasLocalizaciones():
    # Creamos la página de localizaciones de Palma
    ObtenerLocalizaciones("palma")
    # Creamos la página de localizaciones de Inca
    ObtenerLocalizaciones("inca")
    # Creamos la página de localizaciones de Manacor
    ObtenerLocalizaciones("manacor")
    # Creamos la página de localizaciones de Calvia
    ObtenerLocalizaciones("calvia")
    # Creamos la página de localizaciones de Alcudia
    ObtenerLocalizaciones("alcudia")
    # Creamos la página de localizaciones de Marratxi
    ObtenerLocalizaciones("marratxi")
CrearPaginasLocalizaciones()