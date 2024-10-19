# ******************************************
# Ejercicio 3 del Examen del 3er Trimestre
# Samuel Plaza Sáez
# ******************************************

from tkinter import *
from PIL import Image, ImageTk
import os
import pathlib

def seleccionar():
    nombreImg = opcionMenu.get()
    imagen = Image.open(f"./{nombreImg}")  
    render = ImageTk.PhotoImage(imagen)
    seleccionado.config(image=render)
    seleccionado.image = render

def rutaActual(ruta):
    lista = os.listdir(ruta)
    return lista

# Ruta del fichero .py
ruta = str(pathlib.Path().absolute())
lista = rutaActual(ruta)

# Creamos una lista con todas las imagenes que haya en ese directorio
listaImagenes = []
for archivo in lista:
    archivoDiv = archivo.split(".")
    if len(archivoDiv) >1:
        if archivoDiv[1] == "jpg":
            listaImagenes.append(archivo)


# Creamos la ventana
ventana = Tk()
ventana.geometry("800x500")
ventana.title("Ejercicio 3")

# Encabezado con fondo gris y letras blancas
encabezado = Label(ventana, text="Ejercicio 3")
encabezado.config(
    width=85,
    padx=15,
    pady=15,
    bg="gray",
    fg="white",
    font=("Times New Roman", 16),
    anchor=CENTER
)
encabezado.grid(row=0, column=0, columnspan=7, sticky=N)

# Option Menu
opcionMenu = StringVar()
opcionMenu.set(listaImagenes[0])
Label(ventana, text="Seleccione una opcion").grid(row=1, column=0, columnspan=6)
select = OptionMenu(ventana, opcionMenu, *listaImagenes)
select.grid(row=2, column=0, columnspan=6)


# Botón para ver la imagen
Button(ventana, text="Ver", command=seleccionar).grid(row=3, column=0, columnspan=6)

seleccionado = Label(ventana)
seleccionado.config(
    anchor=CENTER
)
seleccionado.grid(row=4, column=0, columnspan=6)


ventana.mainloop()