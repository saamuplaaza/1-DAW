def funcion():
    print("Frase 1 dentro de funcion")
    return
    print("Frase 2 dentro de funcion")#Esta linea no la lee pq está después del return.
print("Frase 1 fuera de la funcion")
funcion()
print ("Frase 2 fuera de la funcion")



def funcion():
    return "Valor de funcion2"
    print("Esta sentencia nunca va a ejecutarse")
var=funcion()
var2=funcion()[0:5]
print(var)
print (var2)
print(funcion()[0:5])



def funcion():
    return
var=funcion()
print(var)



def funcion():
    return "texto1","texto2","texto3"
var,var2,var3=funcion()
print(var)
print(var2)
print(var3)



def funcion():
    '''Esto es un docstring de la funcion'''
    print("HOLA")
funcion()

def funcion2(arg1=0.0, arg2=0.0):
    '''Esto es una funcion para demostrar qué es un docstring
    
    Keywords arguments:
    arg1 -- primer argumento de la funcion (por defecto 0.0)
    arg2 -- segundo argumento de la funcion (por defecto 0.0)
    '''
    print (arg1)
    return arg2
funcion2()

