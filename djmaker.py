import os , asyncio

async def crearEntornoVirtual():
    """
    Crea el entorno virtual donde se instalaran las dependencias para el proyecto
    """

    mostrarTitulo("Creando entorno virtual...")

    await ejecutarProceso(("python", "-m", "venv", "venv"))

    print("Entorno virtual creado")

async def instalarLibrerias(librerias: list[str]):
    """
    Instala las librerias indicadas
    
    :param librerias: La lista de librerias a instalar en el entorno virtual
    :type librerias: list[str]
    """

    mostrarTitulo("Instalando librerias...")

    entorno = os.path.join("venv", "Scripts", "python.exe")

    for libreria in librerias:
        print(f"Instalando {libreria}...\n")
        
        await ejecutarProceso((entorno, "-m", "pip", "install", libreria))

        print(f"\nLibreria {libreria} instalada correctamente")

async def crearProyecto():
    """
    Crea un proyecto django con el nombre indicado en los input
    """
    mostrarTitulo("Creando proyecto...")

    while True:
        nombre_proyecto = str(input("Ingrese el nombre de su proyecto: "))

        if " " in nombre_proyecto:
            print("\nERROR: El nombre del proyecto no debe contener espacios (Ej: 'mi_proyecto'). Intentelo denuevo.\n ")
        else:
            break

    print(f"\nCreando proyecto llamado '{nombre_proyecto}' \n")

    django_admin_path = os.path.join("venv", "Scripts", "django-admin.exe")

    await ejecutarProceso((django_admin_path, "startproject", nombre_proyecto))

    print(f"Proyecto {nombre_proyecto} creado con exito \n")
    
    await crearAplicacionesEnProyecto(nombre_proyecto)

async def crearAplicacionesEnProyecto(proyecto):
    """
    Crea la cantidad de aplicaciones dada en el input "cant_aplicaciones".
    Una vez creada la aplicación, se instalará automaticamente en el proyecto.

    Por cada aplicacion se pedira los input:
        -nombre : el nombre de la aplicacion
        -naturaleza: la naturaleza de la aplicacion, debe seleccionar una opcion de las siguientes:
            - 1. Naturaleza web
            - 2. Naturaleza api

    :param proyecto: El proyecto donde se crearán e instalarán las aplicaciones indicadas.
    """

    mostrarTitulo("Creando aplicaciones...")

    while True:
        cant_aplicaciones = int(input("¿Cuántas aplicaciones desea crear?: "))

        if cant_aplicaciones <= 0:
           print("\nERROR: El número de aplicaciones debe ser mayor a cero.\n")
        else:
           break

    for i in range(cant_aplicaciones):
        
        print(F"\nCreando aplicacion {i+1}\n")

        #ingresar nombre de la aplicacion

        while True:
            nombre_app = str(input("Ingrese el nombre de la app: "))

            if " " in nombre_app:
                print("\nERROR: El nombre de la aplicación no debe contener espacios (Ej: 'mi_aplicación'). Intentelo denuevo.\n")
            else:
                break

        #ingresar naturaleza de la aplicacion: web/api
        while True:

            naturaleza_app = int(input("\nNaturaleza de la aplicación\n\n\t-1. Web\n\t-2. Api\n\nSeleccione una naturaleza (1-2): """))

            if naturaleza_app == 1:
                await crearAppWeb(proyecto, nombre_app)
                break
            elif naturaleza_app == 2:
                await crearAppApi(proyecto, nombre_app)
                break
            else:
                print("\nERROR: La naturaleza ingresada no es válida. Ingrese una opción válida.\n")

        #instalar app en proyecto

        instalarApp(proyecto,nombre_app)

        print(f"\nAplicaciones creadas [ {i+1} / {cant_aplicaciones} ]\n")
    
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

    print(f"\nAplicacion {nombre_app} creada con exito")

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
    
    #Se crea la carpeta templates y una carpeta con el nombre de la app
    templates_path= os.path.join(proyecto,nombre_app,"templates", nombre_app)
    os.makedirs(templates_path, exist_ok=True)

    #Crear archivo index.html
    html = os.path.join(templates_path, "index.html")
    HTML_CONT ="""<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<title>Document</title>\n</head>\n<body>\n\n</body>\n</html>"""
    with open(html, 'w') as f:
        f.write(HTML_CONT) 

    #Crear archivo urls.py
    urls = os.path.join(proyecto, nombre_app, "urls.py")
    URLS_CONT=  """from django.contrib import admin\nfrom django.urls import path\n\nurlpatterns = [\n\tpath('admin/', admin.site.urls),\n]"""
    with open(urls, 'w') as f:
        f.write(URLS_CONT)

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

def mostrarTitulo(titulo):
    """
    Representa en consola el titulo dado con un recuadro
    
    :param titulo: El titulo a mostar 
    """
    barra= "="*(len(titulo)+10)
    print(f"\n{barra}\n||   {titulo}   ||\n{barra}\n")

def instalarApp(nombre_proyecto, nombre_aplicacion):
    """
    Agrega la app dada a la lista de aplicaciones instaladas del proyecto dado.
    
    :param nombre_proyecto: El nombre del proyecto en el cual se instalará la app
    :param nombre_aplicacion: El nombre de la aplicacion a agregar a la lista de aplicaciones instaladas del proyecto
    """
    SETTINGS_PROYECTO = f"{nombre_proyecto}/{nombre_proyecto}/settings.py"

    with open(SETTINGS_PROYECTO, 'r') as archivo:
        lineas= archivo.readlines()
        
    with open(SETTINGS_PROYECTO, 'w') as archivo:
        #se busca el lugar donde agregar la app
        instaladas_index= lineas.index('INSTALLED_APPS = [\n')
        nuevo = lineas[0:instaladas_index+1]

        #se agrega el nombre de la app al principio de la lista
        nuevo.append(f"\t'{nombre_aplicacion}',\n")

        #se termina sobreescribe con el archivo settings.py con el nuevo contenido
        nuevo = nuevo + lineas[instaladas_index+1:len(lineas)]
        archivo.writelines(nuevo)

async def main():
    await crearEntornoVirtual()

    #agregar aqui las dependencias deseadas (EJ : ["django", "flask", "pillow", etc...])
    await instalarLibrerias(["django"])

    await crearProyecto()
    print("Fin del programa")

if __name__ == "__main__":
    asyncio.run(main())

