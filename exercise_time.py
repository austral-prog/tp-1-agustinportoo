def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665

    minutos = total_segundos / 60
    minutos_enteros = total_segundos // 60
    horas = minutos / 60
    horas_completas = total_segundos // 3600
    minutos_disponibles = total_segundos - 3600
    minutos_completos_restantes = minutos_disponibles // 60
    segundos_restantes =  minutos_disponibles - (minutos_completos_restantes * 60)


    print(horas_completas)
    print(minutos_completos_restantes)
    print(segundos_restantes)
