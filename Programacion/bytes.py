cadena_bytes= b'\x02\x1f' #Representado por dos digitos exadecimales
print(cadena_bytes)
print(bin(543))
print(hex(543))

cadena_bytes2= bytes(3)
print(cadena_bytes2)
print(b'\x41\x42\x43')  #Imprime A, B y C en ASCII

texto_bytes= b'Hola mundo'
print(texto_bytes)
print(int.from_bytes(b'\x41', "big"))

cadena_bytes3= b'\x20\x19\x61\x62\x39\x40'
print(cadena_bytes3[2])
print(cadena_bytes3[2:5])
print(cadena_bytes3[0::2])

cad1= bytearray(b'\x20\x19\x61\x62\x39\x40')
print(cad1)
cad1[0:1] = b'8'
print(cad1)
cad1[2] = ord('h')
print(cad1)