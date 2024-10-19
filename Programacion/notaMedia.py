#Ejercicio 4

import statistics

#Pido notas y hago la media con la funcion media.
nota1=input("Nota 1: ")
nota1=float(nota1)
nota2=input("Nota 2: ")
nota2=float(nota2)
nota3=input("Nota 3: ")
nota3=float(nota3)
listnumber=nota1,nota2,nota3

media=statistics.mean(listnumber)
media=float(media)
media=round(media, 2)
print("Nota media: "+str(media))
