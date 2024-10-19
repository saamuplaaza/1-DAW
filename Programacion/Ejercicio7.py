#Ejercicio 7

import socket

nombreURL=input("Escribe la URL de la página web: ")
ip= socket.gethostbyname(nombreURL)

print ("IP: "+ip)