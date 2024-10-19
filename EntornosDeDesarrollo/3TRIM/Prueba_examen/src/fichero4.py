def factura(horas, minutos, segundos, precio):
    """Esta función calcula la duración de la llamada
    y el coste total de la misma

    Args:
        horas (int): horas que dura la llamada
        minutos (int): minutos que dura la llamada
        segundos (int): segundos que dura la llamada
        precio (int): precio de la llamada

    Returns:
        list: duración y coste de la llamada, coste total de todas las 
        llamadas y duración total de las llamadas.
    """
    duracion = (horas * 3600) + (minutos * 60) + segundos
    coste = (duracion * precio)
    coste= round(coste, 2)
    
    return duracion, coste