
import json
from diccionario import * 

def ObtenerIndiceHTML():
    try:
        indexhtml = f'''<!-- HTML de Mabike -->
<!DOCTYPE html> 
<html lang="es">
    <head>
        <title>MaBike</title>
        <meta charset="UTF-8">
        <meta name="description" content="La mejor web de bicis">
        <meta name="author" content="Juan Tur y Ana Pérez">
        <meta name="date" content="12/11/2022">
        <meta name="generator" content="Visual Studio Code">
        <meta name="last-modified" content="12 de Noviembre de 2022">
        <meta name="keyword" content="bicis, ciclismo, MonBike">
        <base target="_blank">
        <!-- <link rel="shortcut icon" href="img/monbike_logo.png"> -->
        <link rel='stylesheet' href="styles.css">
        <link href='https://fonts.googleapis.com/css?family=Comfortaa' rel='stylesheet'>
    </head>
    <body>
        <!--Barra de navegación-->
        <header id="header">
            <nav class="nav">
                <div id="HeaderBanner">Blog | Tiendas BMK | Únete a la red | Tienda de Bicicletas |  <span style="color: orange">¿Necesitas ayuda?</span> <a href="https://mail.google.com">Contáctanos</a> <img src="https://cdn-icons-png.flaticon.com/512/2811/2811016.png" wight="15px" height="15px"></div>   
            </nav>
            <div id="Marca">MaBike</div>
        </header>
        <!--Titulo-->
        <h1>MaBike</h1>
        <!--Productos separados en secciones-->'''
        for value in Diccionario_JSON():
            img_bici = value["img"]
            indexhtml +=f'''
    <section>
        <div class="card">
            <img src= "{img_bici}",width="200" height="200" alt="Bici de carretera de aluminio">
        </div>
    </section>'''
        indexhtml+=f'''
    <footer id="main-footer">
        <p>Creado por <a href="mailto:Anaperez@gmail.com">Ana Perez</a> y <a href="mailto:jtur@cifpfbmoll.eu">Juan Tur</a></p>
    </footer>
    </body>
</html>'''
    # Excepciones 
    except KeyError:
        print("El valor no es correcto")
    except TypeError: 
        print("El nombre del archivo o de la ruta es incorrecto")
    except TimeoutError:
        print("El tiempo de espera se ha agotado")

    # Si todo es correcto que continue 
    else:    
        return indexhtml