class Dibujar:
    def menuUI():
        print("------------------MENÚ------------------")
        print("1. Dibujar un rectángulo.")
        print("2. Dibujar un rectángulo con caracter a elegir.")
        print("3. Dibujar triángulo.")
        print("4. Salir.")
        opcionMenu = input("Elija una opción: ")
        return opcionMenu

    def dibujarRectangulo(altura, anchura):
        for y in range(altura):
            print("* " * anchura)

    def rectanguloModificado(altura, anchura, caracter):
        for y in range(altura):
            print((caracter + " ") * anchura)

    def triangulo(anchura):
        for y in range(anchura):
            print("* " * (y + 1))
        for y in range(anchura - 1):
            print("* " * (anchura - y - 1))


def dibujarTriangulo(Dibujar):
    anchura = int(input("Anchura del triángulo: "))
    Dibujar.triangulo(anchura)
    input("Pulse Intro para continuar...")


if __name__ == "__main__":
    while True:
        menu = Dibujar.menuUI()
        if menu == "1":
            altura = int(input("Altura del rectángulo: "))
            anchura = int(input("Anchura del rectángulo: "))
            Dibujar.dibujarRectangulo(altura, anchura)
            input("Pulse Intro para continuar...")

        elif menu == "2":
            altura = int(input("Altura del rectángulo: "))
            anchura = int(input("Anchura del rectángulo: "))
            caracter = input("caracter a utilizar: ")
            Dibujar.rectanguloModificado(altura, anchura, caracter)
            input("Pulse Intro para continuar...")

        elif menu == "3":
            dibujarTriangulo(Dibujar)

        elif menu == "4":
            break
