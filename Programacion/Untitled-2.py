nombre=input("Nombre: ")
apellidos=input("Apellidos: ")
edad=input("Edad: ")

todosRellenos=nombre and apellidos and edad
if not todosRellenos:
    print("Tienes que rellenar todos los datos")
else:
    print("Encantado/a %s, al tener %s años puedes subscribirte a la página."%(nombre,edad))
