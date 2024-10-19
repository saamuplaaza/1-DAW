#Ejercicio 9

import os

answer=input("¿Quieres saber las especificaciones de tu PC?: ")
if answer=="si" or answer=="Si":
    
    mascaraRed=os.system(command="getmac")
    puertaEnlace=os.system(command="netsh interface ip show config")
    ipDNS=os.system(command="nslookup")

else:
    print("Vale, ok.")  