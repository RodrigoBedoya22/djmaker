#**Dj Maker**
Dj maker es un script que facilita la creación de proyectos django : creando un entorno virtual, permitiendo la creacion de proyectos con nombre personalizado y también creación de multiples aplicaciones de dos naturalezas concretas: **web** y **api**.

##**Uso**
En la carpeta donde se va a crear el proyecto, clone este repositorio.

Luego de clonado el repositorio, abra una terminal en la carpeta donde se encuentra el script y ejecute:

`python djmaker.py`

Este comando iniciará el script pasando por cada una de las etapas explicadas a continuación.

#**Etapas**
##**1. Creación del entorno virtual**
En primer lugar, DjMaker creará un entorno virtual python en una carpeta llamada venv, donde se instalaran las dependencias django.

##**2. Instalación de librerias**
En segundo lugar, se utilizará el entorno virtual creado anteriormente para instalar las dependencias necesarias.
Las dependencias necesarias pueden modificarse en la linea 170 del codigo, donde se le pasa una lista con todas las dependencias a instalar.

167 async def main():
168   
169    await crearEntornoVirtual()
170    await instalarLibrerias(["django", "flask"]) <-- aqui se ponen las librerias
171    await crearProyecto()
172    print("Fin del programa")

##**3. Creación del proyecto**
En tercer lugar, instaladas ya las dependencias necesarias, se procederá a la creacion del proyecto.
Dj maker preguntará que nombre tendrá el proyecto y procederá a crearlo.

##**4. Creación de aplicaciones**
En cuarto lugar, Dj maker preguntará cuántas aplicaciones se desea crear.

Por cada aplicación se pedirá ingresar el nombre que tendrá la misma y su naturaleza.
La naturaleza de una aplicación puede ser **web** o **api**
-**web**: tendrá la carpeta **templates**, necesaria para la renderización de html's. Ademas contendrá el archivo **urls.py**
-**api** Una aplicacion api será una aplicación pensada para jsonresponse, por lo que no contedrá la carpeta **templates**
