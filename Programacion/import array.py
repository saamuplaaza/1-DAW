import array
vector=["amarillo","rojo","verde","azul"]

numero=input("Dime un número del 0 al 3: ")
numero=int(numero)

if numero>=0 and numero<=3:
    print("Color %s."%(vector[numero]))
else:
    print("Número erroneo.")