class TrajeIronMan:
    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado

    def __str__(self):
        return f"Modelo: {self.modelo}, Película: {self.pelicula}, Estado: {self.estado}"


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop() if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.items) == 0

    def cima(self):
        return self.items[-1] if not self.esta_vacia() else None

    def tamanio(self):
        return len(self.items)

pila_trajes = Pila()
pila_trajes.apilar(TrajeIronMan("Mark XLIV (Hulkbuster)", "Avengers: Age of Ultron", "Dañado"))
pila_trajes.apilar(TrajeIronMan("Mark XLII", "Iron Man 3", "Destruido"))
pila_trajes.apilar(TrajeIronMan("Mark XLVII", "Spider-Man: Homecoming", "Impecable"))
pila_trajes.apilar(TrajeIronMan("Mark XLVI", "Capitan America: Civil War", "Dañado"))

peliculas_hulkbuster = []
aux_pila = Pila()
while not pila_trajes.esta_vacia():
    traje = pila_trajes.desapilar()
    if traje.modelo == "Mark XLIV (Hulkbuster)":
        peliculas_hulkbuster.append(traje.pelicula)
    aux_pila.apilar(traje)

while not aux_pila.esta_vacia():
    pila_trajes.apilar(aux_pila.desapilar())

if peliculas_hulkbuster:
    print("El modelo Mark XLIV (Hulkbuster) fue utilizado en las siguientes películas:")
    for pelicula in peliculas_hulkbuster:
        print(f"- {pelicula}")
else:
    print("El modelo Mark XLIV (Hulkbuster) no fue utilizado en ninguna película.")

print("\nModelos que quedaron dañados:")
aux_pila = Pila()
while not pila_trajes.esta_vacia():
    traje = pila_trajes.desapilar()
    if traje.estado == "Dañado":
        print(traje)
    aux_pila.apilar(traje)


while not aux_pila.esta_vacia():
    pila_trajes.apilar(aux_pila.desapilar())


print("\nEliminando modelos destruidos:")
aux_pila = Pila()
while not pila_trajes.esta_vacia():
    traje = pila_trajes.desapilar()
    if traje.estado == "Destruido":
        print(f"Eliminado: {traje.modelo}")
    else:
        aux_pila.apilar(traje)


while not aux_pila.esta_vacia():
    pila_trajes.apilar(aux_pila.desapilar())


nuevo_traje = TrajeIronMan("Mark LXXXV", "Avengers: Endgame", "Impecable")
existe = False
aux_pila = Pila()
while not pila_trajes.esta_vacia():
    traje = pila_trajes.desapilar()
    if traje.modelo == nuevo_traje.modelo and traje.pelicula == nuevo_traje.pelicula:
        existe = True
    aux_pila.apilar(traje)


while not aux_pila.esta_vacia():
    pila_trajes.apilar(aux_pila.desapilar())

if not existe:
    pila_trajes.apilar(nuevo_traje)
    print("\nEl modelo Mark LXXXV fue agregado a la pila.")
else:
    print("\nEl modelo Mark LXXXV ya existe en la pila para esa película.")


peliculas_especificas = ["Spider-Man: Homecoming", "Capitan America: Civil War"]
print("\nTrajes utilizados en las películas específicas:")
aux_pila = Pila()
while not pila_trajes.esta_vacia():
    traje = pila_trajes.desapilar()
    if traje.pelicula in peliculas_especificas:
        print(traje.modelo)
    aux_pila.apilar(traje)


while not aux_pila.esta_vacia():
    pila_trajes.apilar(aux_pila.desapilar())