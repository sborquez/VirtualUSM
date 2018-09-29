# Instrucciones

El siguiente documento es una guía de como instalar los módulos
para poder editar y ejecutar el servidor. 

## Instalación de requisitos

El servidor corre sobre python, usando el framework de [django](https://www.djangoproject.com/)
y el motor de base de datos [postgreSQL](https://www.postgresql.org)

### Python

Utilizaremos __python 3__,  se recomienda el uso de _virtual enviroments_ para la instalación, puede
utilizar [Anaconda](https://www.anaconda.com/download/).

Los módulos a instalar se encuentran en el fichero __requirements.txt__, puede
utilizar el siguiente comando para instalar los requisitos

    pip install -r requirements.txt

### PostgreSQL

Para la base de datos necesitamos instalar PostgreSQL desde el siguiente [link](https://www.postgresql.org/download/)


## Preprarar el servidor

Antes de ejecutar el servidor necesitamos:

### Configurar PostgreSQL

__TODO__: Por ahora usaremos SQLlite, nos saltamos este paso

### Configurar el servidor

Usaremos las variables de entorno para configurar el servidor, así la configuración
queda separada del código.

Pueden ver como configurar las variables de entorno correspondiente a su sistema operativo.

Las variables que definiremos son:

* SECRET_KEY: string de 50 caracteres aleatorios.
* DATABASE_URL: __TODO__ (cuando configuremos la BD lo definiremos)
* DEBUG: True

### Migrar la base de datos
Ejecutar

    $ python manage.py makemigrations
    $ python manage.py migrate

### Agregar usuario administrador

Ejecutar

    $ python manage.py createsuperuser

## Ejecutar el servidor

Finalmente, todo debería estar correcto podemos ejecutar el siguiente
comando reemplazando el puerto:

    $ python manage.py runserver  0.0.0.0:<PORT>
    
## Como editar el servidor

Puedes encontrar los url que se usan en __collectibles/urls.py__

Además puedes usar la url __/admin__ para usar el super usuario para modificar la base de datos.

### Backend

Los directorios importantes son:

* collectibles/views.py: Vistas (o oontroladores del patrón MVC)
* collectibles/models.py: Modelos

### Frontend

Los directorios importantes son:
* collectibles/templates: Templates (o vistas del modelo MVC)
* static: Aquí se encuentran los archivos css, js y medias para la aplicación.

 
