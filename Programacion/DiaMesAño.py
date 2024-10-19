fecha=input("Escriba una fecha: ")

fecha=fecha.split("/")
dia=fecha[0]
mes=fecha[1]
annio=fecha[2]
print ('''
       Día: %s
       Mes: %s
       Año: %s'''%(dia,mes,annio))