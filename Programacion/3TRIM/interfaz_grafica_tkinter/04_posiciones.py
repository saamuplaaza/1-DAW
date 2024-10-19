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
    bg="green",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
    )
texto.pack(side=TOP, fill=BOTH, expand=YES)

texto = Label(ventana, text="básico")
texto.config(
    height=5,
    bg="red",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
    )
texto.pack(side=LEFT,fill=X, expand=YES)

texto = Label(ventana, text="básico 2")
texto.config(
    height=5,
    bg="blue",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
    )
texto.pack(side=LEFT,fill=X, expand=YES)

texto = Label(ventana, text="básico 3")
texto.config(
    height=5,
    bg="pink",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
    )
texto.pack(side=LEFT,fill=X, expand=YES)

ventana.mainloop()