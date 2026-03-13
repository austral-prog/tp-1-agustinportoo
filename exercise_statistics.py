def statistics():
    """
    Ejercicio 5 - Estadísticas Simples

    Dados cuatro números, calcular e imprimir:
    1. El promedio
    2. El máximo
    3. El mínimo
    4. El rango (diferencia entre máximo y mínimo)
    """
    num1 = 15
    num2 = 8
    num3 = 23
    num4 = 12

    suma = num1 + num2 + num3 + num4
    promedio = suma / 4
    maximo = max(num1, num2, num3, num4)
    minimo = min(num1, num2, num3, num4)
    rango = maximo - minimo

    print(promedio)
    print(maximo)
    print(minimo)
    print(rango)
