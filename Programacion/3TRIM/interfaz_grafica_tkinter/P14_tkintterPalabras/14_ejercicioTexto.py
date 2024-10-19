from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.title("Operaciones con texto")
ventana.geometry("450x400+550+200")

def encontrarPalabra(texto, palabra):
    if texto == "":
        MessageBox.showinfo("¿Palabra encontrada?", "No se ha introducido ningún texto.")
    elif palabra == "":
        MessageBox.showinfo("¿Palabra encontrada?", "No se ha ingresado una palabra.")
    elif palabra not in texto: 
        MessageBox.showinfo("¿Palabra encontrada?", f"La palabra '{palabra}' no se ha encontrado en el texto.")
    else:
        MessageBox.showinfo("¿Palabra encontrada?", f"La palabra '{palabra}' se ha encontrado en el texto.")

def contar(texto):
    numPalabras = 0
    numCaracteres = 0
    for palabra in texto.split():
        numPalabras+=1
    for caracter in texto:
        numCaracteres+=1
    MessageBox.showinfo("Conteo de palabras y caracteres", f"El texto contiene {numPalabras} palabras y {numCaracteres} caracteres.")
    
def esPalindromo(texto):
    if texto == texto[::-1]:
        MessageBox.showinfo("¿Es palíndromo?", "El texto es un palídromo.")
    else:
        MessageBox.showinfo("¿Es palíndromo?", "El texto no es un palídromo.")


encabezado = Label(ventana, text="Operaciones con cadenas")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10,
)
encabezado.grid(row=0, column=0, sticky=N,  columnspan= 12)

# Label para el campo (Texto)
labelTexto = Label(ventana, text= "Texto")
labelTexto.config(
    bd=5
)
labelTexto.grid(row=1, column=0, sticky=W)

# Campo de texto (texto)
campoTexto = Text(ventana)
campoTexto.config(
    width=50,
    height=10,
    padx=10,
    pady=10
)
campoTexto.grid(row=2, column=0, columnspan=6)

# Texto
def getTexto():
    texto = campoTexto.get("1.0", "end-1c")
    return texto

def getPalabra():
    palabra = palabraBuscar.get()
    return palabra


# Botones
Label(ventana).grid()
Label(ventana, text= "1. Encontrar palabra").grid(row=4, column=0, sticky=W)
palabraBuscar = Entry(ventana)
palabraBuscar.grid(row=4, column=1)
Button(ventana, text="Encontrar Palabra", command= lambda : encontrarPalabra(getTexto(), getPalabra())).grid(row=4, column=2)
Label(ventana, text= "2. Contar palabras y caracteres").grid(row=5, column=0, sticky=W)
botonContar = Button(ventana, text="Contar", command= lambda : contar(getTexto())).grid(row=5, column=1)
Label(ventana, text= "3. ¿Es palíndromo?").grid(row=6, column=0, sticky=W)
Button(ventana, text="Verificar", command= lambda : esPalindromo(getTexto())).grid(row=6, column=1)

ventana.mainloop()