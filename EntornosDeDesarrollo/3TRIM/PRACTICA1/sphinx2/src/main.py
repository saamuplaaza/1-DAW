"""El archivo main.py contiene las funciones para realizar operaciones básicas con números enteros."""
from sumar import suma
from restar import resta
from multiplicar import multiplicacion
from dividir import division
import os

def menuUI():
    """Esta función es el menú de la aplicación
    Returns: 
        str: La opción elegida por el usuario.
    """
    print(
        """
        -----------MENÚ-------------
        \t1. Sumar
        \t2. Restar
        \t3. Multiplicar
        \t4. Dividir
        \t0. Salir
        ----------------------------"""
    )
    opcionMenu = input("Introduce una opción: ")
    return opcionMenu

def main(opcionMenu):
    """El código generado para llamar a las funciones y hacer las operaciones

    Args:
        opcionMenu (str): la opción seleccionada por el usuario.
    """
    
    if  opcionMenu == "1":
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        resultado = suma(num1, num2)
        print(f"El resultado de sumar {num1} y {num2} es: {resultado}")
        input("Pulse Enter para continuar...")
        
    elif opcionMenu == "2":
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        resultado = resta(num1, num2)
        print(f"El resultado de restar {num1} y {num2} es: {resultado}")
        input("Pulse Enter para continuar...")
        
    elif opcionMenu == "3":
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        resultado = multiplicacion(num1, num2)
        print(f"El resultado de multiplicar {num1} y {num2} es: {resultado}")
        input("Pulse Enter para continuar...")
        
    elif  opcionMenu == "4":
        num1 = int(input("Introduce el dividendo: "))
        while True:
            num2 = int(input("Introduce el divisor: "))
            if num2 != 0:
                break
            else:
                print("No se puede dividir entre 0")
        resultado = division(num1, num2)
        print(f"El resultado de dividir {num1} y {num2} es: {resultado}")
        input("Pulse Enter para continuar...")
        
        
if __name__ == "__main__":
    while True:
        opcion = menuUI()
        main(opcion)
        os.system("cls")