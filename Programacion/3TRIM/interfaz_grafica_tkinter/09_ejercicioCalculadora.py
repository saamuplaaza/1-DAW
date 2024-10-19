"""
CALCULADORA:
- Dos campos de texto
- Cuartro botones para las operaciones
- Mostrar resultados en una alerta
"""

from tkinter import *
from tkinter import messagebox as MessageBox

class Calculadora:
    def __init__(self):
        self.numero1=StringVar()
        self.numero2 = StringVar()
        self.resutado = StringVar()
    
    def sumar(self,numeros):
        resultado = float(numeros[0]) + float(numeros[1])
        MessageBox.showinfo("Resultado Suma", f"{numeros[0]:g}+{numeros[1]:g}={resultado:g}")
        self.resetearNumeros()

    def restar(self,numeros):
        resultado = float(numeros[0]) - float(numeros[1])
        MessageBox.showinfo("Resultado Resta", f"{numeros[0]:g}-{numeros[1]:g}={resultado:g}")
        self.resetearNumeros()

    def multiplicar(self,numeros):
        resultado = float(numeros[0]) * float(numeros[1])
        MessageBox.showinfo("Resultado Multiplicación", f"{numeros[0]:g}*{numeros[1]:g}={resultado:g}")
        self.resetearNumeros()

    def dividir(self,numeros):
        if numeros[1] == 0:
            MessageBox.showinfo("Resultado División", "No se puede dividir entre 0")
            return False
        else:
            resultado = float(numeros[0]) / float(numeros[1])
            MessageBox.showinfo("Resultado División", f"{numeros[0]:g}/{numeros[1]:g}={resultado:g}")
            self.resetearNumeros()

calculadora = Calculadora()

ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("700x400")

marco = Frame(ventana, width=250, height=250)
marco.config(
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

# Label para el campo (Primer numero)
labelNum1 = Label(marco, text= "Primer número")
labelNum1.pack()

# Campo de texto (Primer numero)
campoTextoNum1 = Entry(marco)
campoTextoNum1.pack()

# Label para el campo (Segundo número)
labelNum2 = Label(marco, text= "Segundo número")
labelNum2.pack()

# Campo de texto (Segundo número)
campoTextoNum2 = Entry(marco)
campoTextoNum2.pack()

# Números
def getNumeros():
    num1 = float(campoTextoNum1.get())
    num2 = float(campoTextoNum2.get())
    return num1, num2

def resetearNumeros(num1, num2):
    
    num1.set("")
    num2.set("")


# Botones
suma = Button(marco, text="Sumar", command= lambda : calculadora.sumar(getNumeros())).pack(side=LEFT, fill=X, expand=YES)
resta = Button(marco, text="Restar", command= lambda : calculadora.restar(getNumeros())).pack(side=LEFT, fill=X, expand=YES)
mult = Button(marco, text="Multiplicar", command= lambda : calculadora.multiplicar(getNumeros())).pack(side=LEFT, fill=X, expand=YES)
div = Button(marco, text="Dividir", command= lambda : calculadora.dividir(getNumeros())).pack(side=LEFT, fill=X, expand=YES)    

ventana.mainloop()