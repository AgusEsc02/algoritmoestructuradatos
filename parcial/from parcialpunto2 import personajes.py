from parcialpunto2 import personajes
from queue import Queue

#Listado ordenado de manera ascendente por nombre de los personajes
personajes_ordenados_nombre = sorted(personajes, key=lambda x: x["name"])
print("Listado ordenado por nombre:")
for p in personajes_ordenados_nombre:
    print(p["name"])
print()

#Determinar en que posicion esta The Thing y Rocket Raccoon.
nombres = [p["name"] for p in personajes_ordenados_nombre]
pos_thing = nombres.index("The Thing") if "The Thing" in nombres else -1
pos_rocket = nombres.index("Rocket Raccoon") if "Rocket Raccoon" in nombres else -1
print(f"Posición de The Thing: {pos_thing}")
print(f"Posición de Rocket Raccoon: {pos_rocket}")
print()

#Listar todos los villanos de la lista.
villanos = [p for p in personajes if p["is_villain"]]
print("Villanos:")
for v in villanos:
    print(v["name"])
print()

#Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
cola_villanos = deque(villanos)
villanos_antes_1980 = [v for v in cola_villanos if v["first_appearance"] < 1980]
print("Villanos que aparecieron antes de 1980:")
for v in villanos_antes_1980:
    print(f"{v['name']} ({v['first_appearance']})")
print()

#Listar los superheores que comienzan con  Bl, G, My, y W.
patron = re.compile(r"^(Bl|G|My|W)", re.IGNORECASE)
superheroes = [p for p in personajes if not p["is_villain"] and patron.match(p["name"])]
print("Superhéroes que comienzan con Bl, G, My, W:")
for s in superheroes:
    print(s["name"])
print()

#Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
personajes_ordenados_real = sorted(personajes, key=lambda x: (x["real_name"] or ""))
print("Listado ordenado por nombre real:")
for p in personajes_ordenados_real:
    print(f"{p['name']} ({p['real_name']})")
print()

#Listado de superheroes ordenados por fecha de aparación.
superheroes_ordenados_fecha = sorted([p for p in personajes if not p["is_villain"]], key=lambda x: x["first_appearance"])
print("Superhéroes ordenados por fecha de aparición:")
for s in superheroes_ordenados_fecha:
    print(f"{s['name']} ({s['first_appearance']})")
print()

# Modificar el nombre real de Ant Man a Scott Lang.
for p in personajes:
    if p["name"] == "Ant Man":
        p["real_name"] = "Scott Lang"
        print("Nombre real de Ant Man modificado a Scott Lang.")
print()

# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
print("Personajes cuya biografía incluye 'time-traveling' o 'suit':")
for p in personajes:
    bio = p["short_bio"].lower()
    if "time-traveling" in bio or "suit" in bio:
        print(f"{p['name']}: {p['short_bio']}")
print()

#Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
eliminados = []
for nombre in ["Electro", "Baron Zemo"]:
    for i, p in enumerate(personajes):
        if p["name"] == nombre:
            eliminados.append(personajes.pop(i))
            break
print("Personajes eliminados:")
for e in eliminados:
    print(e)