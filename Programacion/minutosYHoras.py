

tiempo=input("Escriba los minutos: ")
tiempo=int(tiempo)
horas=tiempo//60
minutos=tiempo%60
if minutos>0: #Con este condicional hago que si sobran minutos al hacer la división los imprima,pero
              #si el resto de la division es 0, que imprima solo las horas, asi no pone 0 minutos al imprimir.
    print('''%s minutos son %s horas y %s minutos.'''%(tiempo,horas,minutos))
else:
    print('''%s minutos son %s horas.'''%(tiempo,horas))