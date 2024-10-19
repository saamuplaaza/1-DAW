print('''
  *****************************************
      
      Resolvamos la siguiente ecuaión:
      ax^2-bx+c=0
      
  *****************************************
      ''')
import math
a = int(input("Valor de 'a': "))
b = int(input("Valor de 'b': "))
c = int(input("Valor de 'c': "))
raiz=(b**2)-(4*a*c)
if raiz>0:
    result_raiz=math.sqrt(abs(raiz))
    x1 = ((-b+result_raiz)/(2*a)).__round__(5)
    x2 = ((-b-result_raiz)/(2*a)).__round__(5)
    print("x1: ",x1)
    print("x2: ",x2)
else:
    print("Solución no real.")
