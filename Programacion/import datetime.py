import datetime


#Solicito nombre y año de nacimiento por teclado
nombre=input("¿Cuál es tu nombre?:").title
anioNacimiento=input("¿En qué año naciste?:")
anioNacimiento=int(anioNacimiento)
anioActual=datetime.datetime.today().year


edad=anioActual-anioNacimiento
print ("Te llamas "+nombre+" y tienes "+str(edad)+" años")