import webbrowser

f = open("index_bikes.html", "w")

index = """
<!DOCTYPE html>
<html lang="es">
    <head>
        <title> MonBike</title>
        <meta charset="UTF-8">
        <meta name="description" content="La mejor web de bicis">
        <meta name="author" content="Juan Tur y Ana Pérez">
        <meta name="date" content="12/11/2022">
        <meta name="generator" content="Visual Studio Code">
        <meta name="last-modified" content="12 de Noviembre de 2022">
        <meta name="keyword" content="bicis, ciclismo, MonBike">
        <base href="http://127.0.0.1:5500/MonBike/index.html" target="_blank">
        <link rel="shortcut icon" href="img/monbike_logo.png">
        <link rel='stylesheet' href="styles.css">
    </head>
    <body>
    <!--Barra de navegación-->
        <header id="header">
          <nav class="nav">
            <a href="#" class="logo">Logo</a>
            <ul class="nav-menu">
                <li class="nav-menu-item">
                    <!--Creamos un desplegable-->
                    <select name="tipos" id="dropdown-tipos">
                        <option value="mtb">Mtb</option>
                        <option value="carretera">Carretera</option>
                        <option value="city-bike">City Bike</option>
                        <option value="mtb-electrica">Mtb Electrica</option>
                        <option value="carretera-electrica">Carretera Electrica</option>
                        <option value="city-bike-electrica">City Bike Electrica</option>
                    </select>
                </li>
                <li class="nav-menu-item">
                    <select name="ubicacion" id="dropdown-ubicacion">
                        <option value="palma">Palma</option>
                        <option value="inca">Inca</option>
                        <option value="manacor">Manacor</option>
                        <option value="alcudia">Alcudia</option>
                        <option value="calvia">Calvia</option>
                    </select>
                </li>
            </ul>
          </nav>
        </header>
        <!--Titulo-->
        <h1>MonBike</h1>
        <!--Productos separados en secciones-->
        <section>
            <div class="card">
                <img src="https://acortar.link/kYAPRZ" width="200" height="200" alt="Bici de carretera de aluminio">
            </div>
        </section>
        <section>
            <div class="card">
                <img src="https://acortar.link/kYAPRZ" width="200" height="200" alt="Bici de carretera de aluminio">
            </div>
        </section>
        <section>
            <div class="card">
                <img src="https://acortar.link/kYAPRZ" width="200" height="200" alt="Bici de carretera de aluminio">
            </div>
        </section>
        <section>
            <div class="card">
                <img src="https://acortar.link/kYAPRZ" width="200" height="200" alt="Bici de carretera de aluminio">
            </div>
        </section>
        <section>
            <div class="card">
                <img src="https://acortar.link/kYAPRZ" width="200" height="200" alt="Bici de carretera de aluminio">
            </div>
        </section>
        <section>
            <div class="card">
                <img src="https://acortar.link/kYAPRZ" width="200" height="200" alt="Bici de carretera de aluminio">
            </div>
        </section>
        <section>
            <div class="card">
                <img src="https://acortar.link/kYAPRZ" width="200" height="200" alt="Bici de carretera de aluminio">
            </div>
        </section>
        <section>
            <div class="card">
                <img src="https://acortar.link/kYAPRZ" width="200" height="200" alt="Bici de carretera de aluminio">
            </div>
        </section>
        <section>
            <div class="card">
                <img src="https://acortar.link/kYAPRZ" width="200" height="200" alt="Bici de carretera de aluminio">
            </div>
        </section>
        <section>
            <div class="card">
                <img src="https://acortar.link/kYAPRZ" width="200" height="200" alt="Bici de carretera de aluminio">
            </div>
        </section>
        <section>
            <div class="card">
                <img src="https://acortar.link/kYAPRZ" width="200" height="200" alt="Bici de carretera de aluminio">
            </div>
        </section>
        <section>
            <div class="card">
                <img src="https://acortar.link/kYAPRZ" width="200" height="200" alt="Bici de carretera de aluminio">
            </div>
        </section>
        <section>
            <div class="card">
                <img src="https://acortar.link/kYAPRZ" width="200" height="200" alt="Bici de carretera de aluminio">
            </div>
        </section>
        <section>
            <div class="card">
                <img src="https://acortar.link/kYAPRZ" width="200" height="200" alt="Bici de carretera de aluminio">
            </div>
        </section>
        <section>
            <div class="card">
                <img src="https://acortar.link/kYAPRZ" width="200" height="200" alt="Bici de carretera de aluminio">
            </div>
        </section>

        <br>

        <table>
            <tr>
                <th>
                    
                </th>
            </tr>
        </table>
        

        <footer id="main-footer">
            <p>Creado por <a href="">Ana perez</a> y <a href="mailto:jtur@cifpfbmoll.eu">Juan Tur</a></p>
        </footer>

    </body>
</html>
"""
f.write(index)
f.close()

webbrowser.open_new_tab("index_ºbikes.html")