import pathlib
import os
from P11_comandosTerminal import comprobarComando

if __name__ == "__main__":
    os.system("cls")
    while True:
        ruta = str(pathlib.Path().absolute())
        rutaSinUnidad = ruta.split(":")[-1].strip("\\")
        comando = input("samuplaza#"+rutaSinUnidad+":\> ").split()
        comprobarComando(ruta, comando)