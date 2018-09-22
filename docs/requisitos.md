# VirtualUSM

A continuación se definirá la aplicación y sus requisitos.

## Abstracto

La aplicación es parte de un juego, este consiste que los __jugadores__ en buscar en las dependecias
de la universidad distintos __coleccionables__ en forma de __códigos QR__. Estos colecionables
incluyen información relevante de la universidad, de la carrera Ing Civil Informática y un
incentivo que impulse a su búsqueda y colección.
 
 Estos coleccionables son administrados por
un __administrador__ el cual se encarga tanto de agregar, modificar y eliminar los colecionable,
además de tener una forma sencilla de llevarlos al mundo real. También debe ser capaz de 
ver los resultados actuales del juego, quien va ganando, cuantos jugadores, etc.

Los jugadores usarán sus smartphones para la búsqueda, podrán agregar los colecionables usando
la cámara, deben tener un mapa para ubicarse en la universidad y 
poder ver y compartir su progreso. La aplicación debe ser sencilla 
en su uso y de rápido inicio a la acción.

En cuanto a los coleccionables, pueden ser globos, tazos, monedas, etc. 
Pero deben estar acompañados de información como el lugar donde está, imágenes,
links útiles (como la malla interactiva) o easter eggs.

## Modelo de dominio

El módelo consiste de 4 clases: el administrador, el jugador y el item, este
 está conformado por el coleccionable y la información, img, etc.


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
5. Tener un dashboard de administración
6. Generar e imprimir los códigos QR para los coleccionables
7. Tener un tutorial de como jugar

## Requisitos no funcionales

0. Debe ser fácil de entrar al juego, no necesitar instalar, ser una webapp
1. Debe rápido de comenzar a jugar, no necesitar registro.
2. Debe estar enfocado en ser usado en dispositivos móviles.
3. Debe ser llamativo, que le de un motivo al jugar para ir en busqueda de los coleccionables.
4. Debe ser útil para los jugadores