# ******************************************
# Ejercicio 2 del Examen del 3er Trimestre
# Samuel Plaza Sáez
# ******************************************

import mysql.connector
import csv
import hashlib

def hashearContrasenia(password):
        """Este método realiza el hasheo de la contraseña del usuario, 
        ya sea para guardarla o para compararla con la que el usuario ingresa.

        Args:
            password (str): contraseña que se va a hashear

        Returns:
            contraseniaCifrada: contraseña hasheada con cifrado sha256
        """
        hash_obj = hashlib.sha256()
        hash_obj.update(password.encode('utf-8'))
        contraseniaCifrada = hash_obj.hexdigest()
        return contraseniaCifrada

# Leemos el archivo .lst 
with open("routerdefaultpass-combo.lst", "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    # Pedimos usuario y contraseña para la conexion con la BBDD
    usuarioBBDD = input("Usuario para la conexión con la base de datos: ")
    contraseniaBBDD = input("Contraseña para la conexión con la base de datos: ")
    nombreBBDD = input("Nombre de la base de datos: ")

    # Realizamos la conexion con la BBDD con los datos parametrizados
    # cursor.execute()
    database = mysql.connector.connect(
                host = "localhost",
                user = usuarioBBDD,
                passwd = contraseniaBBDD,
                database = nombreBBDD
            )
    cursor = database.cursor()

    # Procedemos a meter los datos del archivo (están almacenados en reader) en la tabla passwords
    for row in reader:
        # Los datos vienen separados por ":", por lo que hacemos una división con ese caracter
        rowSplit = row[0].split(":")
        # Hasheamos la contraseña con la función creada arriba. Va cifrada en sha256
        contrHash = hashearContrasenia(rowSplit[1])
        # Insertamos los datos en la tabla passwords (la base de datos se especifica en la conexión)
        cursor.execute(f"""INSERT INTO passwords values
                        ('{rowSplit[0]}', '{contrHash}')""")
        # Guardamos los cambios hechos en la base de datos
        database.commit()