print(dir(str))
texto = "             HoLa MunDo    .    "
print(texto.capitalize())
print(texto.lower())
print(texto.upper())
print(texto.title())
print(texto.swapcase())
print("COLOR" == "color") # Key Sensitive
texto2 = "Hola Me gusta la lasaña."
print(texto2.count("la"))
print(texto2.find("la"))
print(texto2.rfind("la"))

# Clasificacion de caracteres
texto3 = "123abc"
texto4 = "123$abc"
texto5 = "123"
bin_texto = "1010"
print(texto3.isalnum())
print(texto4.isalnum())
print(texto5.isdigit())

# Formateo de una cadena de texto por pantalla
print(texto.center(30))
print(texto.ljust(200))
print(texto.rjust(40))
print(texto.lstrip())
print(texto.rstrip())
print(texto.strip())
print(texto.replace(" ", "-"))
print(bin_texto.zfill(8))
print(", ".join(["rojo","azul","verde"]))
print("{}-{}-{}".format("dia", "mes", 2024))
