dic= {
    "Nombre": "Samuel",
    "Apellido": "Plaza",
    "Pais": "España",
    "Ciudad": "Córdoba"
}
dic["Apellido"]= "Plaza Sáez"
dic["Edad"]= 20
print(dic)

dic2={
    "num": 20,
    "str": "Hola mundo",
    "lista": [1,2,3,"adios"],
    "tupla":(1,2,3,4,),
    "dic":{"k1":"valor1", "k2":"valor2"}
}
print(dic2)

dic3={
    "key":"valor 1",
    "key":"valor 2"
}
print(dic3)

dic4={
    "key1":"value1",
    "key2":"value2",
}
dic5={
    "key3":"value3",
    "key4":"value4",
}
print(dic4+dic5)    #No se pueden hacer operaciones con los diccionarios
