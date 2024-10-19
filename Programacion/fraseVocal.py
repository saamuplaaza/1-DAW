frase=input("Introduzca una frase: ")
vocal=input("Ahora introduzca una vocal: ").lower()
lista=["a","e","i","o","u"]
if vocal in lista:
    print(frase.replace(vocal,vocal.upper()))
else:
    print("No ha introducido una vocal.")


fraseN=input("Introduzca una frase: ")
fraseN=fraseN.lower()
vocalN=input("Ahora introduzca una vocal: ").lower()
cambio=""
lista=["a","e","i","o","u"]
i=0
while i<len(fraseN):
    if not fraseN[i] in lista:
        cambio=cambio+fraseN[i]
    else:
        cambio=cambio+vocalN
    i+=1

print(cambio)



'''else:
    print("No ha introducido una vocal.")'''
