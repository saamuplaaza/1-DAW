from tkinter import *

ventana = Tk()
ventana.geometry("800x300")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 12)
)
encabezado.grid(row=0, column=0, columnspan=6, sticky=N)

def mostrarProfesion():
    texto = ""
    if web.get():
        texto += "Desarrollo Web"
        
    if movil.get():
        if web.get():
            texto += " y desarrollo móvil"
        else:
            texto += "Desarrollo móvil"
            
        
    mostrar.config(
        text = texto,
        bg="green",
        fg="white"
    )

def marcar():
    marcado.config(text=opcion.get())
    
def seleccionar():
    seleccionado.config(text=opcionMenu.get())

web = IntVar()
movil = IntVar()
# Botones
Label(ventana, text="¿A qué te dedicas?").grid(row=1, column=0)
Checkbutton(
    ventana, 
    text="Desarrollo Web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0)

Checkbutton(
    ventana, 
    text="Desarrollo Multiplataforma",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=3, column=0)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)

# Radiobuttons
opcion = StringVar()
opcion.set(None)
Label(ventana, text="¿Cuál es tu género?").grid(row=5, column=0)
Radiobutton(
    ventana, 
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=6)
Radiobutton(
    ventana, 
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=7)

marcado = Label(ventana)
marcado.grid(row=8)

# Option Menu
opcionMenu = StringVar()
opcionMenu.set("Opcion 1")
Label(ventana, text="Seleccione una opcion").grid(row=6, column=1)
select = OptionMenu(ventana, opcionMenu, "Opcion 1", "Opcion 2", "Opcion 3")
select.grid(row=7, column=1)

Button(ventana, text="Ver", command=seleccionar).grid(row=8, column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=9, column=1)

ventana.mainloop()