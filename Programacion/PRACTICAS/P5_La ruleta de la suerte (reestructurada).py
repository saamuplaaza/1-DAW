# -----------------------------------------------
#   Nombre:Samuel Plaza Sáez
#   Curso: 1º DAW
#   Título: PRÁCTICA 5: LA RULETA DE LA SUERTE (reestructurada)
# -----------------------------------------------

import random
import os

# Variables Globales
opcionesRuleta = [50, 25, 50, 0, 75, 25, 100, "x2", "QUIEBRA", "PIERDE TURNO"]
dineroTotalJugadores = []

# Definir funciones

def crearJuego(panel, numeroJugadores, dineroTotalJugadores):
    # La frase del panel no se puede quedar vacío.
    if panel=="":
        return False
    else:
        try:
            numeroJugadores=int(numeroJugadores)
        except ValueError:
            return False
        else:
            if numeroJugadores==0:
                return False
            else:
                i = 0
                # Añadimos a la lista de dinero total tantos elementos como jugadores haya. 
                # Todos los jugadores empiezan con 0€.
                while i <numeroJugadores:
                    dineroTotalJugadores.append(0)
                    i+= 1
                # Guardamos los datos de los jugadores en un diccionario.
                dicJugadores = {}
                i = 1
                j = 0
                while i<=numeroJugadores:
                    nombreJugador = input("Nombre del jugador %s: " %i)
                    nombreJugador = nombreJugador.capitalize()
                    try:
                        edadJugador = int(input("Edad del jugador %s: " %i))
                    except ValueError:
                        print("Introduce un número entero.")
                    else:
                        dicJugadores ["Jugador %s" % i] = [nombreJugador, edadJugador, dineroTotalJugadores[j]]
                        i+= 1
                        j+= 1
                return dicJugadores

def mostrarMenuUI(numeroJugador, fraseResuelta):
    os.system("cls")
    print("""
     __          ___         .______       __    __   __       _______ .___________.    ___         
    |  |        /   \        |   _  \     |  |  |  | |  |     |   ____||           |   /   \        
    |  |       /  ^  \       |  |_)  |    |  |  |  | |  |     |  |__   `---|  |----`  /  ^  \       
    |  |      /  /_\  \      |      /     |  |  |  | |  |     |   __|      |  |      /  /_\  \      
    |  `----./  _____  \     |  |\  \----.|  `--'  | |  `----.|  |____     |  |     /  _____  \     
    |_______/__/     \__\    | _| `._____| \______/  |_______||_______|    |__|    /__/     \__\    
                                                                                                                                
_______   _______     __          ___              _______. __    __   _______ .______     .___________. _______               
|       \ |   ____|   |  |        /   \            /       ||  |  |  | |   ____||   _  \    |           ||   ____|              
|  .--.  ||  |__      |  |       /  ^  \          |   (----`|  |  |  | |  |__   |  |_)  |   `---|  |----`|  |__                 
|  |  |  ||   __|     |  |      /  /_\  \          \   \    |  |  |  | |   __|  |      /        |  |     |   __|                
|  '--'  ||  |____    |  `----./  _____  \     .----)   |   |  `--'  | |  |____ |  |\  \----.   |  |     |  |____               
|_______/ |_______|   |_______/__/     \__\    |_______/     \______/  |_______|| _| `._____|   |__|     |_______|              
                                                                            
""")
    print("-----------------------------------------------------------------------------------------------------------\n")
    print(fraseResuelta[0])
    print(pista)
    print("\n------------------------------------------------MENÚ-------------------------------------------------------\n")
    print("-----------------------------------------JUGADOR %s: %s ---------------------------------------------\n" %(numeroJugador, nombreJugador))
    print("Total: %s€\n\n" %dineroTotalJugadores[numeroJugador - 1])
    print("\t1. Decir letra\n")
    print("\t2. Comprar vocal (10€)\n")
    print("\t3. Resolver\n")
    print("\t4. Rendirme\n")
    print("-----------------------------------------------------------------------------------------------------------")
    opcion=input("Elija una opción: ")
    print("-----------------------------------------------------------------------------------------------------------\n")
    return opcion

def tirarRuleta():
    valorRuleta=random.choice(opcionesRuleta)
    return valorRuleta

def quitarTilde(panel):
    i=0
    listaSinTilde=list(panel)
    for letra in listaSinTilde:
        if letra =="Á":
            listaSinTilde[i]="A"
        elif letra=="É":
            listaSinTilde[i]="E"
        elif letra=="Í":
            listaSinTilde[i]="I"
        elif letra=="Ó":
            listaSinTilde[i]="O"
        elif letra=="Ú":
            listaSinTilde[i]="U"
        i+=1
    fraseSinTilde="".join(listaSinTilde)
    return fraseSinTilde

def quitarTildeRespuesta(respuesta):
    i=0
    listaRespuesta=list(respuesta)
    for letra in listaRespuesta:
        if letra =="Á":
            listaRespuesta[i]="A"
        elif letra=="É":
            listaRespuesta[i]="E"
        elif letra=="Í":
            listaRespuesta[i]="I"
        elif letra=="Ó":
            listaRespuesta[i]="O"
        elif letra=="Ú":
            listaRespuesta[i]="U"
        i+=1
    respuestaSinTilde="".join(listaRespuesta)
    return respuestaSinTilde

def limpiarFrase(fraseSinTilde):
    fraseLimpia=""
    for letra in fraseSinTilde:
        # En la tabla ASCII las letras mayúsculas van del 65 al 90.
        # Esta función todo lo que no sean letras, números o \n lo reemplaza por espacios.
        #  Así conseguimos limpiarlo de otros caracteres.
        if (ord(letra) >= 65 and ord (letra) <= 90) or letra=="Ñ":
            letra=letra
        else:
            letra=letra.replace(letra, " ")
        fraseLimpia=fraseLimpia+letra
    return fraseLimpia

def comprobarLetra(letra):
    consonantes= "BCDFGHJKLMNÑPQRSTVWXYZ"
    vocales = "AEIOU"
    letra = letra.upper()
    if letra in consonantes:
        return 1 # Es consonante.
    elif letra in vocales:
        return 0 # Es vocal.
    else:
        return -1 # No ha introducido letra válida.

def existeLetra(letra, panel, listaLetras):
    letra = letra.upper()
    if letra in listaLetras:
        return -1 # Ya la has dicho.
    elif letra in panel:
        return 1 # Sí existe en el panel y no la has dicho todavía.
    else:
        return 0 # No existe en el panel y no la has dicho todavía.

def actualizaPanel( panel, listaLetras):
    i=0
    contador=0
    listaAsteriscos=list(panel)
    listaSinTilde=quitarTilde(panel)
    while i<len(listaAsteriscos):
        if listaLetras==[]: # Para la primera vez que entra en la función, no hay lista con consonantes, por lo que creamos esta condición.
            if (ord(listaSinTilde[i])>=65 and ord(listaSinTilde[i])<=122) or listaSinTilde[i]=="Ñ":
                listaAsteriscos[i]="*"
            i+=1
            
        else: # Para el resto de condiciones hacemos el siguiente código
            for caracter in listaSinTilde:
                # Consultamos la tabla ASCII para saber cual es el número asociado de las vocales y consonantes. (min: 65, max: 90)
                if (ord(caracter)>=65 and ord(caracter)<=90) or listaSinTilde[i]=="Ñ":
                    if listaSinTilde [i] in listaLetras: # Para las letras que se encuentren en la lista, las dejamos iguales y aumentamos el contador.
                        if listaSinTilde[i]== listaLetras[-1]:
                            contador+=1
                    else: # Para el resto, las convertimos a asteriscos.
                        listaAsteriscos[i]=listaAsteriscos[i]
                        listaAsteriscos[i]="*"
                i+=1
                fraseConsonantes="".join(listaAsteriscos)
    fraseConsonantes="".join(listaAsteriscos)
    return fraseConsonantes, contador, listaSinTilde

def actualizarTotal(tiradaRuleta, dineroTotalJugadores, numeroJugador, fraseResuelta):
    # Si entra en la opcion 2 significa que tiene que meter una vocal, por lo que restamos 10 al total.
    if opcionMenu == "2":
        dineroTotalJugadores[numeroJugador-1] -= 10
    else:
        if isinstance(tiradaRuleta, int):
            dineroTotalJugadores[numeroJugador-1]+=tiradaRuleta*fraseResuelta[1]
        elif tiradaRuleta == "x2":
            dineroTotalJugadores[numeroJugador-1]*=2
        elif tiradaRuleta == "QUIEBRA":
            dineroTotalJugadores[numeroJugador-1]=0
    return dineroTotalJugadores

def limpiarRespuesta(respuestaSinTilde):
    respuestaLimpia=""
    for letra in respuestaSinTilde:
        # En la tabla ASCII las letras minúsculas van del 97 al 122.
        # Esta función todo lo que no sean letras, números o \n lo reemplaza por espacios.
        #  Así conseguimos limpiarlo de otros caracteres.
        if (ord(letra) >= 65 and ord (letra) <= 90) or letra=="Ñ":
            letra=letra
        else:
            letra=letra.replace(letra, " ")
        respuestaLimpia = respuestaLimpia+letra
    return respuestaLimpia 

def cambiarTurno(numeroJugadores, numeroJugador):
    numeroJugador+=1
    if numeroJugador > numeroJugadores:
        numeroJugador = 1
    return numeroJugador

def esSolucion():
    frase=limpiarFrase(fraseSinTilde)
    frase=frase.split()
    respuestaSinTilde=quitarTildeRespuesta(respuesta)
    solucionLimpia=limpiarRespuesta(respuestaSinTilde)
    solucionLimpia=solucionLimpia.split()
    return frase, solucionLimpia

# Código principal
os.system("cls")
print("\nVamos a jugar a la Ruleta de la Suerte pero, antes de empezar, hay que introducir la pista del panel y el panel a resolver.")
pista=input("Introducir una pista: ")
pista= pista.upper()
panel=input("Introducir una frase: ")
panel= panel.upper()
numeroJugador = 1
listaLetras=[]
try:
    numeroJugadores= int(input("Número de jugadores: "))
except ValueError:
    print("Introduce un número entero.")
else:
    juego = crearJuego(panel, numeroJugadores, dineroTotalJugadores)
    os.system("cls")
    while True:
        nombreJugador = juego["Jugador %s" %numeroJugador][0]
        # Para la primera vez, primero actualizamos el panel y luego mostramos el menú,
        # sino nos dará error, ya que en ningún momento hemos entrado en la funcion actualizarPanel.
        # No pongo la funcion actualizarPanerl dentro de la funcion mostrarMenuUI porque sino voy a estar repitiendo código en las demas opciones del menú, 
        # ya que actualizo el panel al final de cada una de ellas.
        if listaLetras==[]:
            fraseResuelta=actualizaPanel( panel, listaLetras)
            fraseSinTilde = fraseResuelta[2]
            opcionMenu = mostrarMenuUI(numeroJugador, fraseResuelta)
        else:
            opcionMenu = mostrarMenuUI(numeroJugador, fraseResuelta)

        if opcionMenu == "":
            print("Debes elegir una de las opciones del menú.")
            input("Pulsa Intro para continuar...")
        elif opcionMenu == "1": # Decir consonante
            tiradaRuleta = tirarRuleta()
            try:
                (tiradaRuleta =="x2") or (tiradaRuleta == int(tiradaRuleta)) 
                if tiradaRuleta=="x2":
                    print("--> %s" %tiradaRuleta)
                else:
                    print("--> %s€" %(tiradaRuleta))
            except:
                print("--> %s" %tiradaRuleta)
                actualizarTotal(tiradaRuleta, dineroTotalJugadores, numeroJugador, fraseResuelta)
                numeroJugador = cambiarTurno(numeroJugadores, numeroJugador)
                input("Pulsa Intro para continuar...")
            else:
                while True:
                    letra = input("Introduce una consonante: ")
                    if len(letra) != 1 or comprobarLetra(letra)!=1:
                        print("Error: Solo puedes introducir una consonante.")
                        input("Pulsa Intro para continuar...")
                    elif comprobarLetra(letra)==1:
                        if existeLetra(letra, panel, listaLetras)==1:
                            listaLetras.append(letra.upper())
                            fraseResuelta = actualizaPanel( panel, listaLetras)
                            if fraseResuelta[1]==1:
                                print("La consonante '%s' se encuentra %s vez en el panel." %(letra.upper(), fraseResuelta[1]))
                            else:
                                print("La consonante '%s' se encuentra %s veces en el panel." %(letra.upper(), fraseResuelta[1]))
                            actualizarTotal(tiradaRuleta, dineroTotalJugadores, numeroJugador, fraseResuelta)
                            input("Pulsa Intro para continuar...")
                        elif existeLetra(letra, panel, listaLetras)==0:
                            listaLetras.append(letra.upper())
                            print("La letra no se encuentra en el panel.")
                            input("Pulsa Intro para continuar...")
                            numeroJugador = cambiarTurno(numeroJugadores, numeroJugador)
                        else:
                            print("Esta letra ya se ha intentado usar.")
                            input("Pulsa Intro para continuar...")
                            numeroJugador = cambiarTurno(numeroJugadores, numeroJugador)
                        break
        elif opcionMenu == "2": # Comprar vocal
            if dineroTotalJugadores[numeroJugador - 1] < 10:
                print("Necesitas al menos 10€ para comprar una vocal.")
                input("Pulsa Intro para continuar...")
            else:
                letra = input("Introduce una vocal: ")
                if len(letra) != 1 or comprobarLetra(letra)!=0:
                    print("Error: Solo puedes introducir una vocal.")
                    input("Pulsa Intro para continuar...")
                elif comprobarLetra(letra) == 0:
                    if existeLetra(letra, panel, listaLetras) == 1:
                        listaLetras.append(letra.upper())
                        fraseResuelta = actualizaPanel( panel, listaLetras)
                        if fraseResuelta[1]==1:
                            print("La vocal '%s' se encuentra %s vez en el panel." %(letra.upper(), fraseResuelta[1]))
                        else:
                            print("La vocal '%s' se encuentra %s veces en el panel." %(letra.upper(), fraseResuelta[1]))
                        actualizarTotal(tiradaRuleta, dineroTotalJugadores, numeroJugador, fraseResuelta)
                        input("Pulsa Intro para continuar...")
                    elif existeLetra(letra, panel, listaLetras)==0:
                        listaLetras.append(letra.upper())
                        print("La letra no se encuentra en el panel.")
                        input("Pulsa Intro para continuar...")
                        numeroJugador = cambiarTurno(numeroJugadores, numeroJugador)
                    else:
                        print("Esta letra ya se ha intentado usar.")
                        input("Pulsa Intro para continuar...")
                        numeroJugador = cambiarTurno(numeroJugadores, numeroJugador)
        elif opcionMenu == "3": # Resolver
            respuesta = input("Solución: ")
            respuesta = respuesta.upper()
            solucion = esSolucion()
            if solucion[0] == solucion[1]: 
                # Habíamos creado una lista en la función de la solución. Ahora compramos los elementos de dicha lista. 
                #Si los dos elementos son iguales, significa que la respuesta es correcta.
                print('''
    _______ _______ _______ _______ ______ _______ ______ _______ _______ _______ _______ 
    |    ___|    |  |   |   |       |   __ \   _   |   __ \   |   |    ___|    |  |   _   |
    |    ___|       |       |   -   |      <       |   __ <   |   |    ___|       |       |
    |_______|__|____|___|___|_______|___|__|___|___|______/_______|_______|__|____|___|___|
                                                                                        
    _______ _______ _______      _______ _______ _______ _______ _____  _______           
    |   |   |   _   |     __|    |     __|   _   |    |  |   _   |     \|       |          
    |       |       |__     |    |    |  |       |       |       |  --  |   -   |          
    |___|___|___|___|_______|    |_______|___|___|__|____|___|___|_____/|_______|          
                                                                                                
                ''')
                print("%s ha ganado un total de %s€\n" %(nombreJugador, dineroTotalJugadores[numeroJugador-1]))
                break
            else:
                print("Esa no es la solución.")
                numeroJugador = cambiarTurno(numeroJugadores, numeroJugador)
                input("Pulsa Intro para continuar...")
        elif opcionMenu=="4": # Rendirme
            break
        else:
            print("Elije una de las opciones del menú.")
            input("Pulsa Intro para continuar...")