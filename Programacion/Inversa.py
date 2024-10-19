palabra=input("Escribe una palabra: ")
nombreInverso=""
n=-1
while n>=-len(palabra):
    nombreInverso=nombreInverso+palabra[n]
    n-=1       #El -= es equivalente a restar y asignar el resultado a la variable inicial (n=n-1)
if palabra==nombreInverso:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")


#Una forma más sencilla de hacer el ejercicio:
#nombre=palabra.lower()
#if nombre[0:]==nombre[::-1]:
    #print("%s es un palíndromo."%(palabra.capitalize()))
#else:
    #print("%s no es un palíndromo."%(palabra.capitalize()))        (El capitalize se usa para poner la primera letra mayúscula.)
'''i=0
while i<=len(nombreCompleto):
    nombreTransformado=nombreTransformado+nombreCompleto[i]
    i+=1
if nombreCompleto==nombreTransformado:
    print("Vale")
else:
    print("mal")'''