# texto1 = "123abc"
# texto2 = "123$abc"
# texto3 = "123"

# texto1.isalnum()
# texto2.isalnum()
# texto3.isdigit()


# texto1 = "Hola mundo"
# print(texto1.center(40))
# print(texto1.ljust(40))

# texto2 = "\t\n       Hola            que      tal    .   "
# print(texto2.lstrip())
# print(texto2.rstrip())
# print(texto2.replace(" ", "-"))



# texto = "Hola"
# print(texto.zfill(8))

# bin_texto = "1011"
# print(bin_texto.zfill(8))

# print(", ".join(["azul", "verde", "rojo"]))

# print("{}-{}-{}".format(3, "hola", [2, 3]))



# lista = ["azul", "verde", "rojo"]
# lista.append("amarillo")
# print(lista)

# lista.extend(["morado", "negro", "blanco"])
# print(lista)

# lista.remove("azul")
# print(lista)

# lista.reverse()
# print(lista)

# lista.pop()
# print(lista)

# lista2 = lista.copy()
# lista[0] = "marrón"
# print(lista)
# print(lista2)

# print(lista.index("morado"))



dic = {
    "key1" : 1,
    "key2" : 2,
    "key3" : 3
}

# dic.update({"key4":10})
# print(dic)

# print(dic.pop("key1"))
# print(dic)

# dic2 = dic.copy()
# print(dic2)

# dic.clear()
# print(dic)

print(list(dic.values()))
print(list(dic.keys()))
print(dic.items())

for key, value in dic.items():
    print(f"{key} -> {value}")