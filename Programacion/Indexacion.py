nombre=input("Escribe una palabra: ")
nombre=nombre.lower()
if nombre[0:]==nombre[::-1]:
    print("%s es un palíndromo."%(nombre.capitalize()))
else:
    print("%s no es un palíndromo."%(nombre.capitalize()))