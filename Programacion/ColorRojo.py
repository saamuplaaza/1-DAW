
listaColores= []

while True:
    color= input("\nIntroduzca un color (Si introduce el rojo no podrá introducir más colores): ")
    listaColores.append(color)

    if color.lower()=="rojo":
        break

for color in listaColores:
    print (color)
print("Ha introducido el color rojo, ya no puede seguir añadiendo colores a la lista.\n¡MUCHAS GRACIAS POR SU TIEMPO!")