from CrearArchivo import *

def ObtenerCarritoVacio():
    carritovacio = f"""

<!DOCTYPE html>
<html lang="es">
    <head>
        <title>MaBike-Carrito</title>
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
                <a href="index-Todas.html"><img src="Img/icon.png" weight="80px" height="80x" alt="icono-MaBike"></a>
            </div>
            <nav class="barraNav">
                <ul class="barraNav">
                    <li><a href="../index.html"><img src="Img/play.png" wight="25px" height="25px" alt="Atrás"></a></li>
                    <li><a href="../formulario-registro.html">Regístrate <img src="Img/registro.png" wight="25px" height="25px"alt="Registrate"></a></li>
                    <li><a href="../Carrito-vacio.html">Carrito <img src="Img/carrito.png" wight="25px" height="25px" alt="Carrito"></a></li>
                    <li><a href="https://www.correos.es/es/es/herramientas/localizador/envios">Envío a Domicilio <img src="Img/envio.png" wight="25px" height="25px" alt="Envio a Domicilio"></a></li>
                    <li><a href="../localizaciones-palma.html">Recogida en Tienda <img src="Img/tienda.png" wight="25px" height="25px" alt="Recogida en Tienda"></a></li>
                    <li><a href="https://www.palma.cat/portal/BICIPALMA/RecursosWeb/DOCUMENTOS/9/12_47262_2.pdf">Términos y Condiciones <img src="Img/terminos.png" wight="25px" height="25px" alt="Términos y Condiciones"></a></li>
                </ul>
            </nav>
        </header>
        <div class="carrito-vacio"><h1>¡Uy! Tu Carrito está vacío</h1></div>
        <div>
            <img class="carrito-vacio" src="Img/carrito-vacio.png" weight="900" height="800" alt="carrito-vacio">
        </div>
    </body>
</html>"""
    CrearArchivo("docs/Carrito-vacio.html",carritovacio)
ObtenerCarritoVacio()
    
    
    
    
    
    
    
    
    