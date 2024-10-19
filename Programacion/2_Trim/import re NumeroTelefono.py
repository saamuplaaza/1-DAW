import re
import os
while True:
    os.system("cls")
    telf = input("Número de teléfono: ")
    if re.match(r"(\(?\+?[\d]{0,3}?\)?)\s?([\d][\s\.\-]?){9,9}$",telf):
        print("Número correcto.")
        input("Pulse Intro para continuar")
    else:
        print("Error en el número de teléfono.")
        input("Pulse Intro para continuar")
