from tkinter import *

ventana = Tk()

ventana.geometry("750x480")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="black",
    padx=50,
    pady=30,
    font=("Consolas", 30)
    )
texto.pack()

texto = Label(ventana, text="Me llamo Samuel")
texto.config(
    height=5,
    bg="orange",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
    )
texto.pack(anchor=W)

def pruebas(nombre, apellidos, pais):
    return(f"Hola {nombre} {apellidos}, veo que eres de {pais}")
    

texto = Label(ventana, text=pruebas(nombre="Samuel", apellidos="Plaza", pais="España"))
texto.config(
    height=3,
    bg="red",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="circle"
    )
texto.pack(anchor=E)
texto.pack()

ventana.mainloop()