# Dj Maker
Dj maker es un script que facilita la creación de proyectos django : creando un entorno virtual, permitiendo la creacion de proyectos con nombre personalizado y también creación de multiples aplicaciones de dos naturalezas concretas: **web** y **api**.

## Instalación
Desde Visual Studio Code acceda a la carpeta donde creará su proyecto django y abra una nueva terminal en la misma.

Clone el repositorio con el siguiente comando:

`git clone https://github.com/RodrigoBedoya22/djmaker.git`

Una vez clonado el repositorio ejecute el script con el comando:

`python djmaker/djmaker.py`

Este comando iniciará el script pasando por cada una de las etapas explicadas a continuación.

# Etapas
## 1. Creación del entorno virtual
En primer lugar, DjMaker creará un entorno virtual python en una carpeta llamada venv, donde se instalaran las dependencias django.

## 2. Instalación de librerias
En segundo lugar, se utilizará el entorno virtual creado anteriormente para instalar las dependencias que se indiquen.
Por defecto se instalará la ultima version de django, pero las dependencias a instalar pueden ser modificadas en la función **instalarLibrerias()** dentro de la funcion **main**, al principio del código.
Es posible también instalar versiones concretas de dependencias, siguiendo el formato **dependencia==version**.

Con versiones específicas:

`await instalarLibrerias(["django==4.2.19", "flask==3.1.1", "etc"])` <-- librerias necesarias y sus versiones

O la ultima version de las dependencias:

`await instalarLibrerias(["django", "flask", "etc"])` <-- solo nombres

Tambien es posible mezclar entre versiones concretas y ultimas versiones:

`await instalarLibrerias(["django", "flask==3.1.1", "etc"])`

## 3. Creación del proyecto
En tercer lugar, instaladas ya las dependencias necesarias, se procederá a la creacion del proyecto.
Dj maker preguntará que nombre tendrá el proyecto y procederá a crearlo.

## 4. Creación de aplicaciones
En cuarto lugar, Dj maker preguntará cuántas aplicaciones se desea crear.

Por cada aplicación se pedirá ingresar el nombre que tendrá la misma y seleccionar su naturaleza. La naturaleza de una aplicación puede ser **web** o **api**

- **web**: tendrá la carpeta **templates**, necesaria para la renderización de html's. Ademas contendrá el archivo **urls.py**
- **api** Una aplicacion api será una aplicación pensada para jsonresponse, por lo que no contedrá la carpeta **templates**

Si desea crear una aplicación web: seleccione la opción 1. 

Si desea crear una aplicación api: seleccione la opción 2.

