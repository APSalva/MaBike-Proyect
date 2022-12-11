
import json
from diccionario import *
from CrearArchivo import * 

def ObtenerIndiceTodas():
    indicetodas = f"""
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>MaBike-Todas las bicicletas</title>
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
                    <li><a href="index.html"><img src="Img/play.png" wight="25px" height="25px" alt="Atrás"></a></li>
                    <li><a href="#">Regístrate <img src="Img/registro.png" wight="25px" height="25px"alt="Registrate"></a></li>
                    <li><a href="Carrito-vacio.html">Carrito <img src="Img/carrito.png" wight="25px" height="25px" alt="Carrito"></a></li>
                    <li><a href="https://www.correos.es/es/es/herramientas/localizador/envios">Envío a Domicilio <img src="Img/envio.png" wight="25px" height="25px" alt="Envio a Domicilio"></a></li>
                    <li><a href="#">Recogida en Tienda <img src="Img/tienda.png" wight="25px" height="25px" alt="Recogida en Tienda"></a></li>
                    <li><a href="https://www.palma.cat/portal/BICIPALMA/RecursosWeb/DOCUMENTOS/9/12_47262_2.pdf">Términos y Condiciones <img src="Img/terminos.png" wight="25px" height="25px" alt="Términos y Condiciones"></a></li>
                </ul>
            </nav>
        </header>
        <div class="header-index">
            <h1>MaBike</h1>
            <p>Mallorca Rental Bike</p>
        </div>
        <div class="DecoLine">
            <ul class="barraNav2">
                <li><a href="index-carretera.html">Bicicletas de carretera</a></li>
                <li><a href="index-MTB.html">MTB</a></li>
                <li><a href="index-Ciudad.html">Bicicletas de Ciudad</a></li>
                <li class="desplegable"><a href="index-EBikes.html">E-Bikes</a></li>
            </ul>
        </div>
        <!--lista de bicis-->
        <div class="segundo-header">
            <p class="header-bicis">Todas las Bicicletas</p>
        </div>
        <div class="tienda">
            <div class="fila">"""
    for value in Diccionario_JSON():
        img_bici = value["img"]
        nombre_bici = value["nombre"]
        tipo_bici = value["tipo"]
        precio_alquiler = "15€"
        indicetodas += f"""
                <div class="columna-bici1">
                    <div class="foto">
                        <a href=""><img src="{img_bici}" width="250px" height="250px"></a>
                        <a href=""><h4>{nombre_bici}</h4></a>
                        <br>
                        <h4>Precio de alquiler</h4>    
                        <ul class="bk1">
                            <li><span><a href="">{tipo_bici}</a></span></li>
                            <li><span class="precio"><a href="">{precio_alquiler}</a></span></li>     
                        </ul>
                    </div>
                </div> """
    indicetodas += f"""
            </div>
        </div>                    
    </body>
    <footer id="main-footer"><p> Creado por <a href="mailto:jtur@cifpfbmoll.eu"> Juan Tur </a> y <a href="mailto:aperezsalva@cifpfbmoll.eu"> Ana Pérez Salvà </a></p></footer>
</html>"""
    
    CrearArchivo("docs/index-Todas.html",indicetodas)

ObtenerIndiceTodas()