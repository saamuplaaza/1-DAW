
correo=input("Introduce el correo: ")
i=0
for caracter in correo:
    if caracter=="@":
        break
    i+=1
usuario=correo[:i]
correofinal=usuario+"@ceu.es"
print("El antiguo correo era %s." %(correo))
print("El nuevo correo es %s." %(correofinal))


