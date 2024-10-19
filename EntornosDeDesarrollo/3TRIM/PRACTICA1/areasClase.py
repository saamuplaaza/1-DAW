from modulos import funcionesMatematicas

class areas:
    """Esta clase calcula las áreas de diferentes figuras geométricas."""
    
    def areaCuadrado(lado):
        """
        Calcula el área de un cuadrado
        elevando al cuadrado el lado pasado por parámetro

        Args:
            lado (int): lado del cuadrado

        Returns:
            str: área del  cuadrado
        """
        return f"El área del cuadrado es: {lado * lado}"

    def areaTriangulo(base, altura):
        """
        Calcula el área de un triángulo utilizando
        los parámetros base y altura

        Args:
            base (int): base del triángulo
            altura (int): altura del triángulo

        Returns:
            str: área del triángulo
        """
        return f"El área del triángulo es: {(base * altura)/2}"
    
help(areas.areaTriangulo) # ayuda de la función areaTriangulo
help(areas) # ayudaa general de la clase
help(funcionesMatematicas) # ayuda del módulo