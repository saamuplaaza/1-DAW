
numeroEntero=input("Escriba su número de teléfono con el prefijo y la extensión: ")
numeroEntero=numeroEntero.strip("+")
numeroSeparado=[]
numeroJunto=""
numeroSolo=""
extension=""
prefijo=""
prefijos=["49","54","61","43","32","1","57","34"]
pais=["Alemania","Argentina","Australia","Austria","Bélgica","Canadá","Colombia","España"]


if len(numeroEntero)>9:
    i=0
    while i<len(numeroEntero):
        if numeroEntero[i]==" " or numeroEntero[i]=="-" or numeroEntero[i]==".":
            numeroSeparado.append(numeroEntero[:i])
            numeroEntero=numeroEntero[i+1:]
            i=0
        i+=1
    numeroSeparado.append(numeroEntero)

    i=0
    while i<len(numeroSeparado):
            numeroJunto=numeroJunto+numeroSeparado[i]
            i+=1
    #print(numeroJunto)
    prefijo=prefijo+numeroJunto[:2]
    if numeroJunto[:2] in prefijos:
        numeroSolo=numeroSolo+numeroJunto[2:11]
        extension=extension+numeroJunto[11:]       
    else:
         numeroSolo=numeroSolo+numeroJunto[:9]
         extension=extension+numeroJunto[9:]
         print("Número:%s\nPrefijo: No encontrado\nExtensión: %s"%(numeroSolo,extension))
    if prefijo in prefijos[0]:
         print ("Número:%s\nPrefijo: %s(+%s)\nExtensión: %s"%(numeroSolo,pais[0],prefijos[0],extension))
    if prefijo in prefijos[1]:
         print ("Número:%s\nPrefijo: %s(+%s)\nExtensión: %s"%(numeroSolo,pais[1],prefijos[1],extension))
    if prefijo in prefijos[2]:
         print ("Número:%s\nPrefijo: %s(+%s)\nExtensión: %s"%(numeroSolo,pais[2],prefijos[2],extension))
    if prefijo in prefijos[3]:
         print ("Número:%s\nPrefijo: %s(+%s)\nExtensión: %s"%(numeroSolo,pais[3],prefijos[3],extension))
    if prefijo in prefijos[4]:
         print ("Número:%s\nPrefijo: %s(+%s)\nExtensión: %s"%(numeroSolo,pais[4],prefijos[4],extension))
    if prefijo in prefijos[5]:
         print ("Número:%s\nPrefijo: %s(+%s)\nExtensión: %s"%(numeroSolo,pais[5],prefijos[5],extension))
    if prefijo in prefijos[6]:
         print ("Número:%s\nPrefijo: %s(+%s)\nExtensión: %s"%(numeroSolo,pais[6],prefijos[6],extension))
    if prefijo in prefijos[7]:
         print ("Número:%s\nPrefijo: %s(+%s)\nExtensión: %s"%(numeroSolo,pais[7],prefijos[7],extension))
elif len(numeroEntero)==9:
     print("Número:%s\nPrefijo: No encontrado\nExtensión: No encontrada"%(numeroEntero))
else:
     print("Número no válido.")   



# i=0
# while i<len(numeroSeparado):
#      if (numeroSeparado[i] in prefijos):  #Comparo que la palabra no esté en el vector articulo
#           numeroSeparado[i]=numeroSeparado[i].replace(prefijos,pais)#Pone en mayuscula la primera
#      else:
#           numeroSeparado=numeroSeparado[i] #Pone en minuscula 
#           print("Prefijo incorrecto")
# print (numeroSeparado)





# numero=numeroEntero.split("-") #Hacemos que divida la cadena cuando haya un "-".
# print(numero[1])