from tkinter import *

ventana = Tk()
ventana.geometry("700x700")
ventana.config(
    bd=50,
)

def getDato():
    resultado.set(dato.get())
    if len(resultado.get()) >=1:
        textoRecogido.config(
    bg="green",
    fg="white"
)

dato = StringVar()
resultado = StringVar()

Label(ventana, text="Mete un texto").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="Dato recogido: ").pack(anchor=NW)
textoRecogido = Label(ventana, textvariable=resultado)

textoRecogido.pack(anchor=NW)

Button(ventana, text="Mostrar dato", command=getDato).pack(anchor=NW)

ventana.mainloop()