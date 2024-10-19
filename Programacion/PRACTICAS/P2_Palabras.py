# -----------------------------------------------
#   Nombre:Samuel Plaza Sáez
#   Curso: 1º DAW
#   Título: PRÁCTICA 2: OPERACIONES CON CADENAS
# -----------------------------------------------


#Funciones

def quitarTildeTexto(leer,i):
    # Meter el texto en una lista para recorrerla e ir cambiando las vocales que tengan tilde por vocales sin tilde.
    lista=list(leer)
    for letra in lista:
        if letra =="á":
            lista[i]="a"
        elif letra=="é":
            lista[i]="e"
        elif letra=="í":
            lista[i]="i"
        elif letra=="ó":
            lista[i]="o"
        elif letra=="ú":
            lista[i]="u"
        i+=1
    leer="".join(lista)
    return leer

def numLineas():
    # Separar por retorno de cargo para contar las líneas del texto.
    lineas=len(leer.split("\n"))
    return lineas

def limpiarTexto(listaLimpia, sinTilde):
    for letra in sinTilde:
        # En la tabla ASCII las letras minúsculas van del 97 al 122.
        # Esta función todo lo que no sean letras, números o \n lo reemplaza por espacios.
        #  Así conseguimos limpiarlo de otros caracteres.
        if (ord(letra) >= 97 and ord (letra) <= 122):
            letra=letra
        elif (ord(letra) >= 48 and ord(letra) <= 57):
            letra=letra
        elif letra == "\n":
            letra=letra
        else:
            letra=letra.replace(letra, " ")
        listaLimpia=listaLimpia+letra
    return listaLimpia

def vecesPalabra(repeticion, buscar):
    textoLimpio=limpiarTexto(listaLimpia, sinTilde)
    lineas=textoLimpio.split("\n")
    # Recorre cada línea del texto limpio y separa por espacios.
    # Incrementa el valor de repeticion si coincide buscar y palabra.
    for linea in lineas:
        linea=linea.split(" ")
        for palabra in linea:
            if buscar == palabra:
                repeticion+=1
    return repeticion

def contarPalabras(limpiar):
    # Separamos el texto limpio por espacios para obtener el número de palabras del texto (a través de la longitud de la lita que se crea).
    textoLimpio=limpiarTexto(listaLimpia, sinTilde)
    palabras=textoLimpio.split()
    return len(palabras)

def contarCaracteres():
    # Meter en una lista cada caracter del texto original (obtenemos nº de caracteres a través de la longitud de la lista).
    listacaracteres=list(leer)
    return len(listacaracteres)

def quitarTildePalabra(palabra,i):
        # Meter el texto en una lista para recorrerla e ir cambiando las vocales que tengan tilde por vocales sin tilde (tanto mayúsculas como minúsculas).
        # Esta función se va a usar en la opción 3 del menú e intenta guardar el formato de la palabra introducida por el usuario.
    lista=list(palabra)
    for letra in lista:
        if letra =="á":
            lista[i]="a"
        elif letra=="é":
            lista[i]="e"
        elif letra=="í":
            lista[i]="i"
        elif letra=="ó":
            lista[i]="o"
        elif letra=="ú":
            lista[i]="u"
        if letra =="Á":
            lista[i]="A"
        elif letra=="É":
            lista[i]="E"
        elif letra=="Í":
            lista[i]="I"
        elif letra=="Ó":
            lista[i]="O"
        elif letra=="Ú":
            lista[i]="U"
        i+=1
    palabra="".join(lista)
    return palabra

def cambiarVocal(i):
    lista=list(palabraSinTilde)
    # No pasar la palabra introducida por el usuario a minúsculas para mantener el formato.
    # Recorrer la palabra y sustituir las vocales por lavocal introducida por el usuario.
    # Previamente se han quitado las tildes a las vocales, ya que van a ser sustituidas y no altera el formato de la palabra.
    for letra in lista:
        if letra =="a" or letra=="A":
            lista[i]=vocal
        elif letra=="e" or letra=="E":
            lista[i]=vocal
        elif letra=="i" or letra=="I":
            lista[i]=vocal
        elif letra=="o" or letra=="O":
            lista[i]=vocal
        elif letra=="u" or letra=="U":
            lista[i]=vocal
        i+=1
    palabraCambiada="".join(lista)
    return palabraCambiada

def esPalindrimo(i):
    while i<len(palabraPalindromo):
        # Si la palabra es un número, no puede ser palíndromo, por eso intenta pasar de cadena a entero.
        try:
            palabraPalindromo[i]=int(palabraPalindromo[i])
            print("%s --> Solo las palabras pueden ser palíndromos."%(palabraPalindromo[i]))
        except ValueError:
            # Si no es un entero, evalúa si es igual normal y leída al revés.
            # Previamente se ha pasado todo a minúsculas.
            if palabraPalindromo[i]==palabraPalindromo[i][::-1]:
                print("%s --> Sí es un palíndromo."%(palabraPalindromo[i]))
            else:
                print("%s --> No es un palíndromo."%(palabraPalindromo[i]))
        i+=1
    
    
#Variables
i=0
repeticion=0
numPalabras=0
contador=0
listaLimpia=""

#Código principal
while True:
    print("""

.______    ___                   ______   .______    _______ .______          ___       ______  __    ______   .__   __.  _______     _______.
|   _  \  |__ \                 /  __  \  |   _  \  |   ____||   _  \        /   \     /      ||  |  /  __  \  |  \ |  | |   ____|   /       |
|  |_)  |    ) |     ______    |  |  |  | |  |_)  | |  |__   |  |_)  |      /  ^  \   |  ,----'|  | |  |  |  | |   \|  | |  |__     |   (----`
|   ___/    / /     |______|   |  |  |  | |   ___/  |   __|  |      /      /  /_\  \  |  |     |  | |  |  |  | |  . `  | |   __|     \   \    
|  |       / /_                |  `--'  | |  |      |  |____ |  |\  \----./  _____  \ |  `----.|  | |  `--'  | |  |\   | |  |____.----)   |   
| _|      |____|                \______/  | _|      |_______|| _| `._____/__/     \__\ \______||__|  \______/  |__| \__| |_______|_______/    
                                                                                                                                              
  ______   ______   .__   __.      ______     ___       _______   _______ .__   __.      ___           _______.                               
 /      | /  __  \  |  \ |  |     /      |   /   \     |       \ |   ____||  \ |  |     /   \         /       |                               
|  ,----'|  |  |  | |   \|  |    |  ,----'  /  ^  \    |  .--.  ||  |__   |   \|  |    /  ^  \       |   (----`                               
|  |     |  |  |  | |  . `  |    |  |      /  /_\  \   |  |  |  ||   __|  |  . `  |   /  /_\  \       \   \                                   
|  `----.|  `--'  | |  |\   |    |  `----./  _____  \  |  '--'  ||  |____ |  |\   |  /  _____  \  .----)   |                                  
 \______| \______/  |__| \__|     \______/__/     \__\ |_______/ |_______||__| \__| /__/     \__\ |_______/                                   
                                                                                                                                              

""")
    input("Pulse cualquier tecla para abrir el menú.")
    print("----------------------------------------------MENU---------------------------------------------------------\n")
    print("\t1. Encontrar palabra\n")
    print("\t2. Conteo de palabras\n")
    print("\t3. Cambiar vocal\n")
    print("\t4. Palíndromo\n")
    print("\t0. Salir")
    print("-----------------------------------------------------------------------------------------------------------\n")
    opcion=input("Elija una opción: ")
    print("-----------------------------------------------------------------------------------------------------------\n")

    # Pide un archivo tanto si has elegido la opción 1 o la 2 del menú. 
    # De esta forma ahorro tener que copiar dos veces el mismo código (evito redundancia).
    if opcion=="":
        print("Debe elegir una de las opciones del menú.")
        input("Pulse cualquier tecla para continuar...")
    elif opcion=="1" or opcion=="2":
        try:
            archivo=input("Introduzca el nombre del fichero (extenión incluida): ")
            abrirArchivo=open(archivo,"r", encoding="utf-8")
        except FileNotFoundError:
            print("Archivo no encontrado.")
            input("Pulse cualquier tecla para continuar...")
        else:
            leer=abrirArchivo.read()
            print(leer)
            leer=leer.lower()
            sinTilde=quitarTildeTexto(leer, i)
            if opcion=="1":
                buscar=input("Palabra para buscar: ")
                buscar=buscar.lower()
                vecesRepetida=vecesPalabra(repeticion, buscar)
                print("\nVeces que se repite la palabra '%s' en el texto: %s"%(buscar,vecesRepetida))
                print("\n(No se han tenido en cuenta mayúsculas, minúsculas o tildes)")
                print("-----------------------------------------------------------------------------------------------------------\n")
                input("Pulse cualquier tecla para continuar...")

            if opcion=="2":
                limpiar=limpiarTexto(listaLimpia, sinTilde)
                numPalabras=contarPalabras(limpiar)
                numCaracteres= contarCaracteres()
                numeroLineas=numLineas()
                print("\nNúmero de palabras: %s"%numPalabras)
                print("Número de caracteres: %s"%numCaracteres)
                print("Número de líneas: %s"%numeroLineas)
                print("-----------------------------------------------------------------------------------------------------------\n")
                input("Pulse cualquier tecla para continuar...")      
    elif opcion=="3":
        palabra=input("Introduzca una palabra: ")
        vocal=input("Introduzca una vocal: ")
        palabraSinTilde=quitarTildePalabra(palabra, i)
        cambioVocal=cambiarVocal(i)
        print("\n"+cambioVocal)
        print("-----------------------------------------------------------------------------------------------------------\n")
        input("Pulse cualquier tecla para continuar...")
    elif opcion=="4":
        palabraPalindromo=input("Introduzca una palabra: ")
        palabraPalindromo=palabraPalindromo.lower()
        try:
            palabraPalindromo=int(palabraPalindromo)
            print("Solo las palabras pueden ser palíndromos.")
            print("-----------------------------------------------------------------------------------------------------------\n")
            input("Pulse cualquier tecla para continuar...")
        except ValueError:
            palabraPalindromo=palabraPalindromo.split(" ")
            palindromo=esPalindrimo(i)
            print("-----------------------------------------------------------------------------------------------------------\n")
            input("Pulse cualquier tecla para continuar...")
    elif opcion=="0":
        break
    else:
        print("Debe elegir una de las opciones del menú.")