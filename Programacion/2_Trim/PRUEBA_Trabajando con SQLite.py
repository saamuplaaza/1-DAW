# -----------------------------------------------
#   Nombre:Samuel Plaza Sáez
#   Curso: 1º DAW
#   Título: PRÁCTICA 6.2: Trabajando con SQLite
# -----------------------------------------------

import os
import sqlite3

def crearTabla(cursor):
    error=cursor.execute("CREATE TABLE %s ()")

def mostrarMenuUI():
    os.system("cls")
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
    print("-----------------------------------------------------------------------------------------------------------\n")
    print("\n------------------------------------------------MENÚ-------------------------------------------------------\n")
    print("\t1. Crear tabla\n")
    print("\t2. Añadir a tabla\n")
    print("\t3. Consultar tabla\n")
    print("\t0. Salir\n")
    print("-----------------------------------------------------------------------------------------------------------")
    opcion=input("Elija una opción: ")
    print("-----------------------------------------------------------------------------------------------------------\n")
    return opcion


# Main
con = sqlite3.connect("P6_SQLite.db")
cursor = con.cursor()
opcionMenu = mostrarMenuUI()
while True:
    # if opcionMenu == "":
    #     print("Debes elegir una de las opciones del menú.")
    #     input("Pulsa Intro para continuar...")
    # elif opcionMenu == "1": # Crear tabla
    #     nombreTabla = input("Nombre de la tabla: ")
    #     try:
    #         numeroCol = input("Número de columnas:")
    #         numeroCol = int(numeroCol)
    #     except ValueError:
    #         print("ERROR: Debes introducir un número entero de columnas.")
    #     columnas=[]
    #     for i in range(numeroCol):
    #         columna = input("Columana %s: " %(i+1))
    #         columnas.append(columna)
    try:
        error = cursor.execute("CREATE TABLE movie(titulo, anio, puntuacion)")
    except sqlite3.OperationalError:
        pass

    input("1...")
    res = cursor.execute("SELECT name FROM sqlite_master")
    res.fetchone()

    input("2...")
    cursor.execute("""
        INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2),
            ('And Now for Something Completely Different', 1971, 7.5)
    """)
    con.commit()

    res = cursor.execute("SELECT puntuacion FROM movie")
    res.fetchall()

    data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0),
    ]
    cursor.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
    con.commit()

    for row in cursor.execute("SELECT anio, titulo FROM movie ORDER BY anio"):
        print(row)

    con.close()
    new_con = sqlite3.connect("peliculas.db")
    new_cur = new_con.cursor()
    res = new_cur.execute("SELECT titulo, anio FROM movie ORDER BY puntuacion DESC")
    title, year = res.fetchone()
    print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')
