#Ejercicio 6

import array

numero=input ("Dime un número del 0 al 3: ")
numero=int(numero)

vector=["amarillo","rojo","verde","azul"]
if numero>=0 and numero<=3:
    print ("El color es el "+vector[numero]+".")
else:
    print ("Número erróneo.")
