#lista de super heroes
superheroes = [
    "Iron Man", "Thor", "Hulk", "Black Widow", "Hawkeye",
    "Spider-Man", "Doctor Strange", "Black Panther", "Ant-Man",
    "Wasp", "Scarlet Witch", "Vision", "Falcon", "Winter Soldier",
    "Capitan America",
]
def buscar_superheroe(lista, objetivo, index=0):
    if index >= len(lista):
        return False
    if lista[index] == objetivo:
        return True
    return buscar_superheroe(lista, objetivo, index + 1)

def listar_superheroes(lista, index=0):
    if index >= len(lista):
        return
    print(lista[index])
    listar_superheroes(lista, index + 1)

if __name__ == "__main__":
    # Buscar al "Capitan America"
    encontrado = buscar_superheroe(superheroes, "Capitan America")
    print("¿Capitan America está en la lista?", encontrado)

    # Listar todos los superhéroes
    print("\nListado de superhéroes:")
    listar_superheroes(superheroes)