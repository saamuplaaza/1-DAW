
#Vamos a sumar, restar, mutiplicar y dividir dos numeros. Hacemos que las dos variables numero sean decimales.

numero1=input("Dime un número: ")
numero1=float(numero1)
numero2=input("Dime otro número: ")
numero2=float(numero2)
suma=numero1+numero2
resta=numero1-numero2
mutiplicacion=numero1*numero2
mutiplicacion=round(mutiplicacion,3)
division=numero1/numero2
division=round(division,3)
print('''
Resultados:
Suma: %s
Resta: %s
Multiplicación: %s
División: %s''' % (suma,resta,mutiplicacion,division))