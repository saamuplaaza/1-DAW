from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter.font import BOLD

class Examen:
    def __init__(self):
        self.title = "Examen"
        self.geometry = "800x600+350+100"
        self.resizable = False
    
    def cargar(self):
        ventana = Tk()
        self.ventana = ventana
        ventana.title(self.title)
        ventana.geometry(self.geometry)
        ventana.config(
            bg="white"
        )
        
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)
        
        encabezado = Label(ventana, text="Test de Intuición")
        encabezado.config(
            width=85,
            padx=15,
            pady=15,
            fg="black",
            font=("Times New Roman", 16, BOLD),
            anchor=W
        )
        encabezado.grid(row=0, column=0, columnspan=7, sticky=N)
        
        nombre = Label(ventana, text="Nombre")
        nombre.grid(row=0, column=2, sticky=E)
        
        campoNombre = Entry(ventana)
        campoNombre.grid(row=0, column=3, sticky=W)
        
        espacioBlanco = Label(ventana)
        espacioBlanco.config(bg="white")
        espacioBlanco.grid()
        
        # Pregunta 1
        respuesta1 = StringVar()
        respuesta1.set(None)
        pregunta1 = Label(ventana, text="Pregunta 1: Escoja la opción que crea correcta.")
        pregunta1.config(
            padx=10
        )
        pregunta1.grid(row=2, column=0, sticky=W)
        Radiobutton(
            ventana, 
            text="a",
            value="1a",
            bg="white",
            variable=respuesta1
        ).grid(row=3, column=0, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="b",
            value="1b",
            bg="white",
            variable=respuesta1
        ).grid(row=4, column=0, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="c",
            value="1c",
            bg="white",
            variable=respuesta1
        ).grid(row=5, column=0, sticky=W, padx=15)
        
        # Pregunta 2
        respuesta2 = StringVar()
        respuesta2.set(None)
        pregunta2 = Label(ventana, text="Pregunta 2: Escoja la opción que crea correcta.")
        pregunta2.config(
            padx=10
        )
        pregunta2.grid(row=6, column=0, sticky=W)
        Radiobutton(
            ventana, 
            text="a",
            value="2a",
            bg="white",
            variable=respuesta2
        ).grid(row=7, column=0, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="b",
            value="2b",
            bg="white",
            variable=respuesta2
        ).grid(row=8, column=0, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="c",
            value="2c",
            bg="white",
            variable=respuesta2
        ).grid(row=9, column=0, sticky=W, padx=15)
        
        # Pregunta 3
        respuesta3 = StringVar()
        respuesta3.set(None)
        pregunta3 = Label(ventana, text="Pregunta 3: Escoja la opción que crea correcta.")
        pregunta3.config(
            padx=10
        )
        pregunta3.grid(row=10, column=0, sticky=W)
        Radiobutton(
            ventana, 
            text="a",
            value="3a",
            bg="white",
            variable=respuesta3
        ).grid(row=11, column=0, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="b",
            value="3b",
            bg="white",
            variable=respuesta3
        ).grid(row=12, column=0, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="c",
            value="3c",
            bg="white",
            variable=respuesta3
        ).grid(row=13, column=0, sticky=W, padx=15)
        
        # Pregunta 4
        respuesta4 = StringVar()
        respuesta4.set(None)
        pregunta4 = Label(ventana, text="Pregunta 4: Escoja la opción que crea correcta.")
        pregunta4.config(
            padx=10
        )
        pregunta4.grid(row=14, column=0, sticky=W)
        Radiobutton(
            ventana, 
            text="a",
            value="4a",
            bg="white",
            variable=respuesta4
        ).grid(row=15, column=0, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="b",
            value="4b",
            bg="white",
            variable=respuesta4
        ).grid(row=16, column=0, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="c",
            value="4c",
            bg="white",
            variable=respuesta4
        ).grid(row=17, column=0, sticky=W, padx=15)
        
        # Pregunta 5
        respuesta5 = StringVar()
        respuesta5.set(None)
        pregunta5 = Label(ventana, text="Pregunta 5: Escoja la opción que crea correcta.")
        pregunta5.config(
            padx=10
        )
        pregunta5.grid(row=18, column=0, sticky=W)
        Radiobutton(
            ventana, 
            text="a",
            value="5a",
            bg="white",
            variable=respuesta5
        ).grid(row=19, column=0, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="b",
            value="5b",
            bg="white",
            variable=respuesta5
        ).grid(row=20, column=0, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="c",
            value="5c",
            bg="white",
            variable=respuesta5
        ).grid(row=21, column=0, sticky=W, padx=15)
        
        # Pregunta 6
        respuesta6 = StringVar()
        respuesta6.set(None)
        pregunta6 = Label(ventana, text="Pregunta 6: Escoja la opción que crea correcta.")
        pregunta6.grid(row=2, column=3, sticky=W)
        Radiobutton(
            ventana, 
            text="a",
            value="6a",
            bg="white",
            variable=respuesta6
        ).grid(row=3, column=3, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="b",
            value="6b",
            bg="white",
            variable=respuesta6
        ).grid(row=4, column=3, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="c",
            value="6c",
            bg="white",
            variable=respuesta6
        ).grid(row=5, column=3, sticky=W, padx=15)
        
        # Pregunta 7
        respuesta7 = StringVar()
        respuesta7.set(None)
        pregunta7 = Label(ventana, text="Pregunta 7: Escoja la opción que crea correcta.")
        pregunta7.grid(row=6, column=3, sticky=W)
        Radiobutton(
            ventana, 
            text="a",
            value="7a",
            bg="white",
            variable=respuesta7
        ).grid(row=7, column=3, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="b",
            value="7b",
            bg="white",
            variable=respuesta7
        ).grid(row=8, column=3, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="c",
            value="7c",
            bg="white",
            variable=respuesta7
        ).grid(row=9, column=3, sticky=W, padx=15)
        
        # Pregunta 8
        respuesta8 = StringVar()
        respuesta8.set(None)
        pregunta8 = Label(ventana, text="Pregunta 8: Escoja la opción que crea correcta.")
        pregunta8.grid(row=10, column=3, sticky=W)
        Radiobutton(
            ventana, 
            text="a",
            value="8a",
            bg="white",
            variable=respuesta8
        ).grid(row=11, column=3, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="b",
            value="8b",
            bg="white",
            variable=respuesta8
        ).grid(row=12, column=3, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="c",
            value="8c",
            bg="white",
            variable=respuesta8
        ).grid(row=13, column=3, sticky=W, padx=15)
        
        # Pregunta 9
        respuesta9 = StringVar()
        respuesta9.set(None)
        pregunta9 = Label(ventana, text="Pregunta 9: Escoja la opción que crea correcta.")
        pregunta9.grid(row=14, column=3, sticky=W)
        Radiobutton(
            ventana, 
            text="a",
            value="9a",
            bg="white",
            variable=respuesta9
        ).grid(row=15, column=3, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="b",
            value="9b",
            bg="white",
            variable=respuesta9
        ).grid(row=16, column=3, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="c",
            value="9c",
            bg="white",
            variable=respuesta9
        ).grid(row=17, column=3, sticky=W, padx=15)
        
        # Pregunta 10
        respuesta10 = StringVar()
        respuesta10.set(None)
        pregunta10 = Label(ventana, text="Pregunta 10: Escoja la opción que crea correcta.")
        pregunta10.grid(row=18, column=3, sticky=W)
        Radiobutton(
            ventana, 
            text="a",
            value="10a",
            bg="white",
            variable=respuesta10
        ).grid(row=19, column=3, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="b",
            value="10b",
            bg="white",
            variable=respuesta10
        ).grid(row=20, column=3, sticky=W, padx=15)
        Radiobutton(
            ventana, 
            text="c",
            value="10c",
            bg="white",
            variable=respuesta10
        ).grid(row=21, column=3, sticky=W, padx=15)
        
        boton = Button(ventana, text="Finalizar", command= lambda : self.calcularNota(campoNombre, respuesta1, respuesta2, respuesta3, respuesta4, respuesta5, respuesta6, respuesta7, respuesta8, respuesta9, respuesta10))
        boton.grid(row=22, column=2, sticky=W)

    def mostrar(self):
        self.ventana.mainloop()
    
    def calcularNota(self, nombre, respuesta1, respuesta2, respuesta3, respuesta4, respuesta5, respuesta6, respuesta7, respuesta8, respuesta9, respuesta10):
        nota = 0
        if respuesta1.get() == "1a":
            nota +=1
        elif respuesta1.get() == "None":
            nota += 0
        else:
            nota -=1
        if respuesta2.get() == "2b":
            nota +=1
        elif respuesta2.get() == "None":
            nota += 0
        else:
            nota -=1
        if respuesta3.get() == "3a":
            nota +=1
        elif respuesta3.get() == "None":
            nota += 0
        else:
            nota -=1
        if respuesta4.get() == "4a":
            nota += 1
        elif respuesta4.get() == "None":
            nota += 0
        else:
            nota -=1
        if respuesta5.get() == "5b":
            nota += 1
        elif respuesta5.get() == "None":
            nota += 0
        else:
            nota -=1
        if respuesta6.get() == "6c":
            nota += 1
        elif respuesta6.get() == "None":
            nota += 0
        else:
            nota -=1
        if respuesta7.get() == "7a":
            nota += 1
        elif respuesta7.get() == "None":
            nota += 0
        else:
            nota -=1
        if respuesta8.get() == "8c":
            nota += 1
        elif respuesta8.get() == "None":
            nota += 0
        else:
            nota -=1
        if respuesta9.get() == "9b":
            nota += 1
        elif respuesta9.get() == "None":
            nota += 0
        else:
            nota -=1
        if respuesta10.get() == "10a":
            nota += 1
        elif respuesta10.get() == "None":
            nota += 0
        else:
            nota -=1
        
        if nombre.get() =="":
            MessageBox.showinfo("Nota Examen", f"Has sacado un {nota}")
        else:
            MessageBox.showinfo("Nota Examen", f"{nombre.get()}, has sacado un {nota}")
