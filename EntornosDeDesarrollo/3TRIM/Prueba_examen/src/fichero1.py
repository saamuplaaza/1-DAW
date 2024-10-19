def calculoSegundos(horasTotales, minutosTotales, segundosTotales):
    """Esta función hace el cálculo de los segundos y lo imprime por pantalla.

    Args:
        horasTotales (int): total de horas
        minutosTotales (int): total de minutos
        segundosTotales (int): total de segundos

    Returns:
        int: el tiempo en segundos
    """

    h = horasTotales*3600
    m = minutosTotales*60
    hms = h+m+segundosTotales
    return hms