import fichero1, fichero2, fichero3, fichero4

def menu():
    """Esta función muestra por pantalla el menú."""
    print("""
        1. Mostrar tiempo en segundos
        2. Mostrar tiempo en formato h:m:s
        3. Mostrar información factura.
        4. Tiempo total consumido y coste total
        5. Salir""")
    opcion = input("Introduce una opción: ")
    return opcion

if  __name__ == "__main__": 
    """El main llama a las funciones que necesita para poder ejecutar la aplicación
    """
    while True:
        opcionMenu = menu()
        if opcionMenu == "1":
            horasTotales = 0
            minutosTotales = 0
            segundosTotales = 0
            for datos in range(3):
                horas = int(input("horas: "))
                minutos = int(input("minutos: "))
                segundos = int(input("segundos: "))
                horasTotales = horasTotales + horas
                minutosTotales = minutosTotales + minutos
                segundosTotales = segundosTotales + segundos
            solucion = fichero1.calculoSegundos(horasTotales, minutosTotales, segundosTotales)
            print(f"La suma de las horas, los minutos y los segundos es {solucion} segundos")
            input("Pulsa Intro para continuar...")

        elif opcionMenu == "2":
            horasTotales = 0
            minutosTotales = 0
            segundosTotales = 0
            for datos in range(3):
                horas = int(input("horas: "))
                minutos = int(input("minutos: "))
                segundos = int(input("segundos: "))
                horasTotales = horasTotales + horas
                minutosTotales = minutosTotales + minutos
                segundosTotales = segundosTotales + segundos
            solucion = fichero2.calculoTiempo(horasTotales, minutosTotales, segundosTotales)
            print(f"Tiempo total: {solucion[0]}h: {solucion[1]}min: {solucion[2]}s")
            input("Pulsa Intro para continuar...")
            
        elif opcionMenu == "3":
            precio = float(input("¿Cuánto cuesta 1 segundo de comunicación?: "))
            numLlamadas = int(input("¿Cuántas llamadas hay que facturar?: "))
            for facturas in range(numLlamadas):
                horas = int(input("¿Cuántas horas?: "))
                minutos = int(input("¿Cuántos minutos?: "))
                segundos = int(input("¿Cuántos segundos?: "))
                datos = fichero3.factura(horas, minutos, segundos, precio)
                print(f"Duración: {datos[0]} segundos. Coste: {datos[1]}€")
                input("Pulsa Intro para continuar...")
        elif opcionMenu == "4":
            h = 0
            m = 0
            s = 0
            costeTotal = 0
            precio = float(input("¿Cuánto cuesta 1 segundo de comunicación?: "))
            numLlamadas = int(input("¿Cuántas llamadas hay que facturar?: "))
            for facturas in range(numLlamadas):
                horas = int(input("¿Cuántas horas?: "))
                minutos = int(input("¿Cuántos minutos?: "))
                segundos = int(input("¿Cuántos segundos?: "))
                h, m, s = (h+horas), (m+minutos), (s+segundos)
                datos = fichero4.factura(horas, minutos, segundos, precio)
                costeTotal = costeTotal + datos[1]
                costeTotal = round(costeTotal, 2)
                print(f"Duración: {datos[0]} segundos. Coste: {datos[1]}€")
            print(f"Duración total: {h}h {m}min {s}s")
            print(f"Coste total: {costeTotal} €")
            input("Pulsa Intro para continuar...")
        elif opcionMenu == "5":
            break