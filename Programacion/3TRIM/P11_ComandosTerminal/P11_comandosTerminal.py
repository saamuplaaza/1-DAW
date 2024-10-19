import os
import os.path
import shutil

def limpiar():
    """Esta función limpia la pantalla.
    """
    os.system("cls")

def listar(ruta):
    """Esta función lista todos los archivos y carpetas que hay en la ruta especificada.
    Simula el comando dir

    Returns:
        list: lista de todos los archivos y caarpetas que hay en la ruta.
    """
    lista = os.listdir(ruta)
    return lista

def rutaActual(ruta):
    """Esta función te muestra la ruta en la que te encuentras en este momento.

    Args:
        ruta (str): la ruta actual
    """
    return ruta

def crearFichero(ruta, nombreFichero):
    """Esta función crea un archivo en la ruta actual. 

    Args:
        ruta (str): la ruta actual
        nombreFichero (str): El nombre que le hemos puesto al fichero.

    """
    rutaArchivo = ruta + f"\{nombreFichero}"
    open(rutaArchivo, "a+")
    
def crearCarpeta(ruta, nombreCarpeta):
    """Esta función crea un directorio en la ruta especificada.
    Simula el comando mkdir.

    Args:
        ruta (str): la ruta actual
        nombreCarpeta (_type_): el nombre del directorio que queremos crear
    """
    rutaCarpeta = ruta + f"\{nombreCarpeta}"
    os.mkdir(rutaCarpeta)
    
def borrarFichero(ruta, nombreFichero):
    """Esta función elimina un archivo en la ruta actual. 

    Args:
        ruta (str): la ruta actual
        nombreFichero (str): El nombre del fichero que queremos borrar.

    """
    rutaArchivo = ruta + f"\{nombreFichero}"
    os.remove(rutaArchivo)

def borrarCarpeta(ruta, nombreCarpeta):
    """Esta función elimina una carpeta en la ruta actual. 

    Args:
        ruta (str): la ruta actual
        nombreFichero (str): El nombre del directorio que queremos borrar.

    """
    rutaCarpeta = ruta + f"\{nombreCarpeta}"
    shutil.rmtree(rutaCarpeta)
    
def renombrar(ruta, nombreArchivo, nombreArchivoNuevo):
    """Esta función cambia el nombre de un  archivo por otro que elijamos.

    Args:
        ruta (str): la ruta actual
        nombreArchivo (str): nombre del archivo que queremos cambiar
        nombreArchivoNuevo (str): nuevo nombre que le vamos a poner al archivo
    """
    rutaArchivoActual = ruta + f"\{nombreArchivo}"
    rutaArchivoNuevo = ruta + f"\{nombreArchivoNuevo}"
    os.rename(rutaArchivoActual, rutaArchivoNuevo)

def mover(rutaOrigen, rutaDestino):
    """Esta función mueve un archivo de una ruta a otra.

    Args:
        ruta (str): la ruta actual
        rutaNueva (str): laruta a la que vamos a mover el archivo
    """
    shutil.move(rutaOrigen, rutaDestino)
    
def leerArchivo(ruta, nombreArchivo):
    """Abre y devuelve el contenido de un archivo.

    Args:
        ruta (str): La ruta donde se encuentra el archivo
        nombreArchivo (str): Nombre del archivo que queremos abrir.

    Returns:
        str: Contenido del archivo.
    """
    contenido = ""
    archivoLectura = open(ruta + f"\{nombreArchivo}", "r")
    listaContenido = archivoLectura.readlines()
    for frase in listaContenido:
        contenido+= frase
    return contenido

def cambiarDirectorio(rutaNueva):
    """Cambia el directorio actual

    Args:
        ruta (str): la ruta actual
        rutaNueva (str): la ruta a la que nos dirijimos

    Returns:
        str: la nueva ruta
    """
    os.chdir(rutaNueva)

def comprobarComando(ruta, comando):
    """Esta función comprueba que el comando introducido por el usuario es válido.

    Args:
        ruta (str): la ruta en la que nos encontramos.
        comando (str): el comando introducido por el usuario
    """
    if comando[0] == "listar":
        if len(comando)>1:
            rutaLista = ruta + f"\{comando[-1]}"
            if (os.path.isdir(rutaLista)):
                archivos = listar(rutaLista)
            else:
                print("Error. El directorio no existe.")
        elif len(comando) == 1:
            archivos = listar(ruta)
        for archivo in archivos:
            print(archivo)
    elif comando[0] == "sitio":
        sitio = rutaActual(ruta)
        print (sitio)
    elif comando[0] == "crearfichero":
        if len(comando)>1:
            nombreArchivo = comando[-1]
            if not os.path.isfile(ruta + f"\{nombreArchivo}"):
                crearFichero(ruta, nombreArchivo)
            else: 
                print("Error. Ya existe un archivo con ese nombre.")
        else:
            print("Error. Introduzca un nombre para el archivo.")
    
    elif comando[0] == "creardirectorio":
        if len(comando)>1:
            nombreCarpeta = comando[-1]
            if not os.path.isdir(ruta + f"\{nombreCarpeta}"):
                try:
                    crearCarpeta(ruta, nombreCarpeta)
                except FileNotFoundError:
                    print("Error. No se ha encontrado el directorio.")
            else:
                print("Error. Ya existe un directorio con ese nombre.")            
        else:
            print("Error. Introduzca un nombre para el nuevo directorio.")
    
    elif comando[0] == "borrarfichero":
        if len(comando)>1:
            nombreArchivo = comando[-1]
            if os.path.isfile(ruta + f"\{nombreArchivo}"):
                confirmacion = input("¿Está seguro de que desea borrarlo?(y/n):")
                if confirmacion == "y":
                    borrarFichero(ruta, nombreArchivo)
                else:
                    pass
            else:
                print("Error. No se ha encontrado el archivo.")
        else:
            print("Error. Debe introducir el nombre del archivo a eliminar.")
    
    elif comando[0] == "borrardirectorio":
        if len(comando)>1:
            nombreCarpeta = comando[-1]
            if os.path.isdir(ruta + f"\{nombreCarpeta}"):
                confirmacion = input("¿Está seguro de que desea borrarlo?(y/n):")
                if confirmacion == "y":
                    borrarCarpeta(ruta, nombreCarpeta)
                else:
                    pass
            else:
                print("Error. No se ha encontrado el directorio.")
        else:
            print("Error. Debe introducir el nombre del directorio a eliminar.")
    
    elif comando[0] == "renombrar":
        if len(comando)>2:
            nombreArchivo = comando[1]
            nombreArchivoNuevo = comando[-1]
            if (os.path.isfile(ruta + f"\{nombreArchivo}")) or (os.path.isdir(ruta + f"\{nombreArchivo}")):
                try:
                    renombrar(ruta, nombreArchivo, nombreArchivoNuevo)
                except FileExistsError:
                    print("Error. Ya existe un archivo o directorio con ese nombre.")
                    pass
            else:
                print("Error. No se ha encontrado el archivo o directorio.")
        else:
            print("Error. Debe introducir el nombre del archivo o directorio a renombrar y el nombre nuevo.")
    
    elif comando[0] == "mover":
        if len(comando)>3:
            archivo = ruta + f"\{comando[1]}"
            rutaOrigen = ruta + f"\{comando[-2]}"
            rutaOrigenArchivo = rutaOrigen+f"\{comando[1]}"
            rutaDestino = ruta + f"\{comando[-1]}"
            if (os.path.isfile(rutaOrigenArchivo)) or (os.path.isdir(rutaOrigen)):
                mover(rutaOrigenArchivo, rutaDestino)
            else:
                print("Error. No se ha encontrado el fichero o directorio.")
        else:
            print("Error. Debe introducir el nombre del archivo o directorio a mover.")
    
    elif comando[0] == "leerfichero":
        if len(comando)>1:
            nombreArchivo = comando[-1]
            if (os.path.isfile(ruta + f"\{nombreArchivo}")):
                print(leerArchivo(ruta, nombreArchivo))
            else:
                print("Error. El archivo no existe.")
        else: 
            print("Error. Debe introducir el nombre del archivo a leer.")
    
    elif comando[0] == "cambiar":
        if len(comando)>1:     
            rutaNueva = comando[-1].strip("/")
            rutaNueva = rutaNueva.strip("\\")
            if (os.path.isdir(ruta + f"\{rutaNueva}")):
                ruta = cambiarDirectorio(rutaNueva)
            else:
                print("Error. El directorio no existe.")
    
    elif comando[0] == "limpiar":
        limpiar()