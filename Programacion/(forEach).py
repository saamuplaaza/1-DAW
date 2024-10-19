#Ejercicio 1

import ipinfo
token= "3e65ca0ac3fc5a"
handler= ipinfo.getHandler(token)
ip=input("Introduzca la IP: ")
detalles= handler.getDetails(ip)

for clave in detalles.all:
    print("%s: %s" %(clave, detalles.all[clave]))