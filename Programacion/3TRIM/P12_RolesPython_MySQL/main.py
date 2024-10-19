from claseBiblioteca import Biblioteca
from claseUsuario import Usuario
from claseLibro import Libro
import os
import time

if __name__ == "__main__":    
    while True:
        # Creo un array vacío en el que voy a guardar los libros que contenga la BBDD y los que añada nuevos.
        # libros = []
        # Creo un array vacío en el que voy a guardar los usuarios que contenga la BBDD y los que añada nuevos.
        # usuarios = []
        miBiblioteca = Biblioteca(None, "Ies Fidiana", "c/ Saturno")
            
        # Creo el objeto miBblioteca.
        # miBiblioteca = Biblioteca(None, "Ies Fidiana", "c/ Saturno", libros, usuarios)
        os.system("cls")
        print("    -----INICIO DE SESIÓN-----")
        # Pedimos los datos al usuario para iniciar sesión con el método de la clase.
        datosUsuario = miBiblioteca.iniciarSesion()
        print(("Conectando con la base de datos..."))
        time.sleep(0.5)
        # Inicializamos la BBDD 
        try:
            database, cursor, rolConnection = miBiblioteca.conexionesBD(datosUsuario)
        except:
            print("No se ha podido conectar con la base de datos de la biblioteca.")
            print("Asegurese de que tiene el servicio de MySql activo.")
            time.sleep(3)
        else:
            if (database or cursor) == None:
                print("Usuario o contraseña incorrectos. Inténtelo de nuevo.")
                time.sleep(2)
                os.system("cls")
            else:
                # Listo los usuarios y libros haciendo un 'SELECT' en la BBDD.
                listaUsuariosBD = miBiblioteca.listarUsuariosBD(cursor)
                listarLibrosBD = miBiblioteca.listarLibrosBD(cursor)
                
                # Añado los usuarios y los libros a las listasque tenía creadas.
                for usuario in listaUsuariosBD:
                    miBiblioteca.usuarios.append(Usuario(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4]))
                
                for libro in listarLibrosBD:
                    miBiblioteca.libros.append(Libro(libro[0], libro[1], libro[2], libro[3]))
            
                os.system("cls")
                print("BIENVENIDO AL SISTEMA")
                while True:
                    opcion1, opcion2 = miBiblioteca.mostrarMenuUI(rolConnection)
                    if rolConnection == "admin" and opcion1 == "1" and opcion2 == "1": # Agregar Usuario (administrador)
                        while True:
                            os.system("cls")
                            print("AÑADIR USUARIO")
                            # Introducimos los datos del usuario que vamos a añadir.
                            nombre = input("Nombre: ").title()
                            nombreUsuario = input("Nombre de usuario: ").lower()
                            listaNombreUsuarios = []
                            for usuario in miBiblioteca.usuarios:
                                listaNombreUsuarios.append(usuario.nombreUsuario)
                            if nombreUsuario in listaNombreUsuarios:
                                print("El nombre de usuario ya existe.")
                                time.sleep(2)
                                os.system("cls")
                                break
                            else:
                                contrasenia = input("Contraseña: ")
                                contraseniaHasheada = miBiblioteca.hashearContrasenia(contrasenia)
                                rol = input("Rol (admin/usuario): ").lower()
                                if rol != "admin" and rol != "usuario":
                                    print("El rol introducido no es correcto.")
                                    time.sleep(2)
                                    os.system("cls")
                                    break
                                # Creamos el objeto usuario.
                                usuario = Usuario(None, nombre, nombreUsuario, contraseniaHasheada, rol)
                                # Añadimos el usuario a la BBDD y al array de usuarios.
                                miBiblioteca.agregarUsuarioBD(database, cursor, usuario)
                                miBiblioteca.usuarios.append(usuario)
                                print("Usuario agregado satisfactoriamente a la base de datos.")
                                input("Pulse Intro para continuar...")
                                os.system("cls")
                                break
                        
                    elif rolConnection == "admin" and opcion1 == "1" and opcion2 == "2": # Eliminar Usuario (administrador)
                        os.system("cls")
                        # Pedimos los datos del usuario que queremos eliminar.
                        nombreUsuario = input("Nombre de usuario que desea eliminar: ").lower()
                        opcion = input(f"¿Está seguro de que desea eliminar al usuario '{nombreUsuario}'?(s/N): ").lower()
                        if opcion == "s":
                            listaNombreUsuarios = []
                            for usuario in miBiblioteca.usuarios:
                                listaNombreUsuarios.append(usuario.nombreUsuario)
                            if nombreUsuario not in listaNombreUsuarios:
                                print(f"El usuario \"{nombreUsuario}\" no existe.")
                                time.sleep(2)
                                os.system("cls")
                            else:
                                # Eliminamos el usuario de la BBDD y del array de usuarios.
                                miBiblioteca.eliminarUsuarioBD(database, cursor, nombreUsuario)
                                for usuarioEliminar in miBiblioteca.usuarios:
                                    if usuarioEliminar.nombreUsuario == nombreUsuario:
                                        miBiblioteca.usuarios.remove(usuarioEliminar)
                                        break
                                print("Usuario eliminado con éxito.")
                                input("Pulse Intro para continuar...")
                        os.system("cls")
                        
                    elif rolConnection == "admin" and opcion1 == "1" and opcion2 == "3": # Listar Usuarios (administrador)
                        os.system("cls")
                        for usuario in miBiblioteca.usuarios:
                            print(f"""
    Nombre: {usuario.nombre}
    Nombre de usuario: {usuario.nombreUsuario}
    Contraseña hasheada: {usuario.contraseniaHasheada}
    Rol: {usuario.rol}\n""")
                        input("Pulse Intro para continuar...")
                        os.system("cls")
                        
                    elif rolConnection == "admin" and opcion1 == "2" and opcion2 == "1": # Agregar Libro (administrador)
                        while True:
                            os.system("cls")
                            isbn = input("ISBN: ")
                            listaIsbnLibros = []
                            for libro in miBiblioteca.libros:
                                listaIsbnLibros.append(libro.isbn)
                            if isbn in listaIsbnLibros:
                                print("Ya existe un libro con el mismo ISBN.")
                                time.sleep(2)
                                os.system("cls")
                                break
                            else:
                                nombre = input("Nombre: ").title()
                                autor = input("Nombre del autor: ").title()
                                tipo = input("Género: ").capitalize()
                                libro = Libro(isbn, nombre, autor, tipo)
                                miBiblioteca.agregarLibroBD(cursor, libro)
                                miBiblioteca.libros.append(libro)
                                print("Libro agregado satisfactoriamente a la base de datos.")
                                input("Pulse Intro para continuar...")
                                os.system("cls")
                                
                    elif rolConnection == "admin" and opcion1 == "2" and opcion2 == "2": # Eliminar Libro (administrador)
                        os.system("cls")
                        # Pedimos los datos del libro que queremos eliminar.
                        nombreLibro = input("Nombre de libro que desea eliminar: ").title()
                        opcion = input(f"¿Está seguro de que desea eliminar el libro '{nombreLibro}'?(s/N): ").lower()
                        if opcion == "s":
                            listaNombreLibros = []
                            for libro in miBiblioteca.libros:
                                listaNombreLibros.append(libro.isbn)
                            if nombreLibro not in listaNombreLibros:
                                print("El libro no existe.")
                                time.sleep(2)
                                os.system("cls")
                            else:
                                # Eliminamos el libro de la BBDD y del array de libros.
                                miBiblioteca.eliminarLibroBD(database, cursor, nombreLibro)
                                for libroEliminar in miBiblioteca.libros:
                                    if libroEliminar.isbn == nombreLibro:
                                        miBiblioteca.libros.remove(libroEliminar)
                                        break
                                print("Libro eliminado con éxito.")
                                input("Pulse Intro para continuar...")
                        os.system("cls")
                    
                    elif rolConnection == "admin" and opcion1 == "2" and opcion2 == "3": # Listar Libros (administrador)
                        os.system("cls")
                        resultado = miBiblioteca.listarLibrosBD(cursor)
                        for libros in resultado:
                            print(f"""
    ISBN: {libros[0]}
    Nombre: {libros[1]}
    Autor: {libros[2]}
    Tipo: {libros[3]}
                                """)
                        input("Pulse Intro para continuar...")
                        os.system("cls")
                    elif opcion1 == None and opcion2 == None:
                        break
                    
                    elif rolConnection == "usuario" and opcion1 == "1": # Listar Usuarios (usuario)
                        os.system("cls")
                        resultado = miBiblioteca.listarUsuariosBD(cursor)
                        for usuarios in resultado:
                            print(f"""
    ID: {usuarios[0]}
    Nombre: {usuarios[1]}
    Nombre de usuario: {usuarios[2]}
    Contraseña hasheada: {usuarios[3]}
    Rol: {usuarios[4]}""")
                        input("Pulse Intro para continuar...")
                        os.system("cls")
                        
                    elif rolConnection == "usuario" and opcion1 == "2": # Listar Libros (usuario)
                        os.system("cls")
                        resultado = miBiblioteca.listarLibrosBD(cursor)
                        for libros in resultado:
                            print(f"""
    ISBN: {libros[0]}
    Nombre: {libros[1]}
    Autor: {libros[2]}
    Tipo: {libros[3]}
                                """)
                        input("Pulse Intro para continuar...")
                        os.system("cls")