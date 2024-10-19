op=""
num1=4
num2=2
resultado=0
while op!=4:
    print("********************************")
    print("0.Suma")
      1.Resta
      2.Multiplicar
      3.Dividir
      print("4.Salir")
    print("*******************************")
    op=input("Elige una opción:")
    if op==0:
        resultado=num1+num2
        print("El resultado es %s "%(resultado))
        
    if op==1:
        resultado=num1-num2
        print("El resultado es %s "%(resultado))
        
    if op==2:
        resultado=num1*num2
        print("El resultado es %s "%(resultado))
        
    if op==3:
        resultado=num1/num2
        print("El resultado es %s "%(resultado))
        
    