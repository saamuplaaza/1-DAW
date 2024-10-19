# -----------------------------------------------
#   Nombre:Samuel Plaza Sáez
#   Curso: 1º DAW
#   Título: PRÁCTICA 3: LA RULETA DE LA SUERTE
# -----------------------------------------------

# from multiprocessing import Value
import random
import os

# Definir funciones

def quitarTilde(panel, i):
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

def quitarTildeRespuesta(respuesta, i):
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

def cambiarConsonantes(i, acumulacionConsonantes, contador):
    listaAsteriscos=list(panel)
    listaSinTilde=quitarTilde(panel, i)
    while i<len(listaAsteriscos):
        if acumulacionConsonantes==[]: # Para la primera vez que entra en la función, no hay lista con consonantes, por lo que creamos esta condición.
            if (ord(listaSinTilde[i])>=65 and ord(listaSinTilde[i])<=122) or listaSinTilde[i]=="Ñ":
                listaAsteriscos[i]="*"
            i+=1
            
        else: # Para el resto de condiciones hacemos el siguiente código
            for caracter in listaSinTilde:
                # Consultamos la tabla ASCII para saber cual es el número asociado de las vocales y consonantes. (min: 65, max: 122)
                if (ord(caracter)>=65 and ord(caracter)<=122) or listaSinTilde[i]=="Ñ":
                    if listaSinTilde [i] in acumulacionConsonantes: # Para las letras que se encuentren en la lista, las dejamos iguales y aumentamos el contador.
                        if listaSinTilde[i]== acumulacionConsonantes[-1]:
                            contador+=1
                    else: # Para el resto, las convertimos a asteriscos.
                        listaAsteriscos[i]=listaAsteriscos[i]
                        listaAsteriscos[i]="*"
                i+=1
                fraseConsonantes="".join(listaAsteriscos)
    fraseConsonantes="".join(listaAsteriscos)
    return fraseConsonantes, contador, listaSinTilde

def limpiarFrase(fraseLimpia, fraseSinTilde):
    for letra in fraseSinTilde:
        # En la tabla ASCII las letras minúsculas van del 97 al 122.
        # Esta función todo lo que no sean letras, números o \n lo reemplaza por espacios.
        #  Así conseguimos limpiarlo de otros caracteres.
        if (ord(letra) >= 65 and ord (letra) <= 90) or letra=="Ñ":
            letra=letra
        else:
            letra=letra.replace(letra, " ")
        fraseLimpia=fraseLimpia+letra
    return fraseLimpia

def limpiarRespuesta(respuestaLimpia, respuestaSinTilde):
    for letra in respuestaSinTilde:
        # En la tabla ASCII las letras minúsculas van del 97 al 122.
        # Esta función todo lo que no sean letras, números o \n lo reemplaza por espacios.
        #  Así conseguimos limpiarlo de otros caracteres.
        if (ord(letra) >= 65 and ord (letra) <= 90) or letra=="Ñ":
            letra=letra
        else:
            letra=letra.replace(letra, " ")
        respuestaLimpia=respuestaLimpia+letra
    return respuestaLimpia 

def esSolucion():
    # Llama a distintas funciones para obtener una lista con la frase y la respuesta. 
    frase=limpiarFrase(fraseLimpia, fraseSinTilde)
    frase=frase.split()
    respuestaSinTilde=quitarTildeRespuesta(respuesta, i)
    solucionLimpia=limpiarRespuesta(respuestaLimpia, respuestaSinTilde)
    solucionLimpia=solucionLimpia.split()
    return frase, solucionLimpia


# Variables

contador=0
i=0
total=0
consonantes= "bcdfghjklmnñpqrstvwxyz"
consonantes=consonantes.upper()
vocales="aeiou"
vocales=vocales.upper()
acumulacionConsonantes=[]
dinero=0
opcionesRuleta=[50, 25, 75, 50, 0, 75, 25, 100, "x2", "QUIEBRA"]
ruleta=random.choice(opcionesRuleta)
fraseLimpia=""
respuestaLimpia=""


# Código principal
print("\nVamos a jugar a la Ruleta de la Suerte pero, antes de empezar, hay que introducir la pista del panel y el panel a resolver.")
pista=input("Introducir una pista: ")
pista= pista.upper()
panel=input("Introducir una frase: ")
panel= panel.upper()
os.system("cls")
print("""
.______    ____                  __          ___         .______       __    __   __       _______ .___________.    ___         
|   _  \  |___ \                |  |        /   \        |   _  \     |  |  |  | |  |     |   ____||           |   /   \        
|  |_)  |   __) |     ______    |  |       /  ^  \       |  |_)  |    |  |  |  | |  |     |  |__   `---|  |----`  /  ^  \       
|   ___/   |__ <     |______|   |  |      /  /_\  \      |      /     |  |  |  | |  |     |   __|      |  |      /  /_\  \      
|  |       ___) |               |  `----./  _____  \     |  |\  \----.|  `--'  | |  `----.|  |____     |  |     /  _____  \     
| _|      |____/                |_______/__/     \__\    | _| `._____| \______/  |_______||_______|    |__|    /__/     \__\    
                                                                                                                                
_______   _______     __          ___              _______. __    __   _______ .______     .___________. _______               
|       \ |   ____|   |  |        /   \            /       ||  |  |  | |   ____||   _  \    |           ||   ____|              
|  .--.  ||  |__      |  |       /  ^  \          |   (----`|  |  |  | |  |__   |  |_)  |   `---|  |----`|  |__                 
|  |  |  ||   __|     |  |      /  /_\  \          \   \    |  |  |  | |   __|  |      /        |  |     |   __|                
|  '--'  ||  |____    |  `----./  _____  \     .----)   |   |  `--'  | |  |____ |  |\  \----.   |  |     |  |____               
|_______/ |_______|   |_______/__/     \__\    |_______/     \______/  |_______|| _| `._____|   |__|     |_______|              
                                                                            
""")
input("Pulse Intro para continuar...")
fraseSinTilde= cambiarConsonantes(i, acumulacionConsonantes, contador)[2]
while True:
    os.system("cls")
    print("""
.______    ____                  __          ___         .______       __    __   __       _______ .___________.    ___         
|   _  \  |___ \                |  |        /   \        |   _  \     |  |  |  | |  |     |   ____||           |   /   \        
|  |_)  |   __) |     ______    |  |       /  ^  \       |  |_)  |    |  |  |  | |  |     |  |__   `---|  |----`  /  ^  \       
|   ___/   |__ <     |______|   |  |      /  /_\  \      |      /     |  |  |  | |  |     |   __|      |  |      /  /_\  \      
|  |       ___) |               |  `----./  _____  \     |  |\  \----.|  `--'  | |  `----.|  |____     |  |     /  _____  \     
| _|      |____/                |_______/__/     \__\    | _| `._____| \______/  |_______||_______|    |__|    /__/     \__\    
                                                                                                                                
_______   _______     __          ___              _______. __    __   _______ .______     .___________. _______               
|       \ |   ____|   |  |        /   \            /       ||  |  |  | |   ____||   _  \    |           ||   ____|              
|  .--.  ||  |__      |  |       /  ^  \          |   (----`|  |  |  | |  |__   |  |_)  |   `---|  |----`|  |__                 
|  |  |  ||   __|     |  |      /  /_\  \          \   \    |  |  |  | |   __|  |      /        |  |     |   __|                
|  '--'  ||  |____    |  `----./  _____  \     .----)   |   |  `--'  | |  |____ |  |\  \----.   |  |     |  |____               
|_______/ |_______|   |_______/__/     \__\    |_______/     \______/  |_______|| _| `._____|   |__|     |_______|              
                                                                            
""")
    print("-----------------------------------------------------------------------------------------------------------\n")
    fraseConsonantes=cambiarConsonantes(i, acumulacionConsonantes, contador)
    print(fraseConsonantes[0])
    print(pista)
    print("-----------------------------------------------------------------------------------------------------------\n")
    print("\n------------------------------------------------MENÚ-------------------------------------------------------\n")
    print("Total: %s€\n\n" %total)
    print("\t1. Decir letra\n")
    print("\t2. Comprar vocal (10€)\n")
    print("\t3. Resolver\n")
    print("\t4. Rendirme\n")
    print("-----------------------------------------------------------------------------------------------------------")
    opcion=input("Elija una opción: ")
    print("-----------------------------------------------------------------------------------------------------------\n")

    if opcion=="": # Introduce un Intro por teclado.
        print("Debes elegir una de las opciones del menú.")
        input("Pulsa Intro para continuar...")
    elif opcion=="1": # Decir letra
        ruleta=random.choice(opcionesRuleta) # La ruleta escoge un número aleatorio de los que hay en la lista 'opcionesRuleta'. Esta lista tiene 10 opciones.
        try: # Si es un entero, lo imprime con el símbolo del euro.
            ruleta= int(ruleta)
            print("--> %s€" %(ruleta))
        except ValueError: # Si no es un entero, lo imprime tal cual.
            print("--> %s" %ruleta)
        
        if ruleta=="QUIEBRA": # Si la ruleta cae en quiebra, se resetea el dinero que llevas.
            total=0
            print("Has caído en la quiebra, pierdes todo el dinero que llevabas.")
            input("Pulsa Intro para continuar...")
        else:
            while True:
                consonante=input("Introduce una cosonante: ")
                consonante=consonante.upper()
                if consonante not in consonantes: # Consonante no se encuentra en la lista de consonantes.
                    print("No has introducido una consonante.")
                elif consonante in acumulacionConsonantes: # Consonante repetida.
                    print("Ya has dicho esta consonante.")
                elif consonante in consonantes:
                    if consonante=="": # Caso en el que el usuario introduzca un Intro.
                        print("No has introducido ninguna consonante.")
                    elif consonante in panel: # La consonante se encuentra en la frase que hay que adivinar.
                        listaConsonantes=acumulacionConsonantes.append(consonante) # Añadir la consonante a una lista en la que se encuentran todas las introducidas anteriormente.
                        fraseConsonantes=cambiarConsonantes(i, acumulacionConsonantes, contador)
                        vecesLetra=fraseConsonantes[1]
                        if vecesLetra==1:
                            print("La '%s' está %s vez." %(consonante, vecesLetra))
                        else:
                            print("La '%s' está %s veces." %(consonante, vecesLetra))
                        try: # Si ha tocado un número en la ruleta, se lo sumas al total.
                            dinero=vecesLetra*int(ruleta)
                            total= total+dinero
                        except ValueError: # Si la ruleta cae en x2, se duplica el dimero que llevas conseguido.
                            total= total*2

                        input("Pulsa Intro para continuar...")
                        break
                    else: # La consonante no se encuentra en la frase que hay que adivinar.
                        listaConsonantes=acumulacionConsonantes.append(consonante)
                        print("La '%s' no se encuentra en el panel." %consonante)
                        input("Pulsa Intro para continuar...")
                        break
                    

    # Para la opción 2 creamos dos situaciones: Una en la que el total sea mayor que 10 en el que cual puedes comprar vocales; 
    # y otro en el que el total es menor que 10 y no te deja comprar vocales.
    elif opcion=="2" and total>=10: # Comprar vocal
        while True:
            vocal=input("Introduce una vocal: ")
            vocal= vocal.upper()
            if vocal in acumulacionConsonantes: # Caso en el que la vocal se encuentra en la lista de las letras que va introduciendo el usuario.
                print("Ya has dicho esta vocal.")
            elif vocal in vocales:
                if vocal=="": # Caso en el que el usuario introduzca un Intro.
                    print("No has introducido ninguna vocal.")
                elif vocal in panel: # La vocal se encuentra en la frase que hay que adivinar.
                    # print("%s --> -10€" %vocal)
                    # input("Pulsa Intro para continuar...")
                    dinero=10 # La vocal cuesta 10€ comprarla.
                    listaVocales=acumulacionConsonantes.append(vocal)
                    fraseConsonantes=cambiarConsonantes(i, acumulacionConsonantes, contador)
                    vecesVocal=fraseConsonantes[1]
                    if vecesVocal==1:
                        print("La '%s' está %s vez." %(vocal, vecesVocal))
                    else:
                        print("La '%s' está %s veces." %(vocal, vecesVocal))
                    total=total-dinero
                    input("Pulsa Intro para continuar...")
                    break
                else: # La vocal no se encuentra en la frase que hay que adivinar. No te quitan dinero.
                    print("La '%s' no se encuentra en el panel." %vocal)
                    input("Pulsa Intro para continuar...")
                    break
            else: # Caso en el que no se introduzca una vocal.
                print("No has introducido una vocal.")
    elif opcion=="2" and total<10:
        print("No tienes suficiente dinero para comprar una vocal.")
        input("Pulsa Intro para continuar...")
    elif opcion=="3": # Resolver
        respuesta = input("Solución: ")
        respuesta = respuesta.upper()
        solucion = esSolucion()
        if solucion[0] == solucion[1]: # Habíamos creado una lista en la función de la solución. Ahora compramos los elementos de dicha lista. Si los dos elementos son iguales, significa que la respuesta es correcta.
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
            print("Has conseguido un total de %s€\n" %total)
            break
        else:
            print("Esa no es la solución. Inténtalo de nuevo.")
            input("Pulsa Intro para continuar...")
    elif opcion=="4": # Rendirme
        break
    else:
        print("Elije una de las opciones del menú.")
        input("Pulsa Intro para continuar...")