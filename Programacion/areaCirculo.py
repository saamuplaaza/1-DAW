import math
print("Introduzca los datos de círculo.")
radio=input("Radio(cm):")
radio=float(radio)
perimetroCirculo=2*math.pi*radio
perimetroCirculo=round(perimetroCirculo,2)
areaCirculo=math.pi*radio**2
areaCirculo=round(areaCirculo,2)
print('''El perímetro del círculo es %s cm.
El área del círculo es %s cm.'''%(perimetroCirculo,areaCirculo))