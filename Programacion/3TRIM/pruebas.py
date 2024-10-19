import mysql.connector
from claseUsuario import Usuario
from claseBiblioteca import Biblioteca
from claseLibro import Libro

def listarUsuarios(cursor):
        cursor.execute("""
                    SELECT *
                    FROM usuario""")
        resultado = cursor.fetchall()
        return resultado
    
database = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "Samuel21_",
            database = "biblioteca_python"
        )

cursor = database.cursor()



resultado = listarUsuarios(cursor)
usuarios = []
libros = []
for usuario in resultado:
    usuarios.append(Usuario(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4]))
    
miBiblioteca = Biblioteca(None, "Ies Fidiana", "c/ Saturno", libros, usuarios)
    
# for usuario in miBiblioteca.usuarios:
#     print(usuario.nombre)
#     print(usuario.nombreUsuario)
#     print(usuario.rol)
listaUsuarios = miBiblioteca.get_usuarios()

print(listaUsuarios)


libros = [
            Libro(9781234567897, "El Hobbit", "J. R. R. Tolkien", "Novela"),
            Libro(3469346095454, "La sombra del viento", "Carlos Ruiz Zafón", "Novela"),
            Libro(7869246296428, "Cien años de soledad", "Gabriel García Márquez", "Realismo mágico"),
            Libro(6013418701350, "El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela"),
            Libro(1561506150612, "Don Quijote de la Mancha", "Miguel de Cervantes", "Novela clásica"), 
            Libro(8976289328561, "Ficciones", "Jorge Luis Borges", "Cuentos")
        ]