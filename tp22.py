def usar_la_fuerza(mochila, indice=0):
    if indice >= len(mochila):
        return False, 0

    if mochila[indice] == "sable de luz":
        return True, 1

    encontrado, objetos_necesarios = usar_la_fuerza(mochila, indice + 1)

    if encontrado:
        return True, objetos_necesarios + 1
    else:
        return False, objetos_necesarios + 1

#Ejemplo de uso:
mochila = ["botella de agua", "comida en lata", "libro", "sable de luz", "manta"]
encontrado, objetos_necesarios = usar_la_fuerza(mochila)

if encontrado:
    print("El Jedi encontró un sable de luz en la mochila.")
    print(f"Se necesitaron sacar {objetos_necesarios} objetos para encontrarlo.")
else:
    print("El Jedi no encontró un sable de luz en la mochila.")
    print(f"Se sacaron todos los {objetos_necesarios} objetos de la mochila.")