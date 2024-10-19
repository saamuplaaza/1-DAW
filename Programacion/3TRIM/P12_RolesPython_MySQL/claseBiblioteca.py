import hashlib
import mysql.connector
import os

class Biblioteca:
    def __init__(self, id, nombre, direccion, libros = [], usuarios = []):
        """Inicializa los atributos de la clase Biblioteca.

        Args:
            id (int): identificador de la biblioteca
            nombre (str): nombre de la biblioteca
            direccion (str): direccion de la biblioteca
            libros (list): lista de libros que se encuentran en la base de datos
            usuarios (list): lista de usuarios que se encuentran en la base de datos
        """
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.libros = libros
        self.usuarios = usuarios
    
    def set_id(self, id):
        self.id = id
        return self.id
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        return self.nombre
    
    def set_direccion(self, direccion):
        self.direccion = direccion
        return self.direccion
    
    def set_libros(self, libros):
        self.libros = libros
        return self.libros
    
    def set_usuarios(self, usuarios):
        self.usuarios = usuarios
        return self.usuarios
    
    def get_id(self):
        return self.id
    
    def get_nombre(self):
        return self.nombre
    
    def get_direccion(self):
        return self.direccion
    
    def get_libros(self):
        return self.libros
    
    def get_usuarios(self):
        return self.usuarios
    
    def mostrarMenuUI(self, rol):
        """Este método muestra la interfaz de ussuario del programa. Dependiendo del rol 
        que ternga el usuario que ha iniciado sesión se mostrará un menú u otro.
        
        Args:
            rol (str): rol del usuario que ha iniciado sesión

        Returns:
            opcion: primera opción del menú que elige el usuario
            opcionMenu: segunda opción del menú que elige el usuario
        """
        while True:
            if rol == "admin":
                print("""
            ---- MENÚ DE ADMINISTRADOR ----
                1. Gestionar usuarios.
                2. Gestionar libros.
                0. Salir del sistema.
                """)
                opcion = input("Elije una opción: ")
                while True:
                    if opcion == "1":
                        os.system("cls")
                        print("""
            ----MENÚ DE ADMINISTRADOR----
            --- Gestión de usuarios ---
                1. Agregar un nuevo usuario.
                2. Eliminar usuario existente.
                3. Listar usuarios.
                0. Salir.
                """)
                        opcionMenu = input("Elije una opción: ")
                        if opcionMenu == "0":
                            break
                        else:
                            return opcion, opcionMenu
                    elif opcion == "2":
                        os.system("cls")
                        print("""
            ----MENÚ DE ADMINISTRADOR----
            --- Gestión de libros ---
                1. Agregar un nuevo libro.
                2. Eliminar libro existente.
                3. Listar libros.
                0. Salir.
                    """)
                        opcionMenu = input("Elije una opción: ")
                        if opcionMenu == "0":
                            break
                        else:
                            return opcion, opcionMenu
                    elif opcion == "0":
                        return None, None 
                    else:
                        os.system("cls")
                        break
            elif rol == "usuario":
                print("""
            ---- MENÚ DE USUARIO ----
                1. Listar usuarios.
                2. Listar libros.
                0. Salir del sistema.
                """)
                opcion = input("Elije una opción: ")
                while True:
                    if opcion == "0":
                        return None, None
                    elif opcion == "1" or opcion == "2":
                        return opcion, None
                    else:
                        os.system("cls")
                        break

    def iniciarSesion(self):
        """Este método pide los datos para iniciar sesión.
        
        Returns:
            usuario: nombre de usuario introducido
            contraseniaHasheada: contraseña introducida hasheada
        """
        
        usuario = input("\tNombre de usuario: ")
        contrasenia = input("\tContraseña: ")
        contraseniaHasheada = self.hashearContrasenia(contrasenia)
        return usuario, contraseniaHasheada

    def crearTablasBD(self):
        """Este método se conecta a la base de datos con el rol de admin,
        crea las tablas de la base de datos si es necesario e introduce 
        unos datos (si no existen) para que no estén vacias las tablas.
        El usuario 'admin' es obligatorio que esté por lo menos la primera vez 
        para poder acceder al sistema.

        Returns:
            database: conexión con la base de datos
            cursor: cursor de la base de datos
        """
        libros = [
            ("9781234567897", "El Hobbit", "J. R. R. Tolkien", "Novela"),
            ("3469346095454", "La sombra del viento", "Carlos Ruiz Zafón", "Novela"),
            ("7869246296428", "Cien años de soledad", "Gabriel García Márquez", "Realismo mágico"),
            ("6013418701350", "El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela"),
            ("1561506150612", "Don Quijote de la Mancha", "Miguel de Cervantes", "Novela clásica"), 
            ("8976289328561", "Ficciones", "Jorge Luis Borges", "Cuentos")
        ]
        database = mysql.connector.connect(
                    host = "localhost",
                    user = "admin",
                    passwd = "admin",
                    database = "biblioteca_python"
                )
        cursor = database.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS libro (
            isbn varchar(13) not null,
            titulo varchar(40) not null,
            autor varchar(40) not null,
            tipo  varchar(40) not null,
            PRIMARY KEY (isbn)
            )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuario (
            id int auto_increment not null,
            nombre varchar(40) not null, 
            nombre_usuario varchar(40) not null unique, 
            hash_password varchar(64) not null, 
            rol varchar(20) CHECK(rol = 'admin' or rol='usuario'),
            PRIMARY KEY (id)
            )""")
        password = "admin"
        hashAdmin = self.hashearContrasenia(password)
        cursor.execute(f"""
                    INSERT INTO usuario
                    SELECT null, 'admin', 'admin', '{hashAdmin}', 'admin'
                    WHERE NOT EXISTS (SELECT * 
                                    FROM usuario
                                    WHERE nombre_usuario='admin'
                                    AND hash_password='{hashAdmin}')
                    """)
        
        cursor.executemany("""INSERT INTO libro 
                           SELECT %s, %s, %s, %s
                           WHERE (SELECT count(isbn) FROM libro) = 0 """, libros)
        database.commit()
    
        return database, cursor
        
    def conexionesBD(self, datosUsuario):
        """Este método se conecta como root para crear tanto la base de datos como
        los roles que va a tener dicha base de datos. Tras realizar esas operaciones, 
        se conecta con el rol de 'admin' (esta operación se realiza en el método 'crearTablas()')
        y comprueba si el usuario que está intentando iniciar sesión existe o no. Si existe, dependiendo 
        del rol del ususario, realizará una conexión u otra con la base de datos.
        
        Args:
            datosUsuario (list): Nombre de usuario y contraseña del usuario que está iniciando sesión

        Returns:
            database: conexión con la base de datos
            cursor: cursor de la base de datos
            rol: 'usuario' or 'admin'
        """
        database = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "Samuel21_"
        )
        cursor = database.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS biblioteca_python")
        cursor.execute("CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin'")
        cursor.execute("GRANT ALL PRIVILEGES ON biblioteca_python.* TO 'admin'@'localhost' ")
        cursor.execute("CREATE USER IF NOT EXISTS 'usuario'@'localhost' IDENTIFIED BY 'usuario' ")
        cursor.execute("GRANT select ON biblioteca_python.* TO 'usuario'@'localhost' ")

        database, cursor = self.crearTablasBD()
        
        cursor.execute(f"""
                        SELECT nombre_usuario, hash_password
                        FROM usuario
                        WHERE nombre_usuario='{datosUsuario[0]}'
                        AND hash_password='{datosUsuario[1]}'
                        """)
        resultado = cursor.fetchall()
        # Si 'resultado' contiene algo significa que el usuario existe, por lo tanto realizará la conexión.
        if resultado != []:
            cursor.execute(f"""
                            SELECT rol
                            FROM usuario
                            WHERE nombre_usuario = '{datosUsuario[0]}'
                            AND hash_password = '{datosUsuario[1]}'
                            """)
            resultado = cursor.fetchall()
            # Dependiendo del rol, realizaremos una coexión u otra.
            if resultado[0][0] == "usuario":
                database = mysql.connector.connect(
                    host = "localhost",
                    user = "usuario",
                    passwd = "usuario",
                    database = "biblioteca_python"
                )
                cursor = database.cursor()
                return database, cursor, "usuario"
            
            elif resultado[0][0] == "admin":
                database = mysql.connector.connect(
                    host = "localhost",
                    user = "admin",
                    passwd = "admin",
                    database = "biblioteca_python"
                )
                cursor = database.cursor()
                return database, cursor, "admin"
        
        else: # Si no se produce conexión
            return None, None, None
            
    def hashearContrasenia(self, password):
        """Este método realiza el hasheo de la contraseña del usuario, 
        ya sea para guardarla o para compararla con la que el usuario ingresa.

        Args:
            password (str): contraseña que se va a hashear.

        Returns:
            contraseniaCifrada: contraseña hasheada con cifrado sha256
        """
        hash_obj = hashlib.sha256()
        hash_obj.update(password.encode('utf-8'))
        contraseniaCifrada = hash_obj.hexdigest()
        return contraseniaCifrada

    def agregarUsuarioBD(self, database, cursor, usuario):
        """Este método agrega un usuario a la base de datos.

        Args:
            database (class object): conexion con la base de datos.
            cursor (class object): cursor de la base de datos.
            usuario (class object): usuario que vamos a agregar.
        """
        cursor.execute(f"""
                    INSERT INTO usuario
                    SELECT null, '{usuario.nombre}', '{usuario.nombreUsuario}', '{usuario.contraseniaHasheada}', '{usuario.rol}'
                    WHERE NOT EXISTS (SELECT * 
                                    FROM usuario 
                                    WHERE nombre='{usuario.nombre}' 
                                    AND  nombre_usuario='{usuario.nombreUsuario}' 
                                    AND hash_password='{usuario.contraseniaHasheada}' 
                                    AND rol='{usuario.rol}')
                    """)
        database.commit()
        
    def agregarLibroBD(self, database, cursor, libro):
        """Este método agrega un libro a la base de datos.

        Args:
            database (class object): conexion con la base de datos.
            cursor (class object): cursor de la base de datos.
            libro (class object): libro que vamos a agregar.
        """
        cursor.execute(f"""
                    INSERT INTO libro
                    SELECT '{libro.isbn}', '{libro.titulo}', '{libro.autor}', '{libro.tipo}' 
                    WHERE NOT EXISTS (SELECT * 
                                    FROM libro 
                                    WHERE isbn='{libro.isbn}' 
                                    AND titulo='{libro.titulo}' 
                                    AND autor='{libro.autor}' 
                                    AND tipo='{libro.tipo}')
                    """)
        database.commit()
        
    def eliminarUsuarioBD(self, database, cursor, nombreUsuario):
        """Este método elimina un usuario de la base de datos.
        
        Args:
            database (class object): conexion con la base de datos.
            cursor (class object): cursor de la base de datos.
            nombreUsuario (str): nombre del usuario que vamos a eliminar.
        """
        cursor.execute(f"""
                    DELETE FROM usuario
                    WHERE nombre_usuario='{nombreUsuario}'""")
        database.commit()
        
    def eliminarLibroBD(self, database, cursor, nombreLibro):
        """Este método elimina un libro de la base de datos.
        
        Args:
            database (class object): conexion con la base de datos.
            cursor (class object): cursor de la base de datos.
            nombreLibro (str): nombre del libro que vamos a eliminar.
        """
        cursor.execute(f"""
                    DELETE FROM libro
                    WHERE nombre='{nombreLibro}'""")
        database.commit()
        
    def listarUsuariosBD(self, cursor):
        """Este método lista todos los usuarios de la base de datos.
        
        Args: 
            cursor (class object): cursor de la base de datos.
            
        Returns:
            resultado: lista de usuarios.
            """
        cursor.execute("""
                    SELECT *
                    FROM usuario""")
        resultado = cursor.fetchall()
        return resultado

    def listarLibrosBD(self, cursor):
        """Este método lista todos los libros de la base de datos.
        
        Args: 
            cursor (class object): cursor de la base de datos.
            
        Returns:
            resultado: lista de libros.
            """
        cursor.execute("""
                    SELECT *
                    FROM libro""")
        resultado = cursor.fetchall()
        return resultado   