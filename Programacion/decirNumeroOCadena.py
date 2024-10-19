a=input("Dime un número: ")

if isinstance(a,int):
    print("Es un entero")
    print(a+10)
elif isinstance(a,str):
    print("Es una cadena")