import mysql.connector

# Conexión
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

# print(database)

# Cursor
cursor = database.cursor()

# Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# cursor.execute("SHOW DATABASES")

# for bd in cursor:
#     print(bd)
    
cursor.execute("""
                CREATE TABLE IF NOT EXISTS vehiculo(
                    id int(10) auto_increment not null,
                    marca varchar(40) not null,
                    modelo varchar(40) not null,
                    precio float(10,2) not null,
                    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
                )""")

# cursor.execute("SHOW TABLES")

# for tabla in cursor:
#     print(tabla)

# cursor.execute("""
#                INSERT INTO vehiculo values
#                (null, 'Opel', 'Astra', 18500)
#                """)

# coches = [
#     ("Seat", "Ibiza", 5000),
#     ("Renault", "Clio", 15000),
#     ("Citroen", "Saxo", 2000),
#     ("Mercedes", "Clase C", 35000)
# ]

# Insertar datos en la tabla
# cursor.executemany("INSERT INTO vehiculo VALUES (null, %s, %s, %s)", coches)
# database.commit()


# Leer datos de una tabla
# cursor.execute("""
#                SELECT marca, precio 
#                FROM vehiculo
#                WHERE precio <= 5000 
#                AND marca = 'Seat'
#                """)

# result = cursor.fetchall()
# for coche in result:
#     print(coche[0], coche[1])
    
cursor.execute("""
                DELETE FROM vehiculo
                WHERE marca = 'Seat'
                """)
database.commit()
    
print(cursor.rowcount, "borrados")
