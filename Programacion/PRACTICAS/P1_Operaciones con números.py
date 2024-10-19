# -----------------------------------------------
#   Nombre:Samuel Plaza Sáez
#   Curso: 1º DAW
#   Título: PRÁCTICA 1: OPERACIONES CON NÚMEROS
# -----------------------------------------------


# Definición de funciones.
def sumar(resultadoSuma,listaSuma):
    # Recorrer listaSuma y vamos sumando cada valor a los anteriores.
    for numero in listaSuma:
        resultadoSuma+=numero
    return resultadoSuma

def restar(lista1Resta, lista2Resta, resultadoResta):
    i=0
    while i<len(lista1Resta):
        # En resultadoResta añadimos el resultado de restar el primer valor de la primera lista y el primer valor de la segunda lista.
        resultadoResta.append(lista1Resta[i]-lista2Resta[i])
        resultadoResta[i]
        i+=1
    return resultadoResta

def multiplicar(numeroMult,resultadoMult):
    i=0
    while i<=10:
        # Vamos multiplicando el número introducido por el usuario por la variable i, la cual va incrementando en 1 hasta llegar a 10.
        resultadoMult=numeroMult*i
        print("%s x %s = %s"%(numeroMult,i,resultadoMult))
        i+=1


def esPrimo1(numDiv1):
    # Un número primo solo es divisible por 1 y por él mismo. Si al dividir por otro número el resto es 0, no es primo.
    # Para saber si es primo recorremos el número desde el 2 hasta uno menos que él.
    for i in range(2,int(numDiv1-1)):
        if (numDiv1%i)==0:
            return False

def esPrimo2(numDiv2):
    # Un número primo solo es divisible por 1 y por él mismo. Si al dividir por otro número el resto es 0, no es primo.
    # Para saber si es primo recorremos el número desde el 2 hasta uno menos que él.
    for i in range(2,int(numDiv2-1)):
        if (numDiv2%i)==0:
            return False

def dividir(numDiv1,numDiv2):
    # Solo se hace la división si el resto es cero.
    if numDiv1%numDiv2==0:
        # Al no haber resto, hacemos la división para que nos de la parte entera del resultado.
        resultadoDiv=numDiv1//numDiv2
        return resultadoDiv


# Variables para la suma.
listaSuma=[]
resultadoSuma=0

# Variables para la resta.
lista1Resta=[]
lista2Resta=[]
resultadoResta=[]

# Variables para la multiplicación.
numeroMult=0
resultadoMult=0

# Variables para la división.
numDiv1=0
numDiv2=0
resultadoDiv=0

# Código principal
while True:
    print("""
.______    __                  ______   .______    _______ .______          ___       ______  __    ______   .__   __.  _______     _______.
|   _  \  /_ |                /  __  \  |   _  \  |   ____||   _  \        /   \     /      ||  |  /  __  \  |  \ |  | |   ____|   /       |
|  |_)  |  | |     ______    |  |  |  | |  |_)  | |  |__   |  |_)  |      /  ^  \   |  ,----'|  | |  |  |  | |   \|  | |  |__     |   (----`
|   ___/   | |    |______|   |  |  |  | |   ___/  |   __|  |      /      /  /_\  \  |  |     |  | |  |  |  | |  . `  | |   __|     \   \    
|  |       | |               |  `--'  | |  |      |  |____ |  |\  \----./  _____  \ |  `----.|  | |  `--'  | |  |\   | |  |____.----)   |   
| _|       |_|                \______/  | _|      |_______|| _| `._____/__/     \__\ \______||__|  \______/  |__| \__| |_______|_______/    
                                                                                                                                            
  ______   ______   .__   __.    .__   __.  __    __  .___  ___.  _______ .______        ______        _______.                             
 /      | /  __  \  |  \ |  |    |  \ |  | |  |  |  | |   \/   | |   ____||   _  \      /  __  \      /       |                             
|  ,----'|  |  |  | |   \|  |    |   \|  | |  |  |  | |  \  /  | |  |__   |  |_)  |    |  |  |  |    |   (----`                             
|  |     |  |  |  | |  . `  |    |  . `  | |  |  |  | |  |\/|  | |   __|  |      /     |  |  |  |     \   \                                 
|  `----.|  `--'  | |  |\   |    |  |\   | |  `--'  | |  |  |  | |  |____ |  |\  \----.|  `--'  | .----)   |                                
 \______| \______/  |__| \__|    |__| \__|  \______/  |__|  |__| |_______|| _| `._____| \______/  |_______/                                 
                                                                                                                                            
""")
    print("----------------------------------------------MENU---------------------------------------------------------\n")
    print("\t1. Sumar\n")
    print("\t2. Restar\n")
    print("\t3. Multiplicar\n")
    print("\t4. Dividir\n")
    print("\t0. Salir")
    print("-----------------------------------------------------------------------------------------------------------\n")
    opcion=input("Elija una opción: ")
    print("-----------------------------------------------------------------------------------------------------------\n")

    # Para todas las opciones vamos a hacer un control de errores. Si el usuario no introduce un número, el programa le advierte y se lo pide otra vez.
    if opcion=="1":# Opción de sumar
        while True:
            try:
                numeros=float(input("Introduzca un número: "))
            except ValueError:
                print("El dato introducido no es válido para hacer operaciones.")
            else:
                # Se añaden número hasta introducir uno negativo.
                if numeros<0:
                    break
                listaSuma.append(numeros)
        suma= sumar(resultadoSuma,listaSuma)
        print("El resultado es: %s"%(suma))
        listaSuma=[]
        resultadoSuma=0
        print("-----------------------------------------------------------------------------------------------------------\n")
        input("Pulse Intro para continuar...")

    if opcion=="2": # Opción de restar
        while True:
            try:
                # Se pide la longitud de las listas.
                longitudListas=int(input("Introduzca la longitud de las listas: "))
            except ValueError:
                print("El dato introducido no es válido para hacer operaciones.")
            else:
                i=0
                # Los dos siguientes while son para introducir tantos números como se haya indicado anteriormente en longitudListas.
                while i<longitudListas:
                    try:
                        numerosLista1=float(input("Introduzca un número para la lista 1: "))
                    except ValueError:
                        print("El dato introducido no es válido para hacer operaciones.")
                    else:
                        lista1Resta.append(numerosLista1)
                        i+=1
                i=0
                while i<longitudListas:
                    try:
                        numerosLista2=float(input("Introduzca un número para la lista 2: "))
                    except ValueError:
                        print("El dato introducido no es válido para hacer operaciones.")
                    else:
                        lista2Resta.append(numerosLista2)
                        i+=1
                resta=restar(lista1Resta, lista2Resta, resultadoResta)
                print("El resultado de restar las dos listas es:\n%s" %(resta))
                lista1Resta=[]
                lista2Resta=[]
                resultadoResta=[]
                print("-----------------------------------------------------------------------------------------------------------\n")
                input("Pulse Intro para continuar...")
                break

    if opcion=="3": # Opción de multiplicar
        while True:
            try:
                numeroMult=float(input("Introduzaca un número: "))
            except ValueError:
                print("El dato introducido no es válido para hacer operaciones.")
            else:
                multiplicar(numeroMult,resultadoMult)
                break
        print("-----------------------------------------------------------------------------------------------------------\n")
        input("Pulse Intro para continuar...")

    if opcion=="4": # Opción de dividir
        print("Para poder hacer la división, el resto deberá ser 0. Sino, la división no se llevará acabo.\n")
        # Los dos siguientes while True piden un número al usuario y comprueba si son primos o no.
        while True:
            try:
                numDiv1=int(input("Introduzaca el primer número: "))
            except ValueError:
                print("El dato introducido no es válido para hacer operaciones.")
            else:
                primo1=esPrimo1(numDiv1)
                if primo1==True:
                    print("(El %s sí es un número primo.)\n"%(numDiv1))
                else:
                    print("(El %s no es un número primo.)\n"%(numDiv1))
                break
        while True:
            try:
                numDiv2=int(input("Introduzca el segundo número: "))
            except ValueError:
                print("El dato introducido no es válido para hacer operaciones.")
            else:
                primo2=esPrimo2(numDiv2)
                if primo2==True:
                    print("(El %s sí es un número primo.)\n"%(numDiv2))
                else:
                    print("(El %s no es un número primo.)\n"%(numDiv2))
                break
        # Creamos una condición por si el dividendo (segundo número) es 0, ya que no se puede dividir entre 0.
        if numDiv2==0:
            print("El divisor no puede ser 0.")
            print("-----------------------------------------------------------------------------------------------------------\n")
            input("Pulse Intro para continuar...")
        else:
            division=dividir(numDiv1, numDiv2)
            if division!=None:
                print("El resultado de la división es: %s"%(division))
                numDiv1=0
                numDiv2=0
                resultadoDiv=0
                print("-----------------------------------------------------------------------------------------------------------\n")
                input("Pulse Intro para continuar...")
            else:
                # Si la función 'dividir' no devuelve nada, no se ha realizado la división, lo que significa que el resto no era 0.
                print("(Para hacer la división el resto debe ser 0)")
                numDiv1=0
                numDiv2=0
                resultadoDiv=0
                print("-----------------------------------------------------------------------------------------------------------\n")
                input("Pulse Intro para continuar...")
    if opcion=="0": # Opción de salir, usar break para no seguir repitiendo el menú.
        break
    else:
        print("Opción no disponible.")