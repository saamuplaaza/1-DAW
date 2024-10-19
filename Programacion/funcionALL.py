
#Solicito variables por teclado.
nombre=input("Nombre: ")
apellidos=input("Apellidos: ")
edad=input("Edad: ")

#Creo una listacon variables.
lista=(nombre,apellidos,edad)

#Si no estan todas las variables, se lo digo al usuario.
todosRellenos=all(lista)
if not todosRellenos:
    print("Tienes que rellenar todos los datos.")
else:
    print("Hola %s %s."% (nombre, apellidos))