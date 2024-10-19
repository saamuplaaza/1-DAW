
def cuentaRegresiva(numero):
    if numero>=0:
        print(numero)
        numero-=1
        cuentaRegresiva(numero)

def cuentaAdelante(i,numero):
    if i<=numero:
        print(i)
        i+=1
        cuentaAdelante(i,numero)

i=0
numero=int(input('''
*****************************************
        Introduce un número: '''))

menu=int(input('''
*****************************************
Elija una opción:
    0. Cuenta hacia adelante.
    1. Cuenta hacia atrás.
'''))
               
print ('''*****************************************
''')
if menu==0:
    cuentaAdelante(i,numero)
elif menu==1:
    cuentaRegresiva(numero)
else:
    print("Campo no disponible.")
