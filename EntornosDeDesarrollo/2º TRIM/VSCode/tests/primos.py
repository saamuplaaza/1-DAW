def esPrimo(numero):
    if numero > 1:
        for i in range(2,numero):
            if (numero % i) == 0:
                return False
                
        else:
            return True
    else:
        return False
