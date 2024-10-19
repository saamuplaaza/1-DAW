from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()

ventana.geometry("750x480")

Label(ventana, text="Hola me llamo Samuel").pack(anchor=E)

imagen = Image.open("./Captura CPU-Z.jpg")
render = ImageTk.PhotoImage(imagen)

Label(ventana, image = render).pack()

ventana.mainloop()