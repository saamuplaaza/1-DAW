import random       

def ordenar_lista(numeros):
    n = len(numeros)
    lista_ordenada = numeros

    for i in range(n):
        for j in range(0, n-i-1):
            if lista_ordenada[j+1] < lista_ordenada[j]:
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]

    return lista_ordenada

numeros = []
for i in range(5):
    numeros.append(random.randint(1,30))
print("La lista original es: ",(numeros))
print("La lista ordenada es: ",ordenar_lista(numeros))
