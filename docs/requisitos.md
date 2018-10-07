# VirtualUSM

A continuación se definirá la aplicación y sus requisitos.

## Abstracto

La aplicación es parte de un juego que combina el mundo real con el 
virtual. El juego consiste de este consiste en buscar los diferentes
 __coleccionables__  y repartidos las dependencias de la institución.

Los __jugadores__ usarán sus smartphones para la búsqueda. Usando la
cámara se accede a la __descripción__ y __contenido__ de la localidad.

El __contenido__ es personalizable, puede ser un __video__, __imagén__,
__texto__ o __link__. 

También podrán agregar el __coleccionable__, uno diferente por localidad.
Un __colecionable__ es el insentivo para la búsqueda, __sticker__, 
__monedas__, __globos__, etc.
 
La aplicación debe ser sencilla en su uso, el proceso de comenzar a jugar
debe ser corto. Informar al jugador el proceso y el estado general del juego.
 
Es importante llevar un control del estado del juego. Se tiene un sitio de
__administrador__, desde aquí se pude editar la base de datos, mostrar la 
cantidad de usuario y un resumenes en forma de gráficos.

También podrá generar los códigos qr para los letreros.

## Modelo de dominio

El módelo consiste de 5 clases: el administrador, el jugador, la localidades 
y el coleccionable.


* El administrador administra a jugadores y localidades.
* El jugador coleciona coleccionable visitando a las localidades
* Cada localidad posee su propio coleccionable único.

## Historias de usuarios

* Como administrador quiero poder agregar, modificar y eliminar coleccionables para darle contenido al juego.
* Como administrador quiero generar los códigos QR para llevar los coleccionables al mundo real.
* Como administrador quiero ver la tabla de posiciones del juego para saber el estado actual de este.
* Como administrador quiero ver la cantidad de jugadores actuales para el análisis.

* Como jugador nuevo quiero tener un tutorial que me introdusca al juego para aprender a jugar :B
* Como jugador quiero agregar coleccionables para progresar en el juego.
* Como jugador quiero ver un mapa para no perderme en la universidad.
* Como jugador quiero ver la tabla de posiciones del juego para saber el estado actual del juego.
* Como jugador quiero compartir en mis redes sociales mi progreso para que mis amigos juegue conmigo ::smile::

## Requisitos funcionales

0. Llevar un registro de los usuarios
1. Leer códigos QR para agregar coleccionables
2. Mostrar y compartir el progreso del jugador
3. Tener un mapa de las dependecias de la universidad
4. Tener una tabla de posiciones del juego
5. Tener un dashboard de administración, el dashboard debe responder:
    0. Cantidad de jugadores, activos y no activos
    1. Tabla de posiciones
    2. Lugares más visitados
    3. Visitas por lugar
    4. Visitas por jugador
6. Generar e imprimir los códigos QR para los coleccionables
7. Tener un tutorial de como jugar

## Requisitos no funcionales

0. Debe ser fácil de entrar al juego, no necesitar instalar, ser una webapp
1. Debe rápido de comenzar a jugar, no necesitar registro.
2. Debe estar enfocado en ser usado en dispositivos móviles.
3. Debe ser llamativo, que le de un motivo al jugar para ir en busqueda de los coleccionables.
4. Debe ser útil para los jugadores


## Requisitos no obligatorios

0. Los usuario pueden dejar comentarios en las localidades, solo una vez o quizás más.