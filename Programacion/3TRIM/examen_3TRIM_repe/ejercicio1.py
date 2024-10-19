# ******************************************
# Ejercicio 1 del Examen del 3er Trimestre
# Samuel Plaza Sáez
# ******************************************

from io import open
import os

# Ruta desde donde se ejecuta el programa
raiz = os.getcwd()


def buscarArchvivo(ruta):
    
    subcarpetas = os.listdir(ruta)
    
    if archivo in subcarpetas:
        # Leer el contenido y almacenarlo
        fichero = open(ruta + "/" + archivo, 'r', encoding="utf-8")
        contenido = fichero.read()
        fichero.close()

        return True, contenido
    else:
        return False, None

def recorrerCarpetas(ruta):
    subcarpetas = os.listdir(ruta) # lista de todas las subcarpetas que hay desde la ruta de ejecución
    
    for carpeta in subcarpetas:

        # Si la subcarpeta es un archivo no cambia la ruta, pero si es una carpeta, cambia la ruta
        if len(carpeta.split(".")) == 1:
            rutaNueva = ruta + "/" + carpeta

            encontrado, contenido = buscarArchvivo(rutaNueva)
            # Si encontrado es True, ejecuta las siguientes líneas de código
            if encontrado:
                print("Ruta del archivo: " + rutaNueva + "/" + archivo)
                print("CONTENIDO:")
                print(contenido)
                input("Pulsa Intro para continuar...\n")

            recorrerCarpetas(rutaNueva)


if __name__ == "__main__":
    os.system("cls")
    archivo = input("Nombre del archivo: ")
    recorrerCarpetas(raiz)