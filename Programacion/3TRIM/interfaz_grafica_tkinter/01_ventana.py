import os.path
# Tkinter --> Modulo para crear interfaces graficas de usuario
from tkinter import *

class Programa:
    def __init__(self):
        self.title = "Título de la ventana"
        self.icon = "./imagenes/logotipo.ico"
        self.iconAlt = "./interfaz_grafica_tkinter/imagenes/logotipo.ico"
        self.size = "750x480"
        self.resizable = False
        
    def cargar(self):
        # Crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana
        # Comprobar si existe el archivo
        rutaIcono = os.path.abspath(self.icon)

        if not os.path.isfile(rutaIcono):
            rutaIcono = os.path.abspath(self.iconAlt)

        # Icono de la ventana
        ventana.iconbitmap(rutaIcono)

        # Mostrar texto en la ventana
        texto = Label(ventana, text = rutaIcono)
        texto.pack()

        # Título de la ventana
        ventana.title(self.title)

        # Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1, 1) # (1,0) para bloquear horizontalmente
        else:
            ventana.resizable(0, 0)

    def addTexto(self):
        texto = Label(self.ventana, text = "Hola desde un metodo")
        texto.pack()
        
    def mostrar(self):
        self.ventana.mainloop()

# Arrancar y mostrar la ventana hasta que se cierre
programa = Programa()
programa.cargar()
programa.addTexto()
programa.addTexto()
programa.mostrar()