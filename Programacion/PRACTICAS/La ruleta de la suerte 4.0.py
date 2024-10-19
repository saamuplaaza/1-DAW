# Las ventajas de la POO son que:
# Tienes mejor estructurado el programa y sabes cada método y cada objeto a qué calse sirve, haciendo más fácil 
# la modificación del programa en un futuro. Este tipo de programación es muy efectiva con programas grandes en los que hay muchos métodos,
# muchas clases, incluso que pueden hacer referencia a otros códigos que se encuentran en otros archivos.




import os
import random

class Juego:
    """Esta clase representa un juego."""
    
    casillasRuleta = [50, 25, 50, 0, 75, 25, 100, "x2", "QUIEBRA", "PIERDE TURNO"]
    dineroTotalJugadores = []
    
    def __init__(self, fraseOriginal, numJugadores):
        """Inicializa los atributos de instancia.

        Args:
            turno (int): Jugador que está jugando en este momento.
            fraseOriginal (str): Frase con la que se va a jugar (paanel).
            fraseDescubierta (str): Frase destapada según se vayan descubriendo letras.
            numJugadores (int): Número de jugadores que van a participar en el juego.
            listaLetras (list): Letras que ya se han dicho entre todos los jugadores.
            casillasRuleta (list): Valores que tiene la ruleta.
        """
        self.turno = 1
        self.fraseOriginal = fraseOriginal
        self.numJugadores = numJugadores
        self.listaLetras = []
        
    def set_turno(self, turno):
        self.turno = turno
        return self.turno
        
    def get_fraseOriginal(self):
        return self.fraseOriginal
    
    def set_fraseDescubierta(self, fraseDescubierta):
        self.fraseDescubierta = fraseDescubierta
        return self.fraseDescubierta
    
    def get_fraseDescubierta(self):
        return self.fraseDescubierta
    
    def set_numJugadores(self, numJugadores):
        self.numJugadores = numJugadores
        return self.numJugadores
    
    def get_numJugadores(self):
        return self.numJugadores
        

    def mostrarMenuUI(self,numeroJugador, fraseResuelta):
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
        print("-----------------------------------------JUGADOR %s: %s ---------------------------------------------\n" %(numeroJugador, jugadorActual.nombre))
        print("Total: %s€\n\n" % jugadorActual.total)
        print("\t1. Decir letra\n")
        print("\t2. Comprar vocal (10€)\n")
        print("\t3. Resolver\n")
        print("\t4. Rendirme\n")
        print("-----------------------------------------------------------------------------------------------------------")
        opcion=input("Elija una opción: ")
        print("-----------------------------------------------------------------------------------------------------------\n")
        return opcion

    def tirar(self, casillasRuleta):
        valorRuleta=random.choice(casillasRuleta)
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
   
    def limpiarRespuesta(respuestaSinTilde):
        respuestaLimpia=""
        for letra in respuestaSinTilde:
            if (ord(letra) >= 65 and ord (letra) <= 90) or letra=="Ñ":
                letra=letra
            else:
                letra=letra.replace(letra, " ")
            respuestaLimpia = respuestaLimpia+letra
        return respuestaLimpia
    
    def comprobarLetra(self, letra):
        consonantes= "BCDFGHJKLMNÑPQRSTVWXYZ"
        vocales = "AEIOU"
        letra = letra.upper()
        if letra in consonantes:
            return 1 # Es consonante.
        elif letra in vocales:
            return 0 # Es vocal.
        else:
            return -1 # No ha introducido letra válida.
        
    def existeLetra(self, letra, panel, listaLetras):
        letra = letra.upper()
        if letra in listaLetras:
            return -1 # Ya la has dicho.
        elif letra in panel:
            return 1 # Sí existe en el panel y no la has dicho todavía.
        else:
            return 0 # No existe en el panel y no la has dicho todavía.

    def actualizaPanel(self, panel, listaLetras):
        i=0
        contador=0
        listaAsteriscos = list(panel)
        listaSinTilde = Juego.quitarTilde(panel)
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
    
    def cambiarTurno(self, numeroJugadores, numeroJugador):
        numeroJugador+=1
        if numeroJugador > numeroJugadores:
            numeroJugador = 1
        miJuego.set_turno(numeroJugador)
        return numeroJugador
          
    def esSolucion(self):
        frase=Juego.limpiarFrase(fraseSinTilde)
        frase=frase.split()
        respuestaSinTilde=Juego.quitarTildeRespuesta(respuesta)
        solucionLimpia=Juego.limpiarRespuesta(respuestaSinTilde)
        solucionLimpia=solucionLimpia.split()
        return frase, solucionLimpia    
    
    
class Jugador:
    """Esta clase representa un jugador"""
    
    def __init__(self, nombre, edad, total):
        """Inicializa os atributos de instancia.

        Args:
            nombre (str): _description_
            edad (int): _description_
            total (int): _description_
        """
        self.total = total
        self.nombre = nombre
        self.edad = edad
        
    def set_total(self, total):
        self.total = total
        return self.total
    
    def get_total(self):
        return self.total
        
    def set_nombre(self, nombre):
        self.nombre = nombre
        return self.nombre
    
    def get_nombre(self):
        return self.nombre
    
    def set_edad(self, edad):
        self.edad = edad
        return self.edad
    
    def get_edad(self):
        return self.edad
    
    def actualizarTotal(self, tiradaRuleta, fraseResuelta):
        # Si entra en la opcion 2 significa que tiene que meter una vocal, por lo que restamos 10 al total.
        if opcionMenu == "2":
            jugadorActual.set_total(jugadorActual.total-10)
        else:
            if isinstance(tiradaRuleta, int):
                jugadorActual.set_total(jugadorActual.total+(tiradaRuleta*fraseResuelta[1]))
            elif tiradaRuleta == "x2":
                jugadorActual.set_total(jugadorActual.total*2)
            elif tiradaRuleta == "QUIEBRA":
                jugadorActual.set_total(0)
        # return jugadores[clave][2]

        
if __name__ == "__main__":
    # dineroTotalJugadores = []
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
        miJuego = Juego(panel, numeroJugadores)
        
        jugadores = {} 
        for i in range(numeroJugadores):
            nombre = input("Nombre del jugador %s: " %(i+1))
            nombre = nombre.capitalize()
            try:
                edad = int(input("Edad del jugador %s: " %(i+1)))
            except ValueError:
                print("Introduce un número entero.")
            else:
                jugadores ["Jugador %s" % (i+1)] = Jugador(nombre, edad, 0)
                
        
        
        os.system("cls")
        while True:
            clave = ["Jugador %s" %numeroJugador][0]
            jugadorActual = jugadores [clave]
            nombre = jugadorActual.nombre
            
            if listaLetras==[]:
                fraseResuelta=miJuego.actualizaPanel( panel, listaLetras)
                fraseSinTilde = fraseResuelta[2]
                opcionMenu = miJuego.mostrarMenuUI(numeroJugador, fraseResuelta)
            else:
                opcionMenu = miJuego.mostrarMenuUI(numeroJugador, fraseResuelta)

            if opcionMenu == "":
                print("Debes elegir una de las opciones del menú.")
                input("Pulsa Intro para continuar...")
            elif opcionMenu == "1": # Decir consonante
                tiradaRuleta = miJuego.tirar(miJuego.casillasRuleta)
                try:
                    (tiradaRuleta =="x2") or (tiradaRuleta == int(tiradaRuleta)) 
                    if tiradaRuleta=="x2":
                        print("--> %s" %tiradaRuleta)
                    else:
                        print("--> %s€" %(tiradaRuleta))
                except:
                    print("--> %s" %tiradaRuleta)
                    jugadorActual.actualizarTotal(tiradaRuleta, fraseResuelta)
                    numeroJugador = miJuego.cambiarTurno(numeroJugadores, numeroJugador)
                    input("Pulsa Intro para continuar...")
                else:
                    while True:
                        letra = input("Introduce una consonante: ")
                        if len(letra) != 1 or miJuego.comprobarLetra(letra)!=1:
                            print("Error: Solo puedes introducir una consonante.")
                            input("Pulsa Intro para continuar...")
                        elif miJuego.comprobarLetra(letra)==1:
                            if miJuego.existeLetra(letra, panel, listaLetras)==1:
                                listaLetras.append(letra.upper())
                                fraseResuelta = miJuego.actualizaPanel( panel, listaLetras)
                                if fraseResuelta[1]==1:
                                    print("La consonante '%s' se encuentra %s vez en el panel." %(letra.upper(), fraseResuelta[1]))
                                else:
                                    print("La consonante '%s' se encuentra %s veces en el panel." %(letra.upper(), fraseResuelta[1]))
                                jugadorActual.actualizarTotal(tiradaRuleta, fraseResuelta)
                                input("Pulsa Intro para continuar...")
                            elif miJuego.existeLetra(letra, panel, listaLetras)==0:
                                listaLetras.append(letra.upper())
                                print("La letra no se encuentra en el panel.")
                                input("Pulsa Intro para continuar...")
                                numeroJugador = miJuego.cambiarTurno(numeroJugadores, numeroJugador)
                            else:
                                print("Esta letra ya se ha intentado usar.")
                                input("Pulsa Intro para continuar...")
                                numeroJugador = miJuego.cambiarTurno(numeroJugadores, numeroJugador)
                            break
            elif opcionMenu == "2": # Comprar vocal
                if jugadorActual.total < 10:
                    print("Necesitas al menos 10€ para comprar una vocal.")
                    input("Pulsa Intro para continuar...")
                else:
                    letra = input("Introduce una vocal: ")
                    if len(letra) != 1 or miJuego.comprobarLetra(letra)!=0:
                        print("Error: Solo puedes introducir una vocal.")
                        input("Pulsa Intro para continuar...")
                    elif miJuego.comprobarLetra(letra) == 0:
                        if miJuego.existeLetra(letra, panel, listaLetras) == 1:
                            listaLetras.append(letra.upper())
                            fraseResuelta = miJuego.actualizaPanel( panel, listaLetras)
                            if fraseResuelta[1]==1:
                                print("La vocal '%s' se encuentra %s vez en el panel." %(letra.upper(), fraseResuelta[1]))
                            else:
                                print("La vocal '%s' se encuentra %s veces en el panel." %(letra.upper(), fraseResuelta[1]))
                            jugadorActual.actualizarTotal(tiradaRuleta, fraseResuelta)
                            input("Pulsa Intro para continuar...")
                        elif miJuego.existeLetra(letra, panel, listaLetras)==0:
                            listaLetras.append(letra.upper())
                            print("La letra no se encuentra en el panel.")
                            input("Pulsa Intro para continuar...")
                            numeroJugador = miJuego.cambiarTurno(numeroJugadores, numeroJugador)
                        else:
                            print("Esta letra ya se ha intentado usar.")
                            input("Pulsa Intro para continuar...")
                            numeroJugador = miJuego.cambiarTurno(numeroJugadores, numeroJugador)
            elif opcionMenu == "3": # Resolver
                respuesta = input("Solución: ")
                respuesta = respuesta.upper()
                solucion = miJuego.esSolucion()
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
                    print("%s ha ganado un total de %s€\n" %(nombre, jugadorActual.total))
                    break
                else:
                    print("Esa no es la solución.")
                    numeroJugador = miJuego.cambiarTurno(numeroJugadores, numeroJugador)
                    input("Pulsa Intro para continuar...")
            elif opcionMenu=="4": # Rendirme
                break
            else:
                print("Elije una de las opciones del menú.")
                input("Pulsa Intro para continuar...")