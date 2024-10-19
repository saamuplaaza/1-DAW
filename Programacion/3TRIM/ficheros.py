from io import open
import pathlib
import shutil
import os
import os.path

# Abrir archivo
ruta = str(pathlib.Path().absolute())+ "/fichero1.txt"
archivo = open(ruta, "a+")

# Escribir en fichero
# archivo.write("Texto metido desde VSCode\n")

# Cerrar archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute())+ "/fichero1.txt"
archivoLectura = open(ruta, "r")

# Leer archivo 
contenido = archivoLectura.read()
print(contenido)

# Leer contenido y guardarlo en lista
# listaContenido = archivoLectura.readlines()
# print(listaContenido)

# Copiar
# rutaNueva = str(pathlib.Path().absolute())+ "/fichero1Copiado.txt"
# shutil.copyfile(ruta, rutaNueva)

# Mover archivo
# rutaOriginal = str(pathlib.Path().absolute())+ "/fichero1Copiado.txt"
# rutaNueva = str(pathlib.Path().absolute())+ "/fichero1CopiadoRenombrado.txt"
# shutil.move(rutaOriginal, rutaNueva)

rutaNueva =  os.path.abspath("./")+ "/fichero1Copiado.txt"
if os.path.isfile(rutaNueva):
    os.remove(rutaNueva)
    print("Archivo borrado satisfactoriamente.")
else:
    print("El archivo no existe. No se puede eliminar.")


if not os.path.isdir("./CarpetaPrueba"):
    os.mkdir("./CarpetaPrueba")
else:
    print("Ya exite una carpeta con ese nombre.")
    
# Eliminar carpeta 
os.rmdir("./CarpetaPrueba")