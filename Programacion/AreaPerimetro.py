
print("Introduzaca las medidas del rectángulo.")
baseRectangulo=input("Base (cm): ")
baseRectangulo=int(baseRectangulo)
alturaRectangulo=input("Altura (cm): ")
alturaRectangulo=int(alturaRectangulo)
perimetroRectangulo=2*baseRectangulo+2*alturaRectangulo
areaRectangulo=baseRectangulo*alturaRectangulo
print(('''Perímetro Rectágulo: %s
Área Rectágulo: %s'''%(perimetroRectangulo,areaRectangulo)))

print("Ahora introduzca las medidas del triángulo.")

lado1=input("Lado 1 (cm): ")
lado1=int(lado1)
lado2=input("Lado  2(cm): ")
lado2=int(lado2)
lado3Base=input("Base (cm): ")
lado3Base=int(lado3Base)
alturaTriangulo=input("Altura (cm): ")
alturaTriangulo=int(alturaTriangulo)
perimetroTriangulo=lado1+lado2+lado3Base
areaTriangulo=(lado3Base*alturaTriangulo)/2
print('''Perímetro Triángulo: %s
Área Triángulo: %s'''%(perimetroTriangulo,areaTriangulo))