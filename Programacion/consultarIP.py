
import ipinfo
token= "3e65ca0ac3fc5a"
handler= ipinfo.getHandler(access_token="3e65ca0ac3fc5a")
ip=input("Introduzca la IP: ")
detalles= handler.getDetails(ip)
print(detalles.all)

# dic= {
#    "hostname":"dns.google",
#    "city":"Mountain View",
#    "region":"California",
#    "country":"US",
#    "loc":"37.4056,-122.0775",
#    "postal":"94043",
#    "timezone":"America/Los_Angeles"
# }

dato= input("Introduce un dato: ")
while dato in detalles.all:
    clave= detalles.all[dato]
    print(clave)
    dato= input("Introduzca otro dato que quiera conocer: ")

else:
    print("Dato no disponible.")
    dato= input("Introduzca otro dato que quiera conocer: ")