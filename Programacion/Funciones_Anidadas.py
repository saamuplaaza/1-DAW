
def suma(i, listaNumeros,resultadoFinal):
    if i<(len(listaNumeros)-1):
        numero=listaNumeros[i]
        resultado=numero+listaNumeros[i]
        i+=1
        resultadoFinal=resultado+listaNumeros[i]
        suma(i,listaNumeros,resultadoFinal)
    print(resultadoFinal)

listaNumeros=[]
i=0
resultadoFinal=0

while True:
    numeros=int(input("Número: "))
    listaNumeros.append(numeros)
    if numeros==0:
        break

print(len(listaNumeros))
suma(i,listaNumeros,resultadoFinal)