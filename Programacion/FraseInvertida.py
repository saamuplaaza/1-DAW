
frase=input("Escriba cualquier frase: ")
frase=frase.split() 
fraseInvertida=""
n=-1
while n>=-len(frase):
    fraseInvertida=(fraseInvertida+frase[n]+" ").capitalize()
    n-=1
print (fraseInvertida)  