from tkinter import *
import os.path
from tkinter.font import BOLD

class BibliotecaUI:
    def __init__(self):
        self.title = "Biblioteca desde Python"
        self.icon = "./imagenes/logotipo2.ico"
        self.iconAlt = "../imagenes/logotipo.ico"
        self.size = "400x220+560+280"
        self.resizable = False
    
    def getDatos(self):
        pass
    
    def cargar(self):
        ventana = Tk()
        self.ventana = ventana
        rutaIcono = os.path.abspath(self.icon)
        
        if not os.path.isfile(rutaIcono):
            rutaIcono = os.path.abspath(self.iconAlt)
        
        ventana.iconbitmap(rutaIcono)
        ventana.title(self.title)
        ventana.geometry(self.size)
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)
            
            # wtotal = ventana.winfo_screenwidth()
            # htotal = ventana.winfo_screenheight()
            #  Guardamos el largo y alto de la ventana
            # wventana = 400
            # hventana = 220

            #  Aplicamos la siguiente formula para calcular donde debería posicionarse
            # pwidth = round(wtotal/2-wventana/2)
            # pheight = round(htotal/2-hventana/2)

            #  Se lo aplicamos a la geometría de la ventana
            # ventana.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

            
        
        # Encabezado 
        encabezado = Label(ventana, text="Biblioteca IES. Fidiana")
        encabezado.config(
            width=26,
            fg="black",
            bg="orange",
            font=("Open Sans", 18, BOLD),
            padx=10,
            pady=10,
            )
        encabezado.grid(row=0, column=0, sticky=N, columnspan=6)
        
        Label(ventana).grid(row=1, column=1)

        # Label para el campo (Nombre de usuario)
        labelNombre = Label(ventana, text= "Nombre de usuario")
        labelNombre.grid(row=2, column=0)
        
        # Campo de texto (Nombre de usuario)
        campoTextoNombre = Entry(ventana)
        campoTextoNombre.config(
            justify=LEFT, 
            state=NORMAL,
        )
        campoTextoNombre.grid(row=2, column=1)
        
        # Label para el campo (Contraseña)
        labelContr = Label(ventana, text= "Contraseña")
        labelContr.config(
            pady=10
        )
        labelContr.grid(row=3, column=0)
        
        # Campo de texto (Contraseña)
        campoTextoContr = Entry(ventana)
        campoTextoContr.config(
            justify=LEFT, 
            state=NORMAL
        )
        campoTextoContr.grid(row=3, column=1)
        
        # Botón
        Label(ventana).grid(row=4, column=1)
        boton = Button(ventana, text="Iniciar Sesión")
        boton.config(
            padx=10,
            pady=7,
            bg="black",
            fg="orange",
            font=("Arial",10)
            
        )
        boton.grid(row=5, column=1, sticky=N)


    def mostrar(self):
        self.ventana.mainloop()



biblioteca = BibliotecaUI()
biblioteca.cargar()
biblioteca.mostrar()