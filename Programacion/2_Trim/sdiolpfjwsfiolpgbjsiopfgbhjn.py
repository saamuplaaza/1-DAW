import re

while True:
    telf = input("Correo: ")
    if re.match(r"^\w*@\w*\.[a-z]{2,4}$", telf):
        print("Número correcto.")
        input("Pulse Intro para continuar")
    else:
        print("Error en el número de teléfono.")
        input("Pulse Intro para continuar")
