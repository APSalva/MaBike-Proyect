![text-1670859066040](https://user-images.githubusercontent.com/117761833/207085803-469afebb-6491-4ca6-a849-275f9a6e8267.png)

## Introducción

El nuevo departamento de desarrollo necesita una plataforma para que la gente local y los/as turistas puedan chequear la disponibilidad de las bicicletas y la localización dónde se encuentran. 

Para ello, utilizaremos **Mongo Atlas**, servicio de la base de datos MongoDB. Los programas se crearán a partir del lenguaje de programación **Python**, versión 3.10.7.

La web estática se generará a partir de **GitHub Pages**.

La idea de **MaBike**, surgió de "Mallorca y bike", en uno de los primeros trabajos de Base de Datos que nos fue encomendado. Al principio surgió como una broma, pero al final decidimos que era una buena decisión quedarnos con el nombre, sobretodo por el significado de la unión de las dos palabras.

## Conceptos Clave 

* Python
* MongoAltas
* HTML
* CSS
* GitHub Pages

## Requerimientos
* Git 
* Python
* Requests
* Pytest

* jsonschema==4.16.0
* Markdown==3.1.1
* pytest==7.2.0
* python-apt===2.0.0-ubuntu0.20.04.8-zorin1
* python-dateutil==2.8.2
* python-debian===0.1.36ubuntu1
* python-pam==1.8.4
* python-xapp==1.8.1
* python-xlib==0.23
* requests==2.22.0
* requests-unixsocket==0.2.0
* webencodings==0.5.1
* WebOb==1.8.5

## Uso
MaBike es un programa que está creado para crear una página web de alquiler de bicis. Para poder ejecutarlo tendras que ir a la carpeta src y ejecutar todos los programas que empiecen por obtener.

## Pasos en la Creación de la Web

 ### Base de Datos:
  * Lo primero que hicimos fue hacer un **cluster en Atlas** donde crear la base de datos.
  * Creamos varias **colecciones** que almacenásen todos los tipos de datos necesarios.
  * Con el **lenguaje de programación python**, hicimos una API que fuera capaz de exportar todos los datos en formato JSON.
   * Ejemplo de documento en la base de datos:
   
   ![gfhfhf](https://user-images.githubusercontent.com/117761833/207181886-0b9da827-c496-4472-ae32-374ccaa18178.png)

 ### HTML y CSS:
  * Empezámos haciendo una **intro** y, poco a poco, fuimos añadiendo distintas páginas HTML, complementándolas y dándoles forma con un archivo externo de CSS.
  * Después de crear diversas plantillas, creamos nuevas carpetas, orgánizamos el código y descargámos todos los archivos necesários para un mejor funcionamiento de la página web.
  * Añadimos la funcionalidad responsive para **iPhone 11 PRO iOS 14.6 y iPad iPadOS 14.7.1 a todas las páginas (Firefox)**.
  * Por último, añadimos todos los enlaces funcionales para una buena y fluida navegación de la página.
  
 ### Python:
 * Después de tener la base de datos preparada, junto con una **API** funcional y diversas plantillas de HTML, empezamos a probar distintas formas de crear los programas para que se crearan los archivos HTML a través de python.
 * Entre las distintas formas se encontraban: **Pymongo** (el cual no tenía un funcionamiento correcto en nuestros equipos), **Flask** (sencillo pero no apto para el proyecto), también se testearon otros como **Jinja2**... Al final, decidímos hacerlo directamente sin emplear librerías externas.
  * Creamos un CRUD para que facilitara la modificación e inserción de datos. 
  
  ![imagen](https://user-images.githubusercontent.com/117761833/207097565-2a7083b3-18cc-43c6-afc6-1d300aafec19.png)

  * Cuando estuvo todo el **HTML y CSS** en una fase prácticamente final, hicimos diferentes programas para que se generáran todos los HTML necesários para llevar acabo el proyecto.
  
   ### Diagrama del uso de la Web:
   
  ![Ilustración_sin_título](https://user-images.githubusercontent.com/117761833/207182462-3f8df80a-0497-49c0-bbc1-e223e5de019a.png)

  ### Metodología:
   * **DSDM** (Método de Desarrollo de Sistemas dinámicos) fue el método que empleamos, aunque de una manera simplificada y acorde a nuestros conocimientos y capacidades.
   * Las pautas que seguimos para que el proyecto saliera a delante fueron:
    1. Un estudio de las herramientas con las que podíamos usar y nuestra capacidad para emplearlas.
    2. Hicimos un resumen con las partes mas importantes y necesarias del proyecto.
    3. A partir del anterior punto, hicimos diferentes modelos y plantillas comprobando su funcionalidad.
    4. Diseñamos la parte visual y la estructura del código.
    5. Por último, lo implementamos todo y comprobamos su funcionamiento.
    
 Ejemplo gráfico:
    
![3-1](https://user-images.githubusercontent.com/117761833/207128527-841bf58a-bde8-49a1-8dd9-aa7cc17cbf50.jpg)
  
 ## Clockify
 * Usamos **Clockify** para poder ver y calcular el tiempo dedicado al proyecto, de esta manera, podemos saber cuantos tokens tenemos. A partir de distintas etiquetas y colores, se pueden ver las distintas partes a las que se les ha dedicado tiempo y esfuerzo.

![text-16708590660](https://user-images.githubusercontent.com/117761833/207162905-4dec62aa-ebd7-4f5e-855c-0070b73a7946.png)

 ### Dificultades
 * La primera y más importante dificultad que hemos tenido, ha sido la **incertidumbre**. Había muchas partes del proyecto las cuales no teníamos ni idea de como empezar a llevarlas a cabo. Teniendo en cuenta que no habíamos programado, o visto, un código como el necesário para esta tarea antes. Poco a poco intentamos distintos métodos y herramientas, y con un poco de tiempo sacámos algo funcional gracias a los compañeros y una docena de pruebas distintas. Luego se nos atragantó el uso de GitHub, ya que a veces la conexión con nuestro VSC no parecía funcionar del todo. Respecto a la parte visual, fue la que más tiempo nos llevó pero al tener más fuentes de información no nos costó tanto como la lógica.
