import sqlite3
import csv

def leerFichero():
    with open('Linkedin2023.csv', newline='', encoding="utf-8") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=',')
        numeroID=0
        numeros = "0123456789"
        # Saltar la primera fila si contiene encabezados
        next(lector_csv, None)
        for fila in lector_csv:
            separado = fila[3].split("-")
            resto = separado[:-1]
            userNameSeparado =""
            for caracter in separado[-1]:
                if caracter in numeros:
                    IDseparado = separado[-1]
                    userNameSeparado =""
                    for valor in resto:
                       userNameSeparado += valor
                    break
            else:
                IDseparado = ""
                for valor in separado:
                    userNameSeparado = valor
            direccionSeparada = fila[59].split(",")
            pais = direccionSeparada[-1]
            direccion = ""
            for valores in direccionSeparada[:-1]:
                direccion += valores +","
            direccion=direccion.strip(",")
            numeroID+=1
            datos = [numeroID, fila[0], userNameSeparado, IDseparado, fila[30].strip("[]"), fila[31].strip("[]"), fila[32].strip("[]"),fila[33],fila[34],fila[36],fila[37],fila[38],fila[39],fila[40],fila[41],fila[42],fila[48], direccion, pais] # fila[59][:-1], fila[59][-1]]
            cursor.execute('''INSERT INTO usuarios_Linkedin2023
                            (id, hashclave, nombreUsuario, userid, correo, correo2, telefono, nombre, apellidos, jerarquia, cargo, sexo, codigoPais, descripcion, sector, fechaNacimiento, empresa, direccion, pais)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', datos)
        con.commit()
        


# Main
# os.system("more Linkedin2023.csv")

con = sqlite3.connect("Linkedin2023.db")
cursor = con.cursor()
try:
    error = cursor.execute("CREATE TABLE usuarios_Linkedin2023(id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, hashclave, nombreUsuario, userid, correo, correo2, telefono, nombre, apellidos, jerarquia, cargo, sexo, codigoPais, descripcion, sector, fechaNacimiento, empresa, direccion, pais)")
    print("Tabla creada con éxito")
except sqlite3.OperationalError:
    print("Ya existe una tabla con este nombre.")
    pass

archivo = leerFichero()

con.close()