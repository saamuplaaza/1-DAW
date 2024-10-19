
def checkfloat(edad):
    edad=input("Edad: ")

sexo=input("Sexo: ")
edad=input("Edad: ")
if (sexo=="m" and (float(edad)>=18 and float(edad)<=20)) or (sexo=="h" and ((float(edad)>=18 and float(edad)<=25))):
    print("Puedes pasar.")
else:
    print("No puedes pasar.")