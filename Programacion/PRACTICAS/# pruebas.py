palabra= input("Palabra: ")
palabraInversa= palabra[::-1]
if palabra==palabraInversa:
    print("palindromo")
else:
    print("no palindromo")
    print("Adiós")






# import datetime
# import math

# fechaCumple= input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ") # 29/06/2003
# fechaCumple=fechaCumple.split("/")

# diaHoy=datetime.datetime.today().day
# mesHoy=datetime.datetime.today().month
# anioHoy=datetime.datetime.today().year

# meses={
#     "enero": 31,
#     "febrero": 29,
#     "marzo": 31, 
#     "abril": 30,
#     "mayo": 31,
#     "junio": 30,
#     "julio": 31,
#     "agosto": 31,
#     "septiembre": 30,
#     "octubre": 31,
#     "noviembre": 30,
#     "diciembre": 31
#     }

# mes=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

# if fechaCumple[1]=="01":
#     fechaCumple[1]=mes[0]
# elif fechaCumple[1]=="02":
#     fechaCumple[1]=mes[1]
# elif fechaCumple[1]=="03":
#     fechaCumple[1]=mes[2]
# elif fechaCumple[1]=="04":
#     fechaCumple[1]=mes[3]
# elif fechaCumple[1]=="05":
#     fechaCumple[1]=mes[4]
# elif fechaCumple[1]=="06":
#     fechaCumple[1]=mes[5]
# elif fechaCumple[1]=="07":
#     fechaCumple[1]=mes[6]
# elif fechaCumple[1]=="08":
#     fechaCumple[1]=mes[7]
# elif fechaCumple[1]=="09":
#     fechaCumple[1]=mes[8]
# elif fechaCumple[1]=="10":
#     fechaCumple[1]=mes[9]
# elif fechaCumple[1]=="11":
#     fechaCumple[1]=mes[10]
# elif fechaCumple[1]=="12":
#     fechaCumple[1]=mes[11]

# if mesHoy==1:
#     mesHoy=mes[0]
# elif mesHoy==2:
#     mesHoy=mes[1]
# elif mesHoy==3:
#     mesHoy=mes[2]
# elif mesHoy==4:
#     mesHoy=mes[3]
# elif mesHoy==5:
#     mesHoy=mes[4]
# elif mesHoy==6:
#     mesHoy=mes[5]
# elif mesHoy==7:
#     mesHoy=mes[6]
# elif mesHoy==8:
#     mesHoy=mes[7]
# elif mesHoy==9:
#     mesHoy=mes[8]
# elif mesHoy==10:
#     mesHoy=mes[9]
# elif mesHoy==11:
#     mesHoy=mes[10]
# elif mesHoy==12:
#     mesHoy=mes[11]

# # Calcular los dias del año del cumple y calcular los dias que quedan del año en el que estamos.
# eneroDias=31
# febreroDias=eneroDias+28
# marzoDias=febreroDias+31
# abrilDias=marzoDias+30
# mayoDias=abrilDias+31
# junioDias=mayoDias+30
# julioDias=junioDias+31
# agostoDias=julioDias+31
# septiembreDias=agostoDias+30
# octubreDias=septiembreDias+31
# noviembreDias=octubreDias+30
# diciembreDias=noviembreDias+31

# numMes={
#     "enero":1,
#     "febrero":2,
#     "marzo":3,
#     "abril":4,
#     "mayo":5,
#     "junio":6,
#     "julio":7,
#     "agosto":8,
#     "septiembre":9,
#     "octubre":10,
#     "noviembre":11,
#     "diciembre":12
# }

# if fechaCumple[1]=="enero":
#     diasCumple=int(fechaCumple[0])
# elif fechaCumple[1]=="febrero":
#     diasCumple=int(fechaCumple[0])+eneroDias
# elif fechaCumple[1]=="marzo":
#     diasCumple=int(fechaCumple[0])+febreroDias
# elif fechaCumple[1]=="abril":
#     diasCumple=int(fechaCumple[0])+marzoDias
# elif fechaCumple[1]=="mayo":
#     diasCumple=int(fechaCumple[0])+abrilDias
# elif fechaCumple[1]=="junio":
#     diasCumple=int(fechaCumple[0])+mayoDias
# elif fechaCumple[1]=="julio":
#     diasCumple=int(fechaCumple[0])+junioDias
# elif fechaCumple[1]=="agosto":
#     diasCumple=int(fechaCumple[0])+julioDias
# elif fechaCumple[1]=="septiembre":
#     diasCumple=int(fechaCumple[0])+agostoDias
# elif fechaCumple[1]=="octubre":
#     diasCumple=int(fechaCumple[0])+septiembreDias
# elif fechaCumple[1]=="noviembre":
#     diasCumple=int(fechaCumple[0])+octubreDias
# elif fechaCumple[1]=="diciembre":
#     diasCumple=int(fechaCumple[0])+noviembreDias

# diasRestantesMes= meses[mesHoy]-diaHoy

# if mesHoy=="enero":
#     diasRestantesAnio = 365-(diaHoy)
# elif mesHoy=="febrero":
#     diasRestantesAnio = 365-(diaHoy+eneroDias)
# elif mesHoy=="marzo":
#     diasRestantesAnio = 365-(diaHoy+febreroDias)
# elif mesHoy=="abril":
#         diasRestantesAnio = 365-(diaHoy+marzoDias)
# elif mesHoy=="mayo":
#         diasRestantesAnio = 365-(diaHoy+abrilDias)
# elif mesHoy=="junio":
#         diasRestantesAnio = 365-(diaHoy+mayoDias)
# elif mesHoy=="julio":
#         diasRestantesAnio = 365-(diaHoy+junioDias)
# elif mesHoy=="agosto":
#         diasRestantesAnio = 365-(diaHoy+julioDias)
# elif mesHoy=="septiembre":
#         diasRestantesAnio = 365-(diaHoy+agostoDias)
# elif mesHoy=="octubre":
#         diasRestantesAnio = 365-(diaHoy+septiembreDias)
# elif mesHoy=="noviembre":
#         diasRestantesAnio = 365-(diaHoy+octubreDias)
# elif mesHoy=="diciembre":
#         diasRestantesAnio = 365-(diaHoy+noviembreDias)

# diasRestantesCumple= diasCumple + diasRestantesAnio

# mesesAnio = 12-numMes[mesHoy]
# mesesCumple = numMes[fechaCumple[1]]
# mesesRestantes = mesesAnio+mesesCumple

# print("Quedan %s meses para tu cumple." %mesesRestantes)
# print("Quedan %s días para tu cumple." %diasRestantesCumple)