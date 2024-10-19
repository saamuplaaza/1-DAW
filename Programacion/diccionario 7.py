listaCompra = {}

while True:
    articulo = input("Nombre del articulo: ")
    if articulo=="":
        break
    precio = input("Precio: ")

    listaCompra[articulo]=precio

if listaCompra=={}:
    print("Adios")
else:
    print("Lista de la compra")
    for i in listaCompra:
        print("%s-->%s" %(i, listaCompra[i]))