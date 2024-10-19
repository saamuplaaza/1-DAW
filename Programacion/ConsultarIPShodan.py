from shodan import Shodan
api= Shodan('PreZHlnOHyXX6qpQRbwGmyJFYLuq0QE5')
ip= input("Introduzca una ip: ")
ipinfo= api.host(ip)
print(ipinfo)

dato= input("Introduce un dato: ")
while dato in ipinfo:
    clave= ipinfo[dato]
    print(clave)
    dato= input("Introduzca otro dato que quiera conocer: ")
else:
    print("Dato no disponible.")
