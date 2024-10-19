agendaDigital= {
    #Primer contacto de la agenda
    "Samuel Plaza Sáez" :{
        "dirección": "Calle diez, 35",
        "email":"samuelplazasaez@gmail.com",
        "teléfono":"644812930"
    },
    #Segundo contacto
    "Alejandro Sanz" :{
        "dirección": "Corazon Partio, 11",
        "email":"alejandrosanz@gmail.com",
        "teléfono":"620172934"
    }
}
def escribirAgenda(nombreAgenda, agendaDigital):
    '''Escribir la agenda en un fichero de texto.

    Parametros posicionales
    nombreAgenda -- str que representa el nombre de la agenda en disco.
    agendaDigital -- dict que representa la agenda digital y los contactos.
    '''
    agendaFichero= open("agendaDigital", "w")
    #Esta sentencia escribe el diccionario en el fichero
    agendaFichero.write(str(agendaDigital))
    #Esta sentencia cierra el fichero que has abierto con la función open()
    agendaFichero.close()

def leerAgenda(nombreAgenda):
    '''Leer agenda digital de un fichero 
    
    Parametros posicionales
    nombreAgenda -- str que representa el nombre de la agenda en disco.
    '''
    agendaDigitalLectura= open("agendaDigital", "r")
    agendaDigital= agendaDigitalLectura.readlines()
    #Esta sentencia cierra el fichero que has abierto con la función open()
    agendaDigitalLectura.close()
    return eval(agendaDigital[0])

def solicitarContactoAgenda():
    '''Esta función solicita los datos de un nuevo contacto al usuario.'''
    nombre= input("Introduce el nombre completo del contacto: ")
    direccion= input("Introduce la dirección del contacto: ")
    email= input("Introduce el email del contacto: ")
    telefono= input("Introduce el teléfono del contacto: ")
    #Construimos un diccionario con los valores recibidos
    contacto= {
        "nombre": nombre,
        "direccion": direccion,
        "email": email,
        "telefono": telefono
    }
    return contacto

def crearContacto(agendaDigital, nuevoContacto):
    '''Introduce un nuevo contacto en la agenda existente.
    
    Parametros posicionales
    agendaDigital -- dict que representa la agenda existente.
    nuevoContacto -- dict que representa el nuevo contacto.
    '''
    agendaDigital[nuevoContacto["nombre"]]= {
        "direccion": nuevoContacto["direccion"],
        "email": nuevoContacto["email"],
        "telefono": nuevoContacto["telefono"]
    }
    return agendaDigital

def consultarContactoAgenda(agendaDigital):
    '''Esta función consulta un contacto en la agenda.'''
    nombre= input("Introduce el nombre completo del contacto: ")
    print("\n[+]", nombre)
    print("\tDireccion:", agendaDigital[nombre]["direccion"])
    print("\tEmail:", agendaDigital[nombre]["email"])
    print("\tTeléfono:", agendaDigital[nombre]["telefono"])


agendaDigital= leerAgenda("agendaDigital")
nuevoContacto= solicitarContactoAgenda()
crearContacto(agendaDigital, nuevoContacto)
escribirAgenda("agendaDigital", agendaDigital)

agendaDigital= leerAgenda("agendaDigital")
consultarContactoAgenda(agendaDigital)