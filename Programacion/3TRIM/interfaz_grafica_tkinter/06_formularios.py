from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.resizable(0,0)
ventana.title("Formulario")

#  Obtenemos el largo y  ancho de la pantalla
wtotal = ventana.winfo_screenwidth()
htotal = ventana.winfo_screenheight()
#  Guardamos el largo y alto de la ventana
wventana = 700
hventana = 400

#  Aplicamos la siguiente formula para calcular donde debería posicionarse
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)

#  Se lo aplicamos a la geometría de la ventana
ventana.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))


# Texto encabezado
encabezado = Label(ventana, text="Formularios con Tkinter - Samuel Plaza")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10,
)
encabezado.grid(row=0, column=0, sticky=N,  columnspan= 6)

# Label para el campo (nombre)
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5)

# Campo de texto (nombre)
campoTexto = Entry(ventana)
campoTexto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campoTexto.config(justify= RIGHT, state= NORMAL)

# Label para el campo (Apellidos)
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, padx=5, pady=5)

# Campo de texto (Apellidos)
campoTexto = Entry(ventana)
campoTexto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campoTexto.config(justify= LEFT, state= DISABLED) # state= DISABLED

# Label para el campo (Descripción)
label = Label(ventana, text="Descripción")
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)

# Campo de texto grande (Descripción)
campoGrande = Text(ventana)
campoGrande.grid(row=3, column=1, sticky=W, padx=5, pady=5)
campoGrande.config(
    width=30, 
    height=5,
    font=("Arial", 12),
    padx=15,
    pady=15
)

# Boton
Label(ventana).grid(row=4, column=1)
boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=N)
boton.config(
    padx=10,
    pady=7,
    bg="green",
    fg="white"
)

ventana.mainloop()