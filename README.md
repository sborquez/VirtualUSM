# VirtualUSM

Virtual es una aplicación web diseñada para _dispositivos móviles_ cuya dinámica consiste en búscar códigos QR en las dependecias de una institución para acceder a información de interés para el jugador.

## InfoQuest 

La primera versión lanzada de VirtualUSM fué [_InfoQuest_](https://infoquest.herokuapp.com/) para el día de puertas abiertas 2018 de la UTFSM. En esta versión los jugadores debían buscar dentro de la universidad diferentes códigos QR ubicados en lugares icónicos de la universidad, los jugadores accedian a información sobre la Univeridad y la carrera Ingeniería Civil Informática, además de mostrar un mapa de Casa Central y las localidades ya visitadas y coleccionar diferentes _stickers_.

## Detalles

La aplicación fué desarrollada con Python 3.6 usando el framework Django para el backend. La lectura de los códigos QR fué realizada con [instascan](https://github.com/schmich/instascan), un framework de Javascript y el diseño usando el framework de CSS [PureCSS](http://purecss.io).

Además se tiene soporte para API Rest, de esta manera se puede visualizar el estado del juego de manera sencilla y dinámica desde cualquier otra aplicación, ya sea jQuery AJAX, jupyter notebook, etc.

## Desafíos

Uno de los desafios que me encontré durante el desarrollo de la aplicación fué tener que reducir lo más posible el tiempo entre que se conoce la aplicación y en comenzar a jugar. Se llegó a la reducción del proceso de registro a solo dos pasos, una breve introducción al juego y la elección de un nickname, dejando toda la lógica de sesiones a las cookies.

El segundo fué la facilidad de uso, la aplicación debía ser sencilla de utilizar. Esto se logró tomando como base para el diseño las heurísticas de nielsen, llegando así a un diseño similar a una aplicación de smartphone pero en el navegador.

