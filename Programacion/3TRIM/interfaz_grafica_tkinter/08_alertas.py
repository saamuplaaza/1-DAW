from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(
    bd=70
)

def sacarAlerta():
    MessageBox.showinfo("Alerta", "Hola me llamo Samuel, esto es una alerta desde python") # showerror / showwarning
    
def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Continuar ejecutando la aplicación?")
    if resultado != "yes":
        MessageBox.showinfo("Chaooo!!!", f"Adios {nombre}")
        ventana.destroy()


Button(ventana, text="Mostrar alerta", command=sacarAlerta).pack()
Button(ventana, text="Salir", command=lambda : salir("Samuel")).pack()


ventana.mainloop()