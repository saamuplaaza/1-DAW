import datetime
nombre=input ("¿Cuál es tu nombre?: ")
fecha=input ("¿Cuando naciste? ")
años=datetime.datetime.year-int(fecha)
años=str(años)
print ("Tu nombre es "+ nombre+" y tienes "+años+" años.")