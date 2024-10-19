import sqlite3
import os

def menuUI():
    print("""
        ------------------------MENÚ---------------------
        1. Buscar persona a través de número de telefono.
        2. Buscar teléfono a través de nombre de persona.
        3. Listar contactos.
        0. Salir
        """)
    
def listarContactos(cursor):
    rows = []
    for row in cursor.execute("""SELECT given_name, number, status FROM wa_contacts"""):
        rows.append(row)
        print(row)
    return rows

def buscarTelefono( telefono, cursor ):
    for nombre in  cursor.execute(f"""
                    SELECT given_name
                    FROM wa_contacts
                    WHERE number = ?
                    """ , (telefono, )):
        if nombre[0] is None:
            pass
        else:
            print(nombre)

def buscarNombre(nombre):
    telefonos = cursor.execute(f"""
                                SELECT number
                                FROM wa_contacts
                                WHERE given_name = ?
                                """(nombre,))
    if telefonos is None:
        return False
    else:
        return telefonos

if __name__ == "__main__":
    con = sqlite3.connect("wa.db")
    cursor = con.cursor()
    while True:
        menuUI()
        opcionMenu =  input("Ingrese una opción: ")
        if opcionMenu == "1":
            telefono = input("Introduzca un número de teléfono: ")
            telf = buscarTelefono(telefono, cursor)
            print(telf)
            input("Pulse Intro para continuar...")
            os.system("cls")
            
        elif opcionMenu == "2":
            nombre = input("Introduzca un nombre: ")
            buscarNombre(nombre)
            input("Pulse Intro para continuar...")
            os.system("cls")
        
        elif opcionMenu == "3":
            listarContactos(cursor)
            input("Pulse Intro para continuar...")
            os.system("cls")
        elif opcionMenu == "4":
            break
        else:
            print("Introduzca una de las opciones del menú.")
            input("Pulse Intro para continuar...")
            os.system("cls")
    