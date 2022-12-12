# MaBike Proyect

## Introducción

El nuevo departamento de desarrollo necesita una plataforma para que la gente local y los/as turistas puedan chequear la disponibilidad de las bicicletas y la localización dónde se encuentran. 

Para ello, utilizaremos **Mongo Atlas**, servicio de la base de datos MongoDB. Los programas se crearán a partir del lenguage de programación **Python**, versión 3.10.7.

La web estática se generará a partir de **GitHub Pages**.

![text-1670859066040](https://user-images.githubusercontent.com/117761833/207085803-469afebb-6491-4ca6-a849-275f9a6e8267.png)

La idea de MaBike, surgió de "Mallorca y bike", en uno de los primeros trabajos de Base de Datos que nos fue encomendado. Al principió surgió como una broma, pero al final decidimos que era una buena decisión quedarnos con el nombre, sobretodo por el significado de la unión de las dos palabras.

## Conceptos Clave 

* Python
* MongoAltas
* HTML
* CSS
* GitHub Pages

## Requerimientos

 --
 --
 
## Pasos en la Creación de la Web

 ### Base de Datos:
  * Lo primero que hicimos fue hacer un cluster en Atlas donde crear la base de datos.
  * Creamos varias colecciones que almacenásen todos los tipos de datos necesarios.
  * Con el lenguaje de programación python, hicimos una API que fuera capaz de exportar todos los datos en formato JSON.
  
 ### HTML y CSS:
  * Empezámos haciendo una intro y, poco a poco, fuimos añadiendo distintas páginas HTML, complementándolas y dándoles forma con un archivo externo de CSS.
  * Despues de crear diversas plantillas, creamos nuevas carpetas, orgánizamos el código y descargámos todos los archivos necesários para un mejor funcionamento de la página web.
  * Añadimos la funcionalidad responsive para iPhone 11 PRO iOS 14.6 y iPad iPadOS 14.7.1 a todas las páginas.
  * Por último, añadimos todos los enlaces funcionales para una buena y fluida navegación de la página.
  
 ### Python:
 * Después de tener la base de datos preparada, junto con una API funcional y diversas plantillas de HTML, empezamos a probar distintas formas de crear los programas para que se crearan los archivos HTML a través de python.
 * Entre las distintas formas se encontraban: Pymongo (el cual no tenía un funcionamiento correcto en nuestros equipos), Flask (sencillo pero no apto para el proyecto), también se testearon otros como Jinja2... Al final, decidímos hacerlo directamente sin emplear librerías externas.
  * Creamos un CRUD para que facilitara la modificación e inserción de datos.
  ![imagen](https://user-images.githubusercontent.com/117761833/207097565-2a7083b3-18cc-43c6-afc6-1d300aafec19.png)

  * Cuando estuvo todo el HTML y CSS en una fase prácticamente final, hicimos diferentes programas para que se generáran todos los HTML necesários para llevar acabo el proyecto.
  
 


