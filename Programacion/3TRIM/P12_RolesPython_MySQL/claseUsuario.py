class Usuario:
    """Esta clase representa a un usuario de la base de datos."""
    def __init__(self, id, nombre, nombreUsuario, contraseniaHasheada, rol = "usuario"):
        """Inicializa los atributos de la clase.

        Args:
            id (int): Número identificador.
            nombre (str): Nombre real del usuario
            nombreUsuario (str): Nickname del usuario.
            hash_password (str): Contraseña hasheada del usuario.
            rol (bool): determina el rol. Por defecto es un usuario normal.
        """
        self.id = id
        self.nombre = nombre
        self.nombreUsuario = nombreUsuario
        self.contraseniaHasheada = contraseniaHasheada
        self.rol = rol
    
    def set_id(self, id):
        self.id = id
        return self.id
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        return self.nombre
    
    def set_nombreUsuario(self, nombreUsuario):
        self.nombreUsuario = nombreUsuario
        return nombreUsuario
    
    def set_contraseniaHasheada(self, contraseniaHasheada):
        self.contraseniaHasheada = contraseniaHasheada
        return self.contraseniaHasheada
    
    def set_rol(self, rol):
        self.rol = rol
        return self.rol
    
    def get_id(self):
        return self.id
    
    def get_nombre(self):
        return self.nombre
    
    def get_nombreUsuario(self):
        return self.nombreUsuario
    
    def get_contraseniaHasheada(self):
        return self.contraseniaHasheada
    
    def get_rol(self):
        return self.rol