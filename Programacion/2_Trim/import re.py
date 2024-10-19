import re
import os

while True:
    os.system("cls")
    correo = input("Correo electrónico: ")
    if (re.match(r"^[a-z0-9\_\-\.]+@[a-z0-9\_\-\.]+\.[a-z]{2,4}$", correo.lower())):
        print("Correo correcto.")
    else:
        print("Correo incorrecto.")