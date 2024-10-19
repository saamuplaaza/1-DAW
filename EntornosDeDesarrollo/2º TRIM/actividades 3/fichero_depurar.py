with open("1.txt", "w") as archivo_original:
    archivo_original.write("I, I will be king\n")
    archivo_original.write("And you, you will be queen\n")
    archivo_original.write("Though nothing, will drive them away\n")
    archivo_original.write("We can beat them, just for one day\n")
    archivo_original.write("We can be heroes, just for one day\n")



titulo_cancion = input("Título de la canción: ")
nombre_compositor = input("Nombre del compositor: ")


with open("1.txt", "r") as archivo_original:
    contenido_original = archivo_original.read()


nombre_nuevo_archivo = f"{titulo_cancion}.txt"


with open(nombre_nuevo_archivo, "w") as nuevo_archivo:
    nuevo_archivo.write(f"Título de la canción: {titulo_cancion}\n")
    nuevo_archivo.write(f"Nombre del autor: {nombre_compositor}\n")
    nuevo_archivo.write(contenido_original)

print(f"Se ha creado el archivo {nombre_nuevo_archivo} con éxito.")


with open("1.txt", "r") as archivo:
    contenido = archivo.read()


print("Caracteres entre la posición 10 y 17 en una línea:")
print(contenido[9:17])


print("\nCaracteres entre la posición 10 y 17 en columna y mayúsculas:")
for caracter in contenido[9:17].lower():
    print(caracter)