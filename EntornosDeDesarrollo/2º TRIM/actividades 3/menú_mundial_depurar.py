def mostrar_jugadores(titulares):
        dorsales_ordenados = sorted(titulares) 

   
        print("Alineación Titular (Ordenados por Dorsal):")
        print("Dorsal\tJugador")
        for dorsal in dorsales_ordenados:
            jugador = titulares.get(dorsal) 
            print(f"{dorsal}\t{jugador}")


def num_titulares(titulares):
    num_jugadores = len(titulares)
   
    print(f"Iniciaron el partido {num_jugadores} jugadores")


def mostrar_info(titulares):
   
    indices = list(titulares) 

    print("\nLista de todos los índices utilizados en la biblioteca:")
    print(indices)

    valores = list(titulares.values())
    print("\nLista de todos los valores almacenados en la biblioteca:")
    print(valores)

def mostrar_suplentes(suplentes):
    
    print("\nDiccionario suplentes:")
    print("Dorsal\tNombre")
    print("------\t------")
    for dorsal in suplentes:
        print(f"{dorsal}\t{suplentes[dorsal]}")

   
def crear_plantilla(titulares,suplentes):
    plantilla = titulares
    plantilla.update(suplentes)


    print("\nPlantilla actualizada:")
    print("Dorsal\tNombre")
    print("------\t------")
    for dorsal in sorted(plantilla):
        print(f"{dorsal}\t{plantilla[dorsal]}")


def main():

    titulares = {
        1: "Iker Casillas (Capitán)",
        15: "Sergio Ramos",
        3: "Gerard Piqué",
        5: "Carles Puyol",
        11: "Joan Capdevila",
        14: "Xabi Alonso",
        16: "Sergio Busquets",
        8: "Xavi Hernández",
        18: "Pedro Rodríguez",
        6: "Andrés Iniesta",
        7: "David Villa"
    }

    suplentes = {
        4:  "Reina",
        21: "Víctor Valdés",
        12: "David Silva",
        23: "Fernando Torres"
    
        }

# Menú principal
    while True:
        print("\nMenú:")
        print("1. Mostrar de menor a mayor jugadores por dorsal")
        print("2. Mostrar nº titutales")
        print("3. Mostrar índices y valores de titulares")
        print("4. Mostrar suplentes")
        print("5. Mostrar plantilla completa")
        print("6. Salir del programa.")

        opcion = int(input("Introduce la opción deseada: "))

        if opcion == 1:
            mostrar_jugadores(titulares)
            input("Pulse Intro para continuar...")
        elif opcion == 2:
            num_titulares(titulares)
            input("Pulse Intro para continuar...")
        elif opcion == 3:
            mostrar_info(titulares)
            input("Pulse Intro para continuar...")
        elif opcion == 4:
            mostrar_suplentes(suplentes)
            input("Pulse Intro para continuar...")
        elif opcion == 5:
            crear_plantilla(titulares,suplentes)
            input("Pulse Intro para continuar...")
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")
            input("Pulse Intro para continuar...")


# Llamar a la función principal
if __name__ == "__main__":
    main()
