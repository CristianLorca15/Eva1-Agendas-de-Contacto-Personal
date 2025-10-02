````
utilizar la cmd no la powershell

-----------------------------------------------------------------------------------------------------

Comando para crear el entorno virtual

-python --version
-python -m venv venv

Luego de eso entramos a la carpeta venv, luego la carpeta scripts y 
arrastramos el file activate.bat a la terminal para determinar la ruta y entrar al entorno virtual

Si funciono deberia salir (venv) al principio de todo

------------------------------------------------------

Comandos para la instalacion de Django

pip install django ## instalamos Django

django-admin startproject bienvenida ## Creamos el proyecto con el nombre bienvenida

cd bienvenida ## comando para cambiar a la ruta con la carpeta

python manage.py runserver ##comando para correr el servidor

## Comandos claves para migracion

python manage.py makemigrations ## creea migraciones 

python manage.py migrate ## este las aplica las migraciones


##creamos la carpeta Models.py

python manage.py makemigrations bienvenida

python manage.py migrate bienvenida


## luego de esto creamos una tabla Producto con dos columnas: nombre y precio en el file de Models.

## El resto esta en los apuntes de la clase 3

## se creo una carpeta templates y dentro de esta una carpeta productos y dentro de esta un file que se llama lista.html en donde esta la estructura de nuestro html

Base de datos DB Browser para manejar bases de datos ## sirve para hacer pruebas

## Creamos una nueva app inventario
 con el comando python manage.py startapp inventario

 creamos la carpeta forms.py dentro de inventario

##comando para crear super admin
python manage.py createsuperuser
 

Username (leave blank to use 'sistemas'): admin
Email address: admin@admin.cl 
Password:admin
Password (again):admin

tailwindcss (Flowbin)
######
Es una libreria para darle estilo a la pagina
######



````