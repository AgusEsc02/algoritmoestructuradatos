from collections import deque

cola = deque([
    {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"personaje": "Sam Wilson", "superheroe": "Falcon", "genero": "M"},
    {"personaje": "Shuri", "superheroe": "Shuri", "genero": "F"},
])


for p in cola:
    if p["superheroe"] == "Capitana Marvel":
        print(f"a. Personaje de Capitana Marvel: {p['personaje']}")


print("b. Superhéroes femeninos:")
for p in cola:
    if p["genero"] == "F":
        print(f"  {p['superheroe']}")


print("c. Personajes masculinos:")
for p in cola:
    if p["genero"] == "M":
        print(f"  {p['personaje']}")


for p in cola:
    if p["personaje"] == "Scott Lang":
        print(f"d. Superhéroe de Scott Lang: {p['superheroe']}")


print("e. Datos con nombres que comienzan con 'S':")
for p in cola:
    if p["personaje"].startswith("S") or p["superheroe"].startswith("S"):
        print(f"  {p}")


encontrado = False
for p in cola:
    if p["personaje"] == "Carol Danvers":
        print(f"f. Carol Danvers está en la cola, su superhéroe es: {p['superheroe']}")
        encontrado = True
if not encontrado:
    print("f. Carol Danvers no está en la cola.")