#Ejercicio 8
#Importamos "os" y utilizamos la funcion "system" para que escriba el comando que le pidamos. 
import os

answer=input("¿Quieres saber las especificaciones de tu PC?: ")
if answer=="si" or answer=="Si":
    
    print("MOSTRANDO ESPECIFICACIONES DEL PC:")
    nombreEquipo=os.system("hostname")
    mascaraRed=os.system(command="getmac")
    puertaEnlace=os.system(command="netsh interface ip show config")
    ipDNS=os.system(command="nslookup")

else:
    print("Vale, ok.")