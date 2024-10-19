from math import e

print("\n VAMOS A CALCULAR LA FUNCIÓN RELU\n")
x=float(input("Introduce un número: "))

def relu(x):
    '''Calcula el resultado de la función matemática relu.'''
    return max(0,x)

print(relu(x))


print("\nAHORA VAMOS A CALCULAR LA FUNCIÓN SIGMOID\n")

x=float(input("Introduce un número: "))

def sigmoid(x):
    '''Calcula el resultado de la función matemática sigmoid.'''
    y = 1/(1+(e**-x))
    return y
    

print(sigmoid(x))


print("\nAHORA VAMOS A CALCULAR LA FUNCIÓN TANH\n")

x=float(input("Introduce un número: "))

def sinh(x):
    '''Calcula el resultado de la función matemática sinh.'''
    return (((e**x)-(e**-x))/2)

def cosh(x):
    '''Calcula el resultado de la función matemática cosh.'''
    return (((e**x)+(e**-x))/2)

def tanh(x):
    '''Calcula el resultado de la función matemática tanh.'''
    return sinh(x)/cosh(x)
    
print(tanh(x))