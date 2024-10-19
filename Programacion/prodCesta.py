prodCesta=input("Prductos de la cesta: ").split(",")
prodSeparados=""
i=0
while i<len(prodCesta):
    prodSeparados=prodSeparados+prodCesta[i]+"\n"
    i+=1
    
print(prodSeparados)
