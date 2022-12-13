from CrearArchivo import * 

def ObtenerFormulario():
    formulario = f"""
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>MaBike-Formulario</title>
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
    <body class="formulario">
        <header class="barraNav">
            <div class="logo">
                <img src="Img/icon.png" weight="80px" height="80x" alt="icono-MaBike">
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
        <section class="form">
            <div class="form-register">
                <h4>Formulario Registro</h4>
                <input class="controls" type="text" name="nombre" placeholder="Ingresa tu nombre">
                <input class="controls" type="text" name="nombre" placeholder="Ingresa tus apellidos">
                <input class="controls" type="email" name="correo" placeholder="Ingresa tu correo">
                <input class="controls" type="password" name="correo" placeholder="Ingresa tu contraseña">
                <p>Estoy de acuerdo con <a href="#">Terminos y Condiciones</a></p>
                <input class="botons "type="submit" value="Registrar">
                <p><a href="#">Ya tengo Cuenta</a></p>
            </div>
        </section>
    </body>
</html>"""
    crear_archivo = open("docs/formulario-registro.html","w", encoding="UTF-8")
    crear_archivo.write(formulario)
ObtenerFormulario()