# -----------------------------------------------
#   Nombre:Samuel Plaza Sáez
#   Curso: 1º DAW
#   Título: PRÁCTICA 3: LA RULETA DE LA SUERTE
# -----------------------------------------------

import os
import ast

# Definir funciones.

def rellenar_preguntas(i, numPreguntas, j, numRespuestas):
    examen["Nombre del examen"]= nombre
    examen["Número de preguntas"]= numPreguntas
    listaRespuestas=[]
    while i<=numPreguntas:
        preguntas={}
        pregunta = input("Introduzca la pregunta %s: " %i).capitalize()
        preguntas["Enunciado pregunta %s" %i]=pregunta
        examen["Pregunta-%s"%i]=preguntas
        while True:
            while True:
                try:
                    numRespuestas= int(input("¿Cuántas respuestas va a tener?: "))
                except ValueError:
                    print("Número no válido.")
                else:
                    preguntas["Número de respuestas de la pregunta %s" %i]=numRespuestas
                    while j<=numRespuestas:
                        listaRespuestas=[]
                        respuesta= input("Respuesta número %s: " %j).capitalize()
                        listaRespuestas.append(respuesta)
                        listaRespuestas.append(j)
                        preguntas["Respuesta-%s de la pregunta %s "%(j, i)]= listaRespuestas
                        j+=1
                    j=1
                    break
            break
        while True:
            respuestaCorrecta= input("Respuesta/s correcta/s? (con número, separar por comas): ").split(",")
            try:
                for x in respuestaCorrecta:
                    int(x)
            except ValueError:
                print("Número no válido.")
            else:
                preguntas["Respuesta/s correcta/s de la pregunta %s" %i]=respuestaCorrecta
                i+=1
                break
    return examen

def escribirFichero():
    fichero= open("examenes_tipo_test.json", "w", encoding="utf-8")
    fichero.write(str(examenes))
    fichero.close()

def leerFichero():
    leerFichero = open("examenes_tipo_test.json", "r", encoding="utf-8")
    examenesTipoTest= leerFichero.read() 
    return examenesTipoTest

def listaDeExamenes(i, j, numExamenes):
    escribirFichero()
    leerFichero()
    if examenes=={}:
        numExamen==1
    else:
        contadorExamenes = len(lecturaFichero)
        numExamen= contadorExamenes +1
    while numExamen<=numExamenes:
        i=1
        nombreExamen = examenes["Examen %s" %numExamen][0]["Nombre del examen"]
        numeroPreguntas = examenes["Examen %s" %numExamen][0]["Número de preguntas"]
        print("\nNombre del examen: %s" %nombreExamen)
        print("Número de preguntas en el examen: %s" %numeroPreguntas)
        while i<=numeroPreguntas:
            numRespuestas= examenes["Examen %s" %numExamen][0]["Pregunta-%s"%i]["Número de respuestas de la pregunta %s" %i]
            enunciado = examenes["Examen %s" %numExamen][0]["Pregunta-%s"%i]["Enunciado pregunta %s" %i]
            print("Pregunta-%s: %s" %(i, enunciado))
            while j <= numRespuestas:
                respuestaPregunta = examenes["Examen %s" %numExamen][0]["Pregunta-%s"%i]["Respuesta-%s de la pregunta %s "%(j, i)][0]
                print("\t%s. %s" %(j, respuestaPregunta))
                j+=1
            j=1
            i+=1
        numExamen+=1



# Definir variables.
i=1
j=1
numExamen=1
numExamenes=0
examen={}
examenes={}
preguntas={}
numRespuestas=0
contadorExamenes=0


# Código principal
os.system("cls")
while True:
    i=1
    j=1
    examen={}
    examenes = {}
    try:
        lecturaFichero = leerFichero()
        lecturaFichero = ast.literal_eval(lecturaFichero)
    except:
        lecturaFichero = {}
    if lecturaFichero=={}:
        numExamen==1
    else:
        contadorExamenes = len(lecturaFichero)
        numExamen= contadorExamenes +1
        numRespuestas=0
    print('''
    .______       __________   ___ .___________..______          ___                      
    |   _  \     |   ____\  \ /  / |           ||   _  \        /   \      _              
    |  |_)  |    |  |__   \  V  /  `---|  |----`|  |_)  |      /  ^  \    (_)             
    |   ___/     |   __|   >   <       |  |     |      /      /  /_\  \                   
    |  |         |  |____ /  .  \      |  |     |  |\  \----./  _____  \   _              
    | _|    _____|_______/__/ \__\     |__|     | _| `._____/__/     \__\ (_)             
        |______|                                                                       
    __________   ___      ___      .___  ___.  _______ .__   __.                         
    |   ____\  \ /  /     /   \     |   \/   | |   ____||  \ |  |                         
    |  |__   \  V  /     /  ^  \    |  \  /  | |  |__   |   \|  |                         
    |   __|   >   <     /  /_\  \   |  |\/|  | |   __|  |  . `  |                         
    |  |____ /  .  \   /  _____  \  |  |  |  | |  |____ |  |\   |                         
    |_______/__/ \__\ /__/     \__\ |__|  |__| |_______||__| \__|                         
                                                                                        
    .___________. __  .______     ______      .___________. __________   ___ .___________.
    |           ||  | |   _  \   /  __  \     |           ||   ____\  \ /  / |           |
    `---|  |----`|  | |  |_)  | |  |  |  |    `---|  |----`|  |__   \  V  /  `---|  |----`
        |  |     |  | |   ___/  |  |  |  |        |  |     |   __|   >   <       |  |     
        |  |     |  | |  |      |  `--'  |        |  |     |  |____ /  .  \      |  |     
        |__|     |__| | _|       \______/         |__|     |_______/__/ \__\     |__|     
        ''')
    print("-----------------------------------------------------------------------------------------------------------\n")
    print("\n------------------------------------------------MENÚ-------------------------------------------------------\n")
    print("\t1. CREAR TIPO TEST\n")
    print("\t2. REALIZAR TIPO TEST\n")
    print("\t0. Salir\n")
    print("-----------------------------------------------------------------------------------------------------------")
    opcion=input("Elija una opción: ")
    print("-----------------------------------------------------------------------------------------------------------\n")
    if opcion=="":      # Introduce un Intro por teclado.
        print("Debes elegir una de las opciones del menú.")
        input("Pulsa Intro para continuar...")
    if opcion=="1":     # Crear tipo test.
        numExamenes+=1
        nombre = input("Nombre del examen: ").capitalize()
        while True:
            try:
                numPreguntas = int(input("Número de preguntas: "))
            except ValueError:
                print("Número no válido.")
            else:
                esqueletoExamen = rellenar_preguntas(i, numPreguntas, j, numRespuestas)
                numExamen = len(lecturaFichero) +1
                examenes["Examen %s" %numExamen]= [examen, numExamenes]
                escrituraFichero = escribirFichero()
                # numExamen= len(lecturaFichero)
                break
        os.system("cls")
        
        lecturaFichero= leerFichero()
        lecturaFichero = ast.literal_eval(lecturaFichero)
        listaDeExamenes(i, j, numExamenes)
        
        print(lecturaFichero)
        input("Pulse Intro para continuar...")






        # while numExamen<=numExamenes:
        #     i=1
        #     nombreExamen = examenes["Examen %s" %numExamen][0]["Nombre del examen"]
        #     numeroPreguntas = examenes["Examen %s" %numExamen][0]["Número de preguntas"]
        #     print("\nNombre del examen: %s" %nombreExamen)
        #     print("Número de preguntas en el examen: %s" %numeroPreguntas)
        #     while i<=numPreguntas:
        #         numRespuestas= examenes["Examen %s" %numExamen][0]["Pregunta-%s"%i]["Número de respuestas de la pregunta %s" %i]
        #         enunciado = examenes["Examen %s" %numExamen][0]["Pregunta-%s"%i]["Enunciado pregunta %s" %i]
        #         print("Pregunta-%s: %s" %(i, enunciado))
        #         while j <= numRespuestas:
        #             respuestaPregunta = examenes["Examen %s" %numExamen][0]["Pregunta-%s"%i]["Respuesta-%s de la pregunta %s "%(j, i)][0]
        #             print("\t%s. %s" %(j, respuestaPregunta))
        #             j+=1
        #         j=1
        #         i+=1
        # numExamen+=1
        # print("\n")
        # input("Pulsa Intro para continuar...")
        os.system("cls")


    elif opcion=="2":   # Realizar tipo test.
        input("Pulsa Intro para continuar...")
    elif opcion=="0":   # Salir.
        break
    else:
        print("Elije una de las opciones del menú.")
        input("Pulsa Intro para continuar...")








        # while i <= numPreguntas:
            #     try:
            #         numRespuestas = int(input("Número de respuestas para la pregunta %s: " %i))
            #     except ValueError:
            #         print("Número no válido.")
            #     else:
            #         try:
            #             numRespuestasCorrectas = int(input("Número de respuestas correctas: "))
            #         except ValueError:
            #             print("Número no válido.")
            #     i+=1
            # puntuacionPreguntas = 




                          # while True:
                #     try:
                #         numRespuestas = int(input("Número de respuestas por pregunta: "))
                #     except ValueError:
                #         print("Número no válido.")
                #     else:
                #         while True:
                #             try:
                #                 numRespuestasCorrectas = int(input("Número de respuestas correctas: "))
                #             except ValueError:
                #                 print("Número no válido.")
                #             else:
                #                 while True:
                #                     try:
                #                         puntuacionPreguntas = float(input("Puntuación de cada pregunta: "))
                #                     except:
                #                         print("Número no válido.")
                #                     else:
                #                         cambios = input("¿Desea cambiar alguna pregunta?: ").lower()
                #                         if cambios=="si" or cambios=="sí":
                #                             try:
                #                                 cambiarPregunta = int(input("¿Qué pregunta quiere cambiar?: "))
                #                             except ValueError:
                #                                 print("Número no válido.")
                #                             else:
                #                                 if cambiarPregunta < numPreguntas:
