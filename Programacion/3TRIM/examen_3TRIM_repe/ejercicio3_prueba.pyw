from tkinter import *
from PIL import Image, ImageTk
import os

def listaImagenes(): 
    imagenes=[]
    ruta=os.getcwd()
    for i in os.listdir(ruta):
        contador=0
        for j in i:
            if j == ".":
                extension=i[contador:]
                if extension == ".jpg":
                    imagenes.append(i)

            else:
                contador+=1
    return imagenes

def seleccionarImagen(): 
    seleccionado = imagen.get()
    ruta_imagen = os.path.join(os.getcwd(), seleccionado)
    if os.path.exists(ruta_imagen):
        img_pil = Image.open(ruta_imagen)
        img_tk = ImageTk.PhotoImage(img_pil)
        label_imagen.config(image=img_tk)

        label_imagen.image = img_tk
    else:
        print("La ruta de la imagen no es válida.")

ventana = Tk()
ventana.title("Ejercicio 3 Examen Programacion")
ventana.geometry("700x700")

titulo = Label(ventana, text="Imagenes Examen")
titulo.grid(row=0, column=0, columnspan=2)
titulo.config(bg="gray", fg="white", width=50, height=2, font=("Consolas", 20))

imagen = StringVar()
imagen.set(None)

imagenes = listaImagenes()
opcion = OptionMenu(ventana, imagen, *imagenes)
opcion.grid(row=1, column=0)

boton = Button(ventana, text="Ver", command=seleccionarImagen)
boton.grid(row=2, column=0)

label_imagen = Label(ventana)
label_imagen.grid(row=3, column=0)

ventana.mainloop()
