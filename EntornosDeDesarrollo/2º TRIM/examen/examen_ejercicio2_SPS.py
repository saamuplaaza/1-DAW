def llenar(n):
    tabla = [0] * n
    for i in range(n):
        tabla[i] = i * 10
    return tabla

def sumar(tabla):
    suma = 0
    n = len(tabla)
    for i in range(n):
        suma += tabla[i]
    return suma

def main():
    n = 5
    # tabla = [0] * n
    tabla = llenar(n)
    suma = sumar(tabla)
    print("La suma es:", suma)

# Llamar a la función principal
if __name__ == "__main__":
    main()
