import os
import hashlib
import csv
from datetime import datetime

def crearUsuario(dni, nombre, apellidos, usuario, contraseniaHasheada, correo, rol, fechaNacimiento, telefono="", avatar=""):
    with open("BBDD.csv", "a", newline="", encoding="utf-8") as archivo_csv:
        writer = csv.writer(archivo_csv, delimiter=";")
        writer.writerow([dni, nombre, apellidos, usuario, contraseniaHasheada, correo, rol, fechaNacimiento, telefono, avatar])
        
def existeDNI(dni):
    for row in archivo2:
        if  dni == row[0]:
            return True
    return False

def existeUsuario(usuario):
    for row in archivo2:
        if  usuario == row[3]:
            return True
    return False

def existeContrasenia(usuario,contraseniaHasheada):
    for row in archivo2:
        if usuario == row[3]:
            if contraseniaHasheada == row[4]:
                return True
    return False

def modificarUsuario(usuarioCambiar, dni, nombre, apellidos, usuario, contrasenia, correo, rol, fechaNacimiento, telefono, avatar):
    lista=[]
    for row in archivo2:
        cadena=row[-1]
        cadena=cadena.split("\n")
        row[-1]=cadena[0]
        if usuarioCambiar in row[3]:
            lineaUsuario=row
        elif usuarioCambiar not in row[3]:
            lista.append(row)
    if dni=="":
        dni=lineaUsuario[0]
    if nombre=="":
        nombre=lineaUsuario[1]
    if apellidos=="":
        apellidos=lineaUsuario[2]
    if usuario=="":
        usuario=lineaUsuario[3]
    if contrasenia=="":
        contrasenia=lineaUsuario[4]
    if correo=="":
        correo=lineaUsuario[5]
    if rol=="":
        rol=lineaUsuario[6]
    if fechaNacimiento=="":
        fechaNacimiento=lineaUsuario[7]
    if telefono=="":
        telefono=lineaUsuario[8]
    if avatar=="":
        avatar=lineaUsuario[9]
    usuarioCambiado=[dni, nombre, apellidos, usuario, contrasenia, correo, rol, fechaNacimiento, telefono, avatar]
    lista.append(usuarioCambiado)
    with open("BBDD.csv", "w",newline="", encoding="utf-8") as archivoCSV:
        writer = csv.writer(archivoCSV, delimiter=";")
        writer.writerows(lista)

def eliminarUsuario(usuarioCambiar):
    lista=[]
    for row in archivo2:
        cadena=row[-1]
        cadena=cadena.split("\n")
        row[-1]=cadena[0]
        if usuarioCambiar not in row[3]:
            lista.append(row)
    with open("BBDD.csv", "w",newline="", encoding="utf-8") as archivoCSV:
        writer = csv.writer(archivoCSV, delimiter=";")
        writer.writerows(lista)

def hasheasrContrasenia(contrasenia):
    hash_obj = hashlib.sha256()
    hash_obj.update(contrasenia.encode('utf-8'))
    contraseniaCifrada = hash_obj.hexdigest()
    return contraseniaCifrada

def loginUsuario(usuario, contraseniaHasheada):
    usuarioUsado=existeUsuario(usuario)
    if usuarioUsado==True:
        contraseniaUsada=existeContrasenia(usuario,contraseniaHasheada)
        if contraseniaUsada==True:
            return True
    return False

def comprobarEdad(usuario):
    for row in archivo2:
        if usuario in row[3]:
            fechaActual=datetime.now()
            fechaDeNacimiento= row[7]
            fechaNacimiento = datetime.strptime(fechaDeNacimiento, "%d/%m/%Y")
            edad= fechaActual.year - fechaNacimiento.year
            if (fechaActual.month, fechaActual.day) < (fechaNacimiento.month, fechaNacimiento.day):
                edad -= 1
    return edad

def recuperarContraseña(usuario, correo):
    for row in archivo2:
        if usuario == row[3]:
            if correo == row [5]:
                return True
    return False

def modificarContrasenia(usuario, contraseniaHasheada):
    lista=[]
    for row in archivo2:
        cadena=row[-1]
        cadena=cadena.split("\n")
        row[-1]=cadena[0]
        if usuario in row[3]:
            row[4]= contraseniaHasheada
            lista.append(row)
        elif usuario not in row[3]:
            lista.append(row)
    with open("BBDD.csv", "w",newline="", encoding="utf-8") as archivoCSV:
        writer = csv.writer(archivoCSV, delimiter=";")
        writer.writerows(lista)

def listarUsuario(i, archivo2):
    i=1
    while i < len(archivo2):
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("""Usuario %s""" %i)
        print("DNI:", archivo2[i][0],"|", "Nombre:", archivo2[i][1],"|","Apellidos:", archivo2[i][2],"|","Nombre de usuario:", archivo2[i][3],"|","Correo electrónico:", archivo2[i][5],"|","Rol: ", archivo2[i][6],"|","Fecha de nacimiento:", archivo2[i][7],"|","Teléfono:", archivo2[i][8],"|","Avatar:", archivo2[i][9])
        i+=1

def mostrarMenuUI():
    print("""
  ____        __    _   ____                                           _         _        
 |  _ \      / /_  / | |  _ \ _ __ ___ _ __   __ _ _ __ __ _ _ __   __| | ___   | | __ _  
 | |_) |____| '_ \ | | | |_) | '__/ _ \ '_ \ / _` | '__/ _` | '_ \ / _` |/ _ \  | |/ _` | 
 |  __/_____| (_) || | |  __/| | |  __/ |_) | (_| | | | (_| | | | | (_| | (_) | | | (_| | 
 |_|         \___(_)_| |_|   |_|  \___| .__/ \__,_|_|  \__,_|_| |_|\__,_|\___/  |_|\__,_| 
            _                   _     |_|                                                 
   ___  ___| |_ _ __ _   _  ___| |_ _   _ _ __ __ _   _ __   __ _ _ __ __ _               
  / _ \/ __| __| '__| | | |/ __| __| | | | '__/ _` | | '_ \ / _` | '__/ _` |              
 |  __/\__ \ |_| |  | |_| | (__| |_| |_| | | | (_| | | |_) | (_| | | | (_| |              
  \___||___/\__|_|   \__,_|\___|\__|\__,_|_|  \__,_| | .__/ \__,_|_|  \__,_|              
             _   ____  ____  ____  ____              |_|                                  
   _ __ ___ (_) | __ )| __ )|  _ \|  _ \                                                  
  | '_ ` _ \| | |  _ \|  _ \| | | | | | |                                                 
  | | | | | | | | |_) | |_) | |_| | |_| |                                                 
  |_| |_| |_|_| |____/|____/|____/|____/                                                  
                                                                                                                                                
""")
    print("\t1. Crear Usuario\n")
    print("\t2. Modificar Usuario\n")
    print("\t3. Eliminar Usuario\n")
    print("\t4. Login Usuario\n")
    print("\t5. Comprobar Edad\n")
    print("\t6. Recuperar contraseña\n")
    print("\t7. Lista de Usuarios\n")
    print("\t0. Salir\n")
    print("-----------------------------------------------------------------------------------------------------------")
    opcion=input("Elija una opción: ")
    print("-----------------------------------------------------------------------------------------------------------\n")
    return opcion

def leerFichero():
    ficheroLectura = open("BBDD.csv", "r",encoding="utf-8")
    fichero = ficheroLectura.readlines()
    return fichero


# Main 
archivo = leerFichero()
i=0 
archivo2 = []
while i < len(archivo):
    archivoDividido = archivo[i].split(";")
    archivo2.append(archivoDividido)
    i+=1
while True:
    os.system("cls")
    opcionMenu = mostrarMenuUI()
    if opcionMenu=="1": # Crear Usuario
        dni = input("DNI: ")
        dniUsado = existeDNI(dni)
        if dniUsado == True:
            print("El DNI ya está registrado.")
        else:
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            usuario = input("Nombre de usuario: ")
            usuarioUsado = existeUsuario(usuario)
            if usuarioUsado == True:
                print("Ya hay un usuario con ese nombre.")
            else:
                contrasenia = input("Contraseña: ")
                contraseniaHasheada=hasheasrContrasenia(contrasenia)
                correo = input("Correo: ")
                rol = input("Rol (Admin/Estándar): ")
                fechaNacimiento = input("Fecha de nacimiento: ")
                telefono = input("Teléfono: ")
                avatar = input("Avatar: ")
                crearUsuario(dni, nombre, apellidos, usuario, contraseniaHasheada, correo, rol, fechaNacimiento, telefono, avatar)
                os.system("cls")
                print("Usuario creado correctamente.")
                input("Pulse Intro para volver al menú...")
    elif opcionMenu=="2": # Modificar Usuario
        usuarioCambiar=input("Introduce el nombre de usuario:")
        contrasenia = input("Contraseña: ")
        contraseniaHasheada=hasheasrContrasenia(contrasenia)
        usuarioLogueado = loginUsuario(usuarioCambiar, contraseniaHasheada)
        if usuarioLogueado==True:
            os.system("cls")
            dni = input(" DNI: ")
            dniUsado = existeDNI(dni)
            if dniUsado == True:
                print("El DNI ya está registrado.")
            else:
                nombre = input("Nombre: ")
                apellidos = input("Apellidos: ")
                usuario = input("Nombre de usuario: ")
                usuarioUsado = existeUsuario(usuario)
                if usuarioUsado == True:
                    print("Ya hay un usuario con ese nombre.")
                else:
                    contrasenia = input("Contraseña: ")
                    contraseniaHasheada=hasheasrContrasenia(contrasenia)
                    correo = input("Correo: ")
                    rol = input("Rol (Admin/Estándar): ")
                    fechaNacimiento = input("Fecha de nacimiento(DD/MM/AAAA): ")
                    telefono = input("Teléfono: ")
                    avatar = input("Avatar: ")
            modificarUsuario(usuarioCambiar, dni, nombre, apellidos, usuario, contraseniaHasheada, correo, rol, fechaNacimiento, telefono, avatar)
            os.system("cls")
            print("Usuario modificado correctamente.")
            input("Pulse Intro para volver al menú...")
        else:
            print("Error en la autenticación. Usuario o contraseña incorrectas.")
    elif opcionMenu=="3": # Eliminar Usuario
        usuarioCambiar=input("Introduce el nombre de usuario:")
        eliminarUsuario(usuarioCambiar)
        os.system("cls")
        print("Usuario eliminado correctamente.")
        input("Pulse Intro para volver al menú...")
    elif opcionMenu=="4": # Login Usuario
        while True:
            usuario = input("Nombre de usuario: ")
            contrasenia = input("Contraseña: ")
            contraseniaHasheada=hasheasrContrasenia(contrasenia)
            usuarioLogueado = loginUsuario(usuario, contraseniaHasheada)
            if usuarioLogueado==True:
                print("Acceso permitido.")
                input("Pulse Intro para volver al menú...")
                break
            else:
                print("Error en la autenticación. Usuario o contraseña incorrectas.")
    elif opcionMenu=="5": # Comprobar Edad
        usuario = input("Nombre de usuario: ")
        edadUsuario = comprobarEdad(usuario)
        print("Tienes %s años." %edadUsuario)
        input("Pulse Intro para volver al menú...")
    elif opcionMenu=="6": # Recuperar Contraseña
        usuario = input("Nombre de usuario: ")
        correo = input("Correo: ") 
        contraseniaRecuperada= recuperarContraseña(usuario, correo)
        if contraseniaRecuperada == True:
            contrasenia = input("Contraseña nueva: ")
            contraseniaHasheada=hasheasrContrasenia(contrasenia)
            contraseniaNueva = modificarContrasenia(usuario, contraseniaHasheada)
            print("Contraseña modificada correctamente.")
            input("Pulse Intro para volver al menú...")
    elif opcionMenu=="7": # Lista de Usuarios
        ListaUsuarios = listarUsuario(i, archivo2)
    elif opcionMenu=="0":
        os.system("cls")
        print("Programa finalizado.")
        break
    else:
        print ("Opción no válida.")