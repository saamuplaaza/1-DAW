fecha=input("Fecha de nacimiento (dd/mm/aaaa): ").split("/")
if(int(fecha[0])<=31 and int(fecha[0])>0) and (int(fecha[1])<=12 and int(fecha[1])>0):
    meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

    dia=fecha[0]
    mes=fecha[1]
    if fecha[1]=="1" and "01":
            mes=meses[0]
    if fecha[1]=="2" and "02":
            mes=meses[1]
    if fecha[1]=="3" and "03":
            mes=meses[2]
    if fecha[1]=="4" and "04":
            mes=meses[3]
    if fecha[1]=="5" and "05":
            mes=meses[4]
    if fecha[1]=="6" and "06":
            mes=meses[5]
    if fecha[1]=="7" and "07":
            mes=meses[6]
    if fecha[1]=="8" and "08":
            mes=meses[7]
    if fecha[1]=="9" and "09":
            mes=meses[8]
    if fecha[1]=="10" and "10":
            mes=meses[9]
    if fecha[1]=="11" and "11":
            mes=meses[10]
    if fecha[1]=="12" and "12":
            mes=meses[11]      
    
    anio=fecha[2]

    '''i=0
    while i<len(fecha):
        fechaN=fechaN+fecha[i]
        i+=1'''
    print("Naciste el %s de %s de %s."%(dia,mes,anio))
else:
    print("El día o mes introducido no existe.")