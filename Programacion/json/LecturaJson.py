import json

f= open("flw_yz14j.json", "r")

for linea in f:
    # linea=f.readline()
    diccionario= json.loads(linea)
    print("hash --> " + str(diccionario["hash"]) + "\nip --> " + str(diccionario["ip"]) + "\nhostname --> " + str(diccionario["hostnames"]) + "\nasn --> " + str(diccionario["asn"]) + "\nport --> " + str(diccionario["port"]))