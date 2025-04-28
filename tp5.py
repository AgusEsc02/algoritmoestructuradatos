def valor_romano(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(romano) == 0:
        return 0
    elif len(romano) == 1:
        return valores[romano]

    if valores[romano[0]] < valores[romano[1]]:
        return valores[romano[1]] - valores[romano[0]] + valor_romano(romano[2:])
    else:
        return valores[romano[0]] + valor_romano(romano[1:])

def romano_a_decimal(romano):
    return valor_romano(romano)

numero_romano = input("Ingrese un número romano: ")
numero_decimal = romano_a_decimal(numero_romano)
print(f"El número romano {numero_romano} es igual a {numero_decimal} en decimal.")