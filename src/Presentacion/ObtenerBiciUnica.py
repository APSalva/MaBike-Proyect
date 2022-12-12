# Importamos las funciones que vamos a utilizar
from diccionario import *
from CrearArchivo import *


def CrearBiciUnica():
    contador = 0
    for value in Diccionario_JSON():
        Pag_Bici_Unica = f"""
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
                    <a href="../index-Todas.html"><img src="Img/icon.png" weight="80px" height="80x" alt="icono-MaBike"></a>
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
        """
        id_bici = value["_id"]
        img_bici = value["img"]
        nombre_bici = value["nombre"]
        marca_bici = value["marca"]
        precio_bici = value["precio"]
        tipo_bici = value["tipo"]
        material_bici = value["material"]
        n_velocidades_bici = value["n_velocidades"]
        peso_bici = value["peso"]
        ubicacion_bici = value["ubicacion"]
        volumen_ruedas_bici = value["volumen_ruedas"]
        Pag_Bici_Unica += f"""
        <div class="img-bici-div">
            <img class="img-bici" src="{img_bici}" height="600" width="600"><br>
            <p>{nombre_bici}</p>
            <p class="precio">{precio_bici}</p>
        </div>
        <div>
            <table class="tabla-bici-unica">
                <tr class="">
                    <th>Tipo</th>
                    <td>{tipo_bici}</td>
                </tr>
                <tr>
                    <th>Marca</th>
                    <td>{marca_bici}</td>
                </tr>
                <tr>
                    <th>Material</th>
                    <td>{material_bici}</td>
                </tr>
                <tr>
                    <th>Número de velocidades</th>
                    <td>{n_velocidades_bici}</td>
                </tr>
                <tr>
                    <th>Peso</th>
                    <td>{peso_bici}</td>
                </tr>
                <tr>
                    <th>Ubicación</th>
                    <td>{ubicacion_bici}</td>
                </tr>
                <tr>
                    <th>Volumen ruedas</th>
                    <td>{volumen_ruedas_bici}</td>
                </tr>
            </table>
        </div>
    </body>
</html>  
        """
        CrearArchivo(f"""./docs/BicisUnicas/{id_bici}.html""",Pag_Bici_Unica)

CrearBiciUnica()