
articulo=["el","la","los","las","de","del"]
nombreCompleto=input("Escribe tu nombre completo: ")
palabras=[]
#print (nombre)
#Pasar nombre de la variable cadena a vector por espacios o guiones
i=0
while i<len(nombreCompleto):
    if nombreCompleto[i]==" " or nombreCompleto[i]=="-":
        palabras.append(nombreCompleto[:i])
        nombreCompleto=nombreCompleto[i+1:]#ahora nombreCompleto vale desde i+1 hasta el final
        i=0
    i+=1
palabras.append(nombreCompleto)

i=0
while i<len(palabras):
    if not (palabras[i].lower() in articulo):  #Comparo que la palabra no esté en el vector articulo
        palabras[i]=palabras[i].title()#Pone en mayuscula la primera
    else:
        palabras=palabras[i].lower() #Pone en minuscula 
    i+=1
print (palabras)





'''n=0
while n<len(nombreCadena):
    i=0
    while i<len(articulo[i]):
        nombre=nombre+nombreCadena
        print(nombre[n][i])
        i+=1
    n+=1'''



'''n=0
i=0
while n<len(articulos) or i<len(nombreCadena):
    nombre=str(nombre)+str(nombreCompleto[i])
    if nombreCadena==" "+str(articulos):
        articulos.lower()
    if nombreCompleto[i-1]==" " or nombreCompleto[i-1]=="-":
        nombre=nombre.title()
    n+=1
    i+=1
print(nombre)'''
    




'''i=0
while i<len(nombreCadena):
    nombre=str(nombre)+str(nombreCompleto[i])
    if nombreCompleto[i-1]==" " or nombreCompleto[i-1]=="-":
        nombre=nombre.title()
    for articulo in nombre:
        articulo.lower()
    i+=1
print(nombre)'''













'''while not (i>=longitud):
    art1=articulos[i][0]
    longitudNombre=len(nombreCadena)
    j=0
    while not j>=longitudNombre:
        if (articulos in nombreCadena[j]):
            nombre.append(nombreCadena[j])
        j+=1
    i+=1


print(art1)
print(nombre)'''






'''palabra=""
i=0
while articulos==nombre:
    palabra=palabra + nombre[i]
    print(palabra)
    i+=1
else:
    print("Has acabado.")'''








'''i=0
while i<len(nombre):
    n=0
    while n<len(nombre[i]):
        print(nombre[i][n])
        n+=1
    i+=1'''