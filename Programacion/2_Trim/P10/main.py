import P1_OperacionesConNumeros as funcNum
import P2_Palabras as funcCad
import os

def mostrarMenuUI():
    print("""
.______    __    ___                 .______   .______        ______     _______ .______          ___      .___  ___.      ___       ______  __    ______   .__   __.    
|   _  \  /_ |  / _ \                |   _  \  |   _  \      /  __  \   /  _____||   _  \        /   \     |   \/   |     /   \     /      ||  |  /  __  \  |  \ |  |    
|  |_)  |  | | | | | |     ______    |  |_)  | |  |_)  |    |  |  |  | |  |  __  |  |_)  |      /  ^  \    |  \  /  |    /  ^  \   |  ,----'|  | |  |  |  | |   \|  |    
|   ___/   | | | | | |    |______|   |   ___/  |      /     |  |  |  | |  | |_ | |      /      /  /_\  \   |  |\/|  |   /  /_\  \  |  |     |  | |  |  |  | |  . `  |    
|  |       | | | |_| |               |  |      |  |\  \----.|  `--'  | |  |__| | |  |\  \----./  _____  \  |  |  |  |  /  _____  \ |  `----.|  | |  `--'  | |  |\   |    
| _|       |_|  \___/                | _|      | _| `._____| \______/   \______| | _| `._____/__/     \__\ |__|  |__| /__/     \__\ \______||__|  \______/  |__| \__|    
                                                                                                                                                                         
.___  ___.   ______    _______   __    __   __          ___      .______                                                                                                 
|   \/   |  /  __  \  |       \ |  |  |  | |  |        /   \     |   _  \                                                                                                
|  \  /  | |  |  |  | |  .--.  ||  |  |  | |  |       /  ^  \    |  |_)  |                                                                                               
|  |\/|  | |  |  |  | |  |  |  ||  |  |  | |  |      /  /_\  \   |      /                                                                                                
|  |  |  | |  `--'  | |  '--'  ||  `--'  | |  `----./  _____  \  |  |\  \----.                                                                                           
|__|  |__|  \______/  |_______/  \______/  |_______/__/     \__\ | _| `._____|                                                                                           
                                                                                                                                                                         
          """)
    print("----------------------------------------------MENU---------------------------------------------------------\n")
    print("\t1. Sumar\n")
    print("\t2. Restar\n")
    print("\t3. Multiplicar\n")
    print("\t4. Dividir\n")
    print("\t5. Encontrar palabra\n")
    print("\t6. Conteo de palabras\n")
    print("\t7. Cambiar vocal\n")
    print("\t8. Palíndromo\n")
    print("\t0. Salir")
    print("-----------------------------------------------------------------------------------------------------------\n")
    opcion=input("Elija una opción: ")
    print("-----------------------------------------------------------------------------------------------------------\n")
    return opcion

if __name__ == "__main__":
    listaLimpia = ""
    while True:
        opcionMenu = mostrarMenuUI()
        if opcionMenu == "":
            print("Debe elegir una de las opciones del menú.")
            input("Pulse cualquier tecla para continuar...")
        
        elif opcionMenu=="1":# Opción de sumar
            listaSuma = []
            while True:
                while True:
                    numeros=input("Introduzca un número: ")
                    if numeros.isnumeric() == True:
                        numeros = int(numeros)
                        if numeros>0:
                            listaSuma.append(numeros)
                        elif numeros == 0:
                            break
                    else:
                        print("El dato introducido no es válido para hacer operaciones.")
                        input("Pulse Intro para continuar...")
                        break 
                suma= funcNum.sumar(listaSuma)
                print(f"El resultado de la suma es {suma}.")
                input("Pulse Intro para continuar...")
                os.system("cls")
                break 

        elif opcionMenu=="2": # Opción de restar
            while True:
                while True:
                    lista1Resta=[]
                    # Se pide la longitud de las listas.
                    longitudListas=input("Introduzca la longitud de las listas: ")
                    if  longitudListas.isdigit() == True:
                        longitudListas=int(longitudListas)
                        for i in range(longitudListas):
                            numerosLista1=input("Introduzca un número para la lista 1: ")
                            if numerosLista1.isnumeric() == True:
                                numerosLista1 = int(numerosLista1)
                                lista1Resta.append(numerosLista1)
                            else:
                                print("El dato introducido no es válido para hacer operaciones.")
                                input("Pulse cualquier tecla para continuar...")
                                os.system("cls")
                                break
                        if len(lista1Resta) != longitudListas:
                            break
                        else:
                            lista2Resta=[]
                            for i in range(longitudListas):
                                numerosLista2=input("Introduzca un número para la lista 2: ")
                                if numerosLista2.isnumeric() == True:
                                    numerosLista2 = int(numerosLista2)
                                    lista2Resta.append(numerosLista2)
                                else:
                                    print("El dato introducido no es válido para hacer operaciones.")
                                    input("Pulse cualquier tecla para continuar...")
                                    os.system("cls")
                                    break
                            if len(lista2Resta)!= longitudListas:
                                break
                    else:
                        print("El dato introducido no es válido para hacer operaciones.")
                        input("Pulse Intro para continuar...")
                        os.system("cls")
                        break
                    resta=funcNum.restar(lista1Resta, lista2Resta)
                    print("El resultado de restar las dos listas es:\n%s" %(resta))
                    print("-----------------------------------------------------------------------------------------------------------\n")
                    input("Pulse Intro para continuar...")
                    os.system("cls")
                    break
                if len(lista1Resta) != longitudListas or len(lista2Resta) != longitudListas:
                    pass
                else:
                    break

        elif opcionMenu=="3": # Opción de multiplicar
            while True:
                numeroMult=input("Introduzaca un número: ")
                if numeroMult.isnumeric()==True:
                    numeroMult = int(numeroMult)
                    print(f"Aquí tienes la tabla del {numeroMult}:")
                    mult = funcNum.multiplicar(numeroMult)
                    input("Pulse Intro para continuar...")
                    os.system("cls")
                    break
                else:
                    print("El dato introducido no es válido para hacer operaciones.")
                    input("Pulse Intro para continuar...")
                os.system("cls")     

        elif opcionMenu=="4": # Opción de dividir
            print("Para poder hacer la división, el resto deberá ser 0. Sino, la división no se llevará acabo.\n")
            # Los dos siguientes while True piden un número al usuario y comprueba si son primos o no.
            while True:
                while True:
                    while True:
                        dividendo=input("Introduzaca el primer número: ")
                        if dividendo.isdigit() == True:
                            dividendo = int(dividendo)
                            primo1=funcNum.esPrimo(dividendo)
                            if primo1==False:
                                print("(El %s no es un número primo.)\n"%(dividendo))
                                break
                            else:
                                print("(El %s sí es un número primo.)\n"%(dividendo))
                                break
                        else:
                            print("El dato introducido no es válido para hacer operaciones.")
                            input("Pulse Intro para continuar...")
                            os.system("cls")
                            break
                        
                    if isinstance(dividendo, str):
                        break
                    else:
                        while True:
                            divisor=input("Introduzca el segundo número: ")
                            if  divisor.isdigit() == True:
                                divisor = int(divisor)
                                if divisor <= 0:
                                    print("No puede dividor entre 0.")
                                    input("Pulse Intro para continuar...")
                                else:
                                    primo2=funcNum.esPrimo(divisor)
                                    if primo2==False:
                                        print("(El %s no es un número primo.)\n"%(divisor))
                                        break
                                    else:
                                        print("(El %s sí es un número primo.)\n"%(divisor))
                                        break
                            else:
                                print("El dato introducido no es válido para hacer operaciones.")
                                input("Pulse Intro para continuar...")
                                os.system("cls")
                                                    
                    division=funcNum.dividir(dividendo, divisor)
                    if division!=None:
                        print("El resultado de la división es: %s"%(division))
                        input("Pulse Intro para continuar...")
                        break
                    else:
                        # Si la función 'dividir' no devuelve nada, no se ha realizado la división, lo que significa que el resto no era 0.
                        print("(Para hacer la división el resto debe ser 0)")
                        input("Pulse Intro para continuar...")
                        os.system("cls")
                if division != None:
                    break
        
        elif opcionMenu == "5" or opcionMenu == "6": # Encontrar palabra
            try:
                archivo=input("Introduzca el nombre del fichero (extenión incluida): ")
                abrirArchivo=open(archivo,"r", encoding="utf-8")
            except FileNotFoundError:
                print("Archivo no encontrado.")
                input("Pulse cualquier tecla para continuar...")
            else:
                leer=abrirArchivo.read()
                leer=leer.lower()
                sinTilde=funcCad.quitarTildeTexto(leer)
                if opcionMenu == "5": # Encontrar palabra
                    buscar=input("Palabra para buscar: ")
                    buscar=buscar.lower()
                    vecesRepetida=funcCad.vecesPalabra(buscar, listaLimpia, sinTilde)
                    print("\nVeces que se repite la palabra '%s' en el texto: %s"%(buscar,vecesRepetida))
                    print("\n(No se han tenido en cuenta mayúsculas, minúsculas o tildes)")
                    print("-----------------------------------------------------------------------------------------------------------\n")
                    input("Pulse cualquier tecla para continuar...")
                if opcionMenu == "6": # Conteo de palabras
                    # limpiar=funcCad.limpiarTexto(listaLimpia, sinTilde)
                    numPalabras=funcCad.contarPalabras(listaLimpia, sinTilde)
                    numCaracteres= funcCad.contarCaracteres(leer)
                    numeroLineas= funcCad.numLineas(leer)
                    print("\nNúmero de palabras: %s"%numPalabras)
                    print("Número de caracteres: %s"%numCaracteres)
                    print("Número de líneas: %s"%numeroLineas)
                    print("-----------------------------------------------------------------------------------------------------------\n")
                    input("Pulse cualquier tecla para continuar...")  
        
        elif opcionMenu == "7": # Cambiar vocal
            palabra=input("Introduzca una palabra: ")
            vocal=input("Introduzca una vocal: ")
            palabraSinTilde = funcCad.quitarTildePalabra(palabra)
            cambioVocal = funcCad.cambiarVocal(vocal, palabraSinTilde)
            print("\n"+cambioVocal)
            print("-----------------------------------------------------------------------------------------------------------\n")
            input("Pulse cualquier tecla para continuar...")
        
        elif opcionMenu == "8": # Palíndromo
            palabraPalindromo=input("Introduzca una palabra: ")
            palabraPalindromo=palabraPalindromo.lower()
            palindromo = funcCad.esPalindrimo(palabraPalindromo)
            if palindromo == True:
                print(f"{palabraPalindromo} sí es un palíndromo.")
                input("Pulse cualquier tecla para continuar...")
            else:
                print(f"{palabraPalindromo} no es un palíndromo.")
                input("Pulse cualquier tecla para continuar...")
            
        elif opcionMenu=="0": # Opción de salir, usar break para no seguir repitiendo el menú.
            break
        
        else:
            print("Opción no disponible.")