from tkinter import *

ventana = Tk()

ventana.geometry("750x700")

marcoPadre1 = Frame(ventana, width=250, height=250)
marcoPadre1.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

marco1_1 = Frame(marcoPadre1, width=250, height=250)
marco1_1.config(
    bg= "red",
    bd=5,
    relief= SOLID
)
marco1_1.pack(side=LEFT)
marco1_1.pack_propagate(False)
texto1_1 = Label(marco1_1, text="Mi primer marco")
texto1_1.config(
    bg= "red",
    fg= "white",
    font=("Arial", 18),
)
texto1_1.pack(anchor= CENTER, fill=BOTH, expand=YES)

marco1_2 = Frame(marcoPadre1, width=250, height=250)
marco1_2.config(
    bg= "green",
    bd=90,
    relief= RAISED
)
marco1_2.pack(side=RIGHT)

marcoPadre2 = Frame(ventana, width=250, height=250)
marcoPadre2.pack(side=TOP , anchor=N, fill=X, expand=YES)

marco2_1 = Frame(marcoPadre2, width=250, height=250)
marco2_1.config(
    bg= "blue",
    bd=90,
    relief= RAISED
)
marco2_1.pack(side=LEFT)

marco2_2 = Frame(marcoPadre2, width=250, height=250)
marco2_2.config(
    bg= "orange",
    bd=30,
    relief = GROOVE
)
marco2_2.pack(side=RIGHT)

ventana.mainloop()