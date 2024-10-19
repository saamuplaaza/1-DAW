# -----------------------------------------------
#   Nombre:Samuel Plaza Sáez
#   Curso: 1º DAW
#   Título: PRÁCTICA EXAMEN: ÁRBOL DE NAVIDAD
# -----------------------------------------------
import os

while True:
    os.system("cls")
    print("Vamos a hacer un árbol de Navidad, para ello necesitamos saber la altura que va a tener.")
    try: # Nos aseguramos de que lo que introduce el usuario es un número.
        numero = int(input("Introduce un número: "))
        os.system("cls")
    except ValueError:
        print("Lo siento, ese número no es válido.")
        os.system("cls")

    else:
        asteriscos=1
        numEspacios=numero-1
        numAsteriscos=1
        while asteriscos <=numero:
            print(" "*(numEspacios)+"*"*numAsteriscos)
            asteriscos+=1
            numAsteriscos+=2
            numEspacios-=1
    print("¡¡¡FELIZ NAVIDAD!!!")
    input("Pulsa Intro para continuar...")
