import array

nombreCompleto=input("Escribe tu nombre completo: ")
nombreCompleto=(nombreCompleto.lower()).split()
articulos=["el","la","los","las","de","del","de la"]
nombre=[]
i=0
while i<len(nombre):
    n=0
    while i<len(articulos):
        if nombreCompleto[i]==articulos[n]:
            nombre.append(nombreCompleto[i])
            i+=1
        else:
            n+=1
    nombreCompleto[i]=nombreCompleto.title()
    nombre.append(nombreCompleto[i])
    i+=1
j=0
nombreMayMin=""
while j<len(nombre):
    nombreMayMin=nombreMayMin+nombre[j]+" "
    j+=1
print(nombreMayMin)