import os
import hashlib
from datetime import datetime
import sqlite3

def crearUsuario(nif, nombre, apellidos, usuario, contraseniaHasheada, correo, fechaNacimiento, telefono=""):
    cursor.execute("""
        INSERT INTO usuarios VALUES
            (?, ?, ?, ?, ?, ?, ?, ?)
    """, (nif, nombre, apellidos, usuario, contraseniaHasheada, correo, fechaNacimiento, telefono))
    con.commit()
        
def existeNIF(nif):
    for row in cursor.execute("SELECT NIF FROM usuarios"):
        if nif in row:
            return True
    return False

def existeUsuario(usuario):
    for row in cursor.execute("SELECT nombre_de_usuario FROM usuarios"):
        if usuario in row:
            return True
    return False

def existeContrasenia(usuario,contraseniaHasheada):
    for row in cursor.execute("SELECT nombre_de_usuario, contrasenia FROM usuarios"):
        if usuario == row[0]:
            if contraseniaHasheada == row[1]:
                return True
    return False

def modificarUsuario(usuarioCambiar, nif, nombre, apellidos, usuario, contrasenia, correo, fechaNacimiento, telefono):
    lineaUsuario = cursor.execute("""
        SELECT * FROM usuarios 
        WHERE nombre_de_usuario=?
        """, (usuarioCambiar,)).fetchone()
    if nif=="":
        nif=lineaUsuario[0]
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
    if fechaNacimiento=="":
        fechaNacimiento=lineaUsuario[6]
    if telefono=="":
        telefono=lineaUsuario[7]
    cursor.execute("""
        UPDATE usuarios
        SET NIF=?, nombre=?, apellidos=?, nombre_de_usuario=?, contrasenia=?, correo=?, fecha_de_nacimiento=?, telefono=?
        WHERE nombre_de_usuario = ?
                   """, (nif, nombre, apellidos, usuario, contrasenia, correo, fechaNacimiento, telefono, usuarioCambiar))
    con.commit()

def eliminarUsuario(usuarioEliminar):
    cursor.execute("""
        DELETE FROM usuarios
        WHERE nombre_de_usuario = ?
    """, (usuarioEliminar,))
    con.commit()
    
def hashearContrasenia(contrasenia):
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
    row = cursor.execute("""
                        SELECT fecha_de_nacimiento 
                        FROM usuarios
                        WHERE nombre_de_usuario = ?
                        """, (usuario,)).fetchone()
    fechaActual=datetime.now()
    fechaDeNacimiento= row[0]
    fechaNacimiento = datetime.strptime(fechaDeNacimiento, "%d/%m/%Y")
    edad= fechaActual.year - fechaNacimiento.year
    if (fechaActual.month, fechaActual.day) < (fechaNacimiento.month, fechaNacimiento.day):
        edad -= 1
    return edad

def recuperarContraseña(usuario, correo):
    for row in cursor.execute("""
        SELECT nombre_de_usuario, correo 
        FROM usuarios
    """):
        if usuario == row[0]:
            if correo == row [1]:
                return True
    return False

def modificarContrasenia(usuario, contraseniaHasheada):
    cursor.execute("""
        SELECT nombre_de_usuario
        FROM usuarios
        WHERE nombre_de_usuario=?
    """, (usuario,))

    cursor.execute("""
        UPDATE usuarios
        SET contrasenia =?
        WHERE nombre_de_usuario =?
    """, (contraseniaHasheada, usuario))
    con.commit()

def listarUsuario():
    i=1
    for row in cursor.execute("SELECT NIF, nombre, apellidos, nombre_de_usuario, correo, fecha_de_nacimiento, telefono FROM usuarios ORDER BY apellidos"):
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("""Usuario %s""" %i)
        print("NIF:", row[0],"|", "Nombre:", row[1],"|","Apellidos:", row[2],"|","Nombre de usuario:", row[3],"|","Correo electrónico:", row[4],"|","Fecha de nacimiento:", row[5],"|","Teléfono:", row[6])
        i+=1

def mostrarMenuUI():
    print("""

.______      __       ___              .___________..______          ___      .______        ___            __       ___      .__   __.  _______   ______   
|   _  \    / /      |__ \             |           ||   _  \        /   \     |   _  \      /   \          |  |     /   \     |  \ |  | |       \ /  __  \  
|  |_)  |  / /_         ) |            `---|  |----`|  |_)  |      /  ^  \    |  |_)  |    /  ^  \         |  |    /  ^  \    |   \|  | |  .--.  |  |  |  | 
|   ___/  | '_ \       / /                 |  |     |      /      /  /_\  \   |   _  <    /  /_\  \  .--.  |  |   /  /_\  \   |  . `  | |  |  |  |  |  |  | 
|  |      | (_) |  __ / /_                 |  |     |  |\  \----./  _____  \  |  |_)  |  /  _____  \ |  `--'  |  /  _____  \  |  |\   | |  '--'  |  `--'  | 
| _|       \___/  (__)____|  ______        |__|     | _| `._____/__/     \__\ |______/  /__/     \__\ \______/  /__/     \__\ |__| \__| |_______/ \______/  
                            |______|                                                                                                                        
     ______   ______   .__   __.         _______.  ______      __       __  .___________. _______                                                           
    /      | /  __  \  |  \ |  |        /       | /  __  \    |  |     |  | |           ||   ____|                                                          
   |  ,----'|  |  |  | |   \|  |       |   (----`|  |  |  |   |  |     |  | `---|  |----`|  |__                                                             
   |  |     |  |  |  | |  . `  |        \   \    |  |  |  |   |  |     |  |     |  |     |   __|                                                            
   |  `----.|  `--'  | |  |\   |    .----)   |   |  `--'  '--.|  `----.|  |     |  |     |  |____                                                           
    \______| \______/  |__| \__|    |_______/     \_____\_____\_______||__|     |__|     |_______|                                                          
                                                                                                                                                            
                                                                    
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


# Main 
con = sqlite3.connect("usuarios.db")
cursor = con.cursor()
try:
    error = cursor.execute("CREATE TABLE usuarios(NIF, nombre, apellidos, nombre_de_usuario, contrasenia, correo, fecha_de_nacimiento, telefono)")
    print("Tabla creada con éxito")
except sqlite3.OperationalError:
    pass

while True:
    os.system("cls")
    opcionMenu = mostrarMenuUI()
    if opcionMenu=="1": # Crear Usuario
        while True:
            nif = input("NIF: ")

            nifUsado = existeNIF(nif)
            if nifUsado == True:
                print("ERROR: El NIF ya está registrado.")
                input("Pulse Intro para conducir...")
            else:
                nombre = input("Nombre: ")

                apellidos = input("Apellidos: ")

                usuario = input("Nombre de usuario: ")

                usuarioUsado = existeUsuario(usuario)
                if usuarioUsado == True:
                    print("ERROR: Nombre de usuario en uso.")
                    input("Pulse Esc para volver al menú...")
                else:
                    contrasenia = input("Contraseña: ")
                    contraseniaHasheada=hashearContrasenia(contrasenia)

                    correo = input("Correo: ")

                    fechaNacimiento = input("Fecha de nacimiento: ")

                    telefono = input("Teléfono: ")

                    crearUsuario(nif, nombre, apellidos, usuario, contraseniaHasheada, correo, fechaNacimiento, telefono)
                    os.system("cls")
                    print("Usuario creado correctamente.")
                    input("Pulse Intro para volver al menú...")
                    break

    elif opcionMenu=="2": # Modificar Usuario
        usuarioCambiar=input("Introduce el nombre de usuario:")
        contrasenia = input("Contraseña: ")
        contraseniaHasheada=hashearContrasenia(contrasenia)
        usuarioLogueado = loginUsuario(usuarioCambiar, contraseniaHasheada)
        if usuarioLogueado==True:
            os.system("cls")
            nif = input("NIF: ")

            nifUsado = existeNIF(nif)
            if nifUsado == True:
                print("ERROR: El NIF ya está registrado.")
                input("Pulse Intro para conducir...")
            else:
                nombre = input("Nombre: ")

                apellidos = input("Apellidos: ")

                usuario = input("Nombre de usuario: ")

                usuarioUsado = existeUsuario(usuario)
                if usuarioUsado == True:
                    print("ERROR: Nombre de usuario en uso.")
                    input("Pulse Esc para volver al menú...")
                else:
                    contrasenia = input("Contraseña: ")
                    contraseniaHasheada=hashearContrasenia(contrasenia)
                    correo = input("Correo: ")

                    fechaNacimiento = input("Fecha de nacimiento: ")

                    telefono = input("Teléfono: ")

            modificarUsuario(usuarioCambiar, nif, nombre, apellidos, usuario, contraseniaHasheada, correo, fechaNacimiento, telefono)
            os.system("cls")
            print("Usuario modificado correctamente.")
            input("Pulse Intro para volver al menú...")
        else:
            print("Error en la autenticación. Usuario o contraseña incorrectas.")
            input("Pulse Intro para volver al menú...")

    elif opcionMenu=="3": # Eliminar Usuario
        usuarioEliminar=input("Introduce el nombre de usuario:")
        contrasenia = input("Contraseña: ")
        contraseniaHasheada=hashearContrasenia(contrasenia)
        usuarioLogueado = loginUsuario(usuarioEliminar, contraseniaHasheada)
        if usuarioLogueado==True:
            eliminarUsuario(usuarioEliminar)
            os.system("cls")
            print("Usuario eliminado correctamente.")
            input("Pulse Intro para volver al menú...")
        else:
            print("Error en la autenticación. Usuario o contraseña incorrectas.")
            input("Pulse Intro para volver al menú...")

    elif opcionMenu=="4": # Login Usuario
        while True:
            usuario = input("Nombre de usuario: ")
            contrasenia = input("Contraseña: ")
            contraseniaHasheada=hashearContrasenia(contrasenia)
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
            contraseniaHasheada=hashearContrasenia(contrasenia)
            contraseniaNueva = modificarContrasenia(usuario, contraseniaHasheada)
            print("Contraseña modificada correctamente.")
            input("Pulse Intro para volver al menú...")
        else: 
            print("Usuario o correo incorrectos.")
            input("Pulse Intro para volver al menú...")

    elif opcionMenu=="7": # Lista de Usuarios
        ListaUsuarios = listarUsuario()
        input("Pulse Intro para continuar...")

    elif opcionMenu=="0":
        os.system("cls")
        print("Programa finalizado.")
        break

    else:
        print ("Opción no válida.")

con.close()