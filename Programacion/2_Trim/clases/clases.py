class Coche:
    """Esta clase representa un coche. Tiene los atributos marca, modelo y color."""
    
    def __init__(self, marca, modelo, cv, combustible):
        """Inicializa los atributos de instancia.

        Args:
            marca: string que representa la marca del coche.
            modelo: string que representa el modelo del coche.
            cv: string que representa los cv del coche.
        """
        self.marca = marca
        self.modelo = modelo
        self.cv = cv
        self.combustible = combustible
        
        
    def set_marca(self, marcaNueva):
        """Este método establece la marca del coche."""
        self.marca = marcaNueva
        return self.marca
    
    def get_marca(self):
        """Este método devuelve la marca del coche."""
        return self.marca
    
    def set_modelo(self, modeloNuevo):
        """Este método establece el modelo del coche."""
        self.modelo = modeloNuevo
        return self.modelo
        
    def get_modelo(self):
        """Este método devuelve el modelo del coche."""
        return self.modelo
    
    def set_cv(self, cvNuevo):
        """Este método establece los cv del coche."""
        self.cv = cvNuevo
        return self.cv
    
    def get_cv(self):
        """Este método devuelve los cv del coche."""
        return self.cv


class Mascota:
    """Esta clase representa una mascota. Tiene como atributo nombre, tipo y color."""
    def __init__(self, nombreMascota, tipoMascota, colorMascota):
        self.nombre = nombreMascota
        self.tipo = tipoMascota
        self.color =colorMascota
    
    def set_nombre(self, nombreNuevo):
        """Este método establece el nombre de la mascota."""
        self.nombre = nombreNuevo
        return self.nombre
    
    def get_nombre(self):
        """Este método devuelve el nombre de la mascota."""
        return self.nombre
    
    def set_tipo(self, tipoNuevo):
        """Este método establece el tipo de la mascota."""
        self.tipo = tipoNuevo
        return self.tipo
    
    def get_tipo(self):
        """Este método devuelve el tipo de la mascota."""
        return self.tipo
    
    def set_color(self, colorNuevo):
        """Este método establece el color de la mascota."""
        self.color = colorNuevo
        return self.color
    
    def get_color(self):
        """Este método devuelve el color de la mascota."""
        return self.color


# miCoche = Coche("Toyota", "Yaris", 40)
# miCoche2 = Coche("bmw", "serie 1", 89)

# Coche 1
# print(miCoche.set_marca(""))
# print(miCoche.set_modelo(""))
# print(miCoche.set_cv(""))

# print(miCoche.get_marca())
# print(miCoche.get_modelo())
# print(miCoche.get_cv())

# Coche 2
# print(miCoche2.set_marca(""))
# print(miCoche2.set_modelo(""))
# print(miCoche2.set_cv(""))

# print(miCoche2.get_marca())
# print(miCoche2.get_modelo())
# print(miCoche2.get_cv())


def mi_funcion():
    print("hola mundo")
    
    
def mi_decorator(func):
    def wrapper():
        print("Antes de la ejecucion")
        func()
        print("Despues de la ejecucion")
    return wrapper

funcion = mi_decorator(mi_funcion)
print(funcion)

class CocheElectrico(Coche):
    """Esta clase representa a los coches electricos"""
    
    def __init__(self, marca, modelo, cv, combustible, capacidadBateria):
        """Inicializa losatributos del padre"""
        super().__init__(marca, modelo, cv, combustible)
        self.combustible = "KWh/100km"
        self._capacidadBateria= capacidadBateria
        
    def detallesBateria(self):
        print(f"El tamaño de la bateria es {self._capacidadBateria}")
        
        
class Bateria:
    
    def __init__(self, capacidad, tipoPila, numPilas, peso):
        self._capacidad = capacidad
        self._tipoPila = tipoPila
        self._numPilas = numPilas
        self._peso = peso



miCoche = CocheElectrico("tesla", "model 3", 150, 200, 30)
