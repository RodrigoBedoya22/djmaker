import os , asyncio

async def crearEntornoVirtual():
    """
    Crea el entorno virtual donde se instalaran las dependencias para el proyecto
    """
    print("\n===============================")
    print("|| Creando entorno virtual... ||")
    print("===============================\n")

    await ejecutarProceso(("python", "-m", "venv", "venv"))

    print("\nEntorno virtual creado")

async def instalarLibrerias(librerias: list[str]):
    """
    Instala las librerias indicadas
    
    :param librerias: La lista de librerias a instalar en el entorno virtual
    :type librerias: list[str]
    """
    print("\n===============================")
    print("||  Instalando librerias...   ||")
    print("===============================\n")

    entorno = os.path.join("venv", "Scripts", "python.exe")
    for libreria in librerias:
        print(f"Instalando {libreria}...\n")
        
        await ejecutarProceso((entorno, "-m", "pip", "install", libreria))

        print(f"\nLibreria {libreria} instalada correctamente\n")

async def crearProyecto():
    """
    Crea un proyecto django con el nombre indicado en los input
    """

    print("\n===============================")
    print("||     Creando proyecto...    ||")
    print("===============================\n")

    nombre_proyecto = str(input("Ingrese el nombre de su proyecto: "))

    print(f"\nCreando proyecto llamado '{nombre_proyecto}' \n")

    django_admin_path = os.path.join("venv", "Scripts", "django-admin.exe")

    await ejecutarProceso((django_admin_path, "startproject", nombre_proyecto))

    print(f"Proyecto {nombre_proyecto} creado con exito \n")
    
    await crearAplicacionesEnProyecto(nombre_proyecto)

async def crearAplicacionesEnProyecto(proyecto):
    """
    Crea la cantidad de aplicaciones dada en el input "cant_aplicaciones"
    Por cada aplicacion se pedira los input:
        -nombre : el nombre de la aplicacion
        -naturaleza: la naturaleza de la aplicacion, puede ser web o api
    
    :param proyecto: El proyecto donde se crearán las aplicaciones indicadas.
    """
    print("\n===============================")
    print("||   Creando aplicaciones...  ||")
    print("===============================\n")

    while True:
        cant_aplicaciones = int(input("¿Cuántas aplicaciones desea crear?: "))
        if cant_aplicaciones <= 0:
           print("Error: El numero de aplicaciones debe ser mayor a cero.")
        else:
           break

    for i in range(cant_aplicaciones):
        num_app = i+1

        print(F"\nCreando aplicacion {num_app}\n")
        #ingresar nombre de la aplicacion
        nombre_app = str(input("Ingrese el nombre de la app: "))

        #ingresar naturaleza de la aplicacion: web/api
        while True:
            naturaleza_app = str(input("Ingrese la naturaleza de la app [web/api]: ")).lower()

            if naturaleza_app == "web":
                await crearAppWeb(proyecto, nombre_app)
                break
            elif naturaleza_app == "api":
                await crearAppApi(proyecto, nombre_app)
                break
            else:
                print("\nLa naturaleza ingresada no es válida.\n")

        print(f"\nApplicaciones creadas [ {num_app} / {cant_aplicaciones} ]")
    
    print("Todas las aplicaciones fueron creadas correctamente\n")

async def crearApp(proyecto,nombre_app):
    """
    Crea una app estandar de Django.
    
    :param proyecto: El proyecto donde se creará la app
    :param nombre_app: El nombre que tendrá la app
    """

    django_path = os.path.abspath(os.path.join("venv", "Scripts", "django-admin.exe"))

    print(f"\nCreando app '{nombre_app}'...")

    await ejecutarProceso((django_path, "startapp", nombre_app), cwd=proyecto)

    print(f"\nAplicacion {nombre_app} creada con exito \n")

async def crearAppWeb(proyecto,nombre_app):
    """
    Utiliza la funcion "crearApp" estandar.
    Crea una app estandar y agrega archivos necesarios para una app web django:
        - archivo urls.py
        - carpeta templates/nombre_app
        - archivo index.html dentro de templates por defecto
    
    :param proyecto: El proyecto donde se creará la app web
    :param nombre_app: El nombre que tendra la app web
    """
    #Se llama a crearApp estandar
    await crearApp(proyecto,nombre_app)

    #
    templates_path= os.path.join(proyecto,nombre_app,"templates", nombre_app)
    os.makedirs(templates_path, exist_ok=True)

    #Crear archivo index.html
    html = os.path.join(templates_path, "index.html")
    htmlCont ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
                
</body>
</html>
    """
    with open(html, 'w') as f:
        f.write(htmlCont)
        

    #Crear archivo urls.py
    urls = os.path.join(proyecto, nombre_app, "urls.py")
    urlsCont=  """
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
     """
    with open(urls, 'w') as f:
        f.write(urlsCont)

async def crearAppApi(proyecto,nombre_app):
    await crearApp(proyecto,nombre_app)

async def ejecutarProceso(comando, cwd=None):
    """
    Ejecuta un comando en consola
    
    :param comando: Una tupla con todos los parametros del comando ordenados
    :param cwd: Una directorio (opcional)
    """
    proceso = await asyncio.create_subprocess_exec(*comando, cwd=cwd)
    await proceso.wait()

async def main():
    
    await crearEntornoVirtual()
    await instalarLibrerias(["django "])
    await crearProyecto()
    print("Fin del programa")

if __name__ == "__main__":
    asyncio.run(main())

