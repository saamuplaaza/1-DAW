
import requests
import random
# import json
import os

class Persona:
    """Esta clase representa una persona. Tiene los atributos  nombre, edad y DNI."""
    def __init__(self, nombre =  "", edad=0, dni=""):
        """Inicializa los atributos de instancia.

        Args:
            nombre (str): nombre de la persona.
            edad (int): edad de la persona.
            dni (str): dni de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
    def set_nombre(self, nombre):
        """Este método establece el nombre de la persona."""
        self.nombre = nombre
        return self.nombre
    
    def get_nombre(self):
        """Este método devuelve el nombre de la persona."""
        return self.nombre
    
    def set_edad(self, edad):
        """Este método establece la edad de la persona."""
        self.edad = edad
        return self.edad
    
    def get_edad(self):
        """Este método devuelve la edad de la persona."""
        return self.edad
    
    def set_dni(self, dni):
        """Este método establece el DNI de la persona."""
        self.dni = dni
        return self.dni
    
    def get_dni(self):
        """Este método devuelve el DNI de la persona."""
        return self.dni
    
    def mostrarDatosUI(self):
        print(f"""
    Nombre: {self.nombre}
    Edad: {self.edad}
    DNI: {self.dni}
              """)
        
    def esMayorDeEdad(self):
        if self.edad >=18:
            return True
        else:
            return False


class Cuenta(Persona):
    """Esta  clase representa a una cuenta bancaria."""
    def __init__(self, titular, cantidad=0):
        """Inicializa los atributos de instancia.

        Args:
            iban (str): es el iban de la cuenta bancaria. Se genera de forma aleatoria.
            titular (str): es la persona que tiene esta cuenta.
            cantidad (float): es la cantidad de dinero en la cuenta.
        """
        super().__init__()
        # self.iban = requests.get("https://api.generadordni.es/v2/bank/account?results=1").text.split(",")[3].split(":")[1].replace("\"", "")
        self.iban = "ES60 4567 2345 34"
        self.titular = dicPersonas[f"persona{i}"]
        self.cantidad = cantidad
        
    def set_iban(self, iban):
        self.iban = iban
        return self.iban
    
    def get_iban(self):
        return self.iban
    
    def set_titular(self, titular):
        self.titular = titular
        return self.titular
    
    def get_titular(self):
        return self.titular
    
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
        return self.cantidad
    
    def get_cantidad(self):
        return self.cantidad
        
    def mostrarDatosUI(self):
        print(f"""
    IBAN: {self.iban}
    Titular:
        -Nombre: {self.titular.nombre}
        -Edad: {self.titular.edad}
        -DNI: {self.titular.dni}
    Saldo disponible: {self.cantidad}€
    """)
        
    def ingresar(self, cantidad):
        if cantidad < 0:
            print(f"No se puede ingresar una cantidad negativa ({cantidad}€).")
        else:
            self.cantidad += cantidad
            print(f"Se ha ingresado {cantidad}€ a tu cuenta.")
            
    def retirar(self, cantidad):
        if cantidad > self.cantidad:
            print("No puede retirar más dinero del que tienes en la cuenta.")
        elif cantidad < 0:
            print("La cantidad de retiro debe ser positiva.")
        else:
            self.cantidad -= cantidad
            print(f"Se ha retirado {cantidad}€ de tu cuenta.")
            
            
class CuentaJoven(Cuenta):
    """Esta clase representa una cuenta joven."""
    def __init__(self, titular, cantidad=0):
        """Inicializa los atributos del padre."""
        super().__init__(titular, cantidad)
        self.bonificacion = random.randrange(3,8)
        
    def set_bonificacion(self, bonificacion):
        """Este método establece la bonificación de la cuenta joven"""
        self.bonificacion = bonificacion
        return self.bonificacion
    
    def get_bonificacion(self):
        """Este método devuelve la bonificacion de la cuenta joven"""
        return self.bonificacion
    
    def esTitularValido(self):
        if dicPersonas[f"persona{i}"].edad >=18 and dicPersonas[f"persona{i}"].edad <26:
            return True
        else:
            return False
    
    def ingresar(self, cantidad):
        if cantidad < 0:
            print(f"No se puede ingresar una cantidad negativa ({cantidad}€).")
        else:
            self.cantidad += cantidad +(cantidad * (self.get_bonificacion()/100))
            print(f"Se ha ingresado {cantidad}€ a tu cuenta.")
    
    def retirar(self, cantidad):
        if self.esTitularValido() == True:    
            if cantidad > self.cantidad:
                print("No puede retirar más dinero del que tienes en la cuenta.")
            elif cantidad < 0:
                print("La cantidad de retiro debe ser positiva.")
            else:
                self.cantidad -= cantidad
                print(f"Se ha retirado {cantidad}€ de tu cuenta.")
        else: 
            print("Lo siento, el titular no es válido para esta cuenta.")
            
    def mostrarDatosUI(self):
        print(f"""
                    CUENTA JÓVEN
    IBAN: {self.iban}
    Titular:
        -Nombre: {self.titular.nombre}
        -Edad: {self.titular.edad}
        -DNI: {self.titular.dni}
    Saldo disponible: {self.get_cantidad()}€
    Bonificación: {self.get_bonificacion()}%
    """)
        
def mostrarMenuUI():
    os.system("cls")
    print("""
.______     ___                 .______     ______     ______                  __    __   _______ .______       _______ .__   __.   ______  __       ___      
|   _  \   / _ \                |   _  \   /  __  \   /  __  \                |  |  |  | |   ____||   _  \     |   ____||  \ |  |  /      ||  |     /   \     
|  |_)  | | (_) |     ______    |  |_)  | |  |  |  | |  |  |  |     ______    |  |__|  | |  |__   |  |_)  |    |  |__   |   \|  | |  ,----'|  |    /  ^  \    
|   ___/   \__, |    |______|   |   ___/  |  |  |  | |  |  |  |    |______|   |   __   | |   __|  |      /     |   __|  |  . `  | |  |     |  |   /  /_\  \   
|  |         / /                |  |      |  `--'  | |  `--'  |               |  |  |  | |  |____ |  |\  \----.|  |____ |  |\   | |  `----.|  |  /  _____  \  
| _|        /_/                 | _|       \______/   \______/                |__|  |__| |_______|| _| `._____||_______||__| \__|  \______||__| /__/     \__\ 
""")
    print("\n------------------------------------------------MENÚ-------------------------------------------------------\n")
    print("\t1. Crear cuenta\n")
    print("\t2. Ingresar dinero\n")
    print("\t3. Retirar dinero\n")
    print("\t4. Mostrar datos de mi cuenta\n")
    print("\t0. Salir\n")
    print("-----------------------------------------------------------------------------------------------------------")
    opcion=input("Elija una opción: ")
    print("-----------------------------------------------------------------------------------------------------------\n")
    return opcion

if __name__ == "__main__":
    dicPersonas = {}
    dicCuentas = {}
    while True:
        i = len(dicCuentas)+1
        opcionMenu = mostrarMenuUI()
        if opcionMenu =="1":
            nombre = input("Nombre: ")
            try:
                edad = int(input("Edad: "))
            except ValueError:
                print("Introduce una edad válida.")
            
            else:
                dni = input("DNI: ")
                dicPersonas [f"persona{i}"] = Persona(nombre, edad, dni)
                if CuentaJoven.esTitularValido(edad):
                    quiereCuentaJoven = input("¿Quiere crear una cuenta jóven? (si/no): ").lower()
                    if quiereCuentaJoven == "si":
                        dicCuentas [f"cuenta{i}"] = CuentaJoven(nombre)
                    else: 
                        dicCuentas [f"cuenta{i}"] = Cuenta(nombre)
                else:
                    dicCuentas [f"cuenta{i}"] = Cuenta(nombre) 
                dicCuentas[f"cuenta{i}"].mostrarDatosUI()
                datos_json= {
                    f"persona{i}": dicPersonas[f"persona{i}"],
                    f"cuenta{i}": dicCuentas[f"cuenta{i}"]
                }
                print("Cuenta creada correctamente.")
                input("Pulse Intro para continuar...")
            
        elif opcionMenu == "2":
            iban = input("Introduzca el iban de su cuenta: ")
            nombre = input("Nombre: ")
            for clave in dicCuentas.values():
                nombreAcceso = clave.titular.get_nombre()
                ibanAcceso = clave.get_iban()
                if nombreAcceso == nombre and ibanAcceso == iban:
                    cantidad = int(input("¿Cuánto dinero desea ingresar?\n"))
                    clave.ingresar(cantidad)
                    input("Pulse Intro para continuar...")
                    break
        
        elif opcionMenu == "3":
            i=0
            iban = input("Introduzca el iban de su cuenta: ")
            nombre = input("Nombre: ")
            for clave in dicCuentas.values():
                nombreAcceso = clave.titular.get_nombre()
                ibanAcceso = clave.get_iban()
                i+=1
                if nombreAcceso == nombre and ibanAcceso == iban:
                    cantidad = int(input("¿Cuánto dinero desea retirar?\n"))
                    clave.retirar(cantidad)
                    input("Pulse Intro para continuar...")
                    break
        
        elif opcionMenu == "4":
            y=0
            iban = input("Introduzca el iban de su cuenta: ")
            nombre = input("Nombre: ")
            for clave in dicCuentas.values():
                y+=1
                nombreAcceso = clave.titular.get_nombre()
                ibanAcceso = clave.get_iban()
                if nombreAcceso == nombre and ibanAcceso == iban:
                    dicCuentas[f"cuenta{y}"].mostrarDatosUI()
        elif opcionMenu == "0":
            break


    
    