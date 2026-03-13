def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100

    monto_impuesto = precio_base*0.21
    subtotal = precio_base + monto_impuesto
    propina = subtotal*0.1
    precio_final = subtotal + propina

    print(monto_impuesto)
    print(subtotal)
    print(propina)
    print(precio_final)
