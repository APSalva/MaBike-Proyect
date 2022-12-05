import webbrowser
import MongoAPI

f = open("general_bicis.html", "w")

general = """

<!DOCTYPE html>
<html lang="es">
    <head>
        <title> MonBike</title>
        <meta charset="UTF-8">
        <meta name="description" content="La mejor web de bicis">
        <meta name="author" content="Ana Perez y Juan Tur">
        <meta name="date" content="12/11/2022">
        <meta name="generator" content="Visual Studio Code">
        <meta name="last-modified" content="12 de Noviembre de 2022">
        <meta name="keyword" content="bicis, ciclismo, MonBike">

        <link rel="shortcut icon" href="../src/img/monbike_bici_logo.png">
        <link rel='stylesheet' href='style.css' type='text/css'>

    </head>
    <body>
        <header>

        </header>

        <center>
            <table style="background-color: #ffff;">
                <tr>
                    <th>
                        Foto de la bici
                    </th>
                    <th>
                        
                    </th>
                    <th>
                        Contenido
                    </th>
                    <th>
                        Comprar
                    </th>
                </tr>
                <tr>
                    <th>
                        IMAGEN BICI
                    </th>
                    <th>
                        
                    </th>
                    <td>
                        <p>
                            TEXTO BICI (aqui ira toda la información de la bici con sus respectivas caracteristicas...)
                        </p>
                    </td>
                    <td>
                        <p>
                            IMAGEN <br>
                            COMPRAR
                        </p>
                    </td>
                </tr>
            </table>
        </center>
        

        <footer id="main-footer">
            <p>Creado por <a href="mailto:">Ana perez</a> y <a href="mailto:jtur@cifpfbmoll.eu">Juan Tur</a></p>
        </footer>

    </body>
</html>
"""

f.write(general)
f.close()

webbrowser.open_new_tab("geneal_bicis.html")