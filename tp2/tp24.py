class PersonajeMCU:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas

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


def resolver_actividades(pila_personajes):
   
    posicion_rocket = -1
    posicion_groot = -1
    pila_aux = Pila()
    posicion_actual = 1

    while not pila_personajes.esta_vacia():
        personaje = pila_personajes.desapilar()
        pila_aux.apilar(personaje)

        if personaje.nombre == "Rocket Raccoon":
            posicion_rocket = posicion_actual
        if personaje.nombre == "Groot":
            posicion_groot = posicion_actual

        posicion_actual += 1

    
    while not pila_aux.esta_vacia():
        pila_personajes.apilar(pila_aux.desapilar())

   
    personajes_mas_de_5 = []

    while not pila_personajes.esta_vacia():
        personaje = pila_personajes.desapilar()
        pila_aux.apilar(personaje)

        if personaje.peliculas > 5:
            personajes_mas_de_5.append((personaje.nombre, personaje.peliculas))

  
    while not pila_aux.esta_vacia():
        pila_personajes.apilar(pila_aux.desapilar())

   
    peliculas_black_widow = 0

    while not pila_personajes.esta_vacia():
        personaje = pila_personajes.desapilar()
        pila_aux.apilar(personaje)

        if personaje.nombre == "Black Widow":
            peliculas_black_widow = personaje.peliculas

   
    while not pila_aux.esta_vacia():
        pila_personajes.apilar(pila_aux.desapilar())

  
    personajes_cdg = []

    while not pila_personajes.esta_vacia():
        personaje = pila_personajes.desapilar()
        pila_aux.apilar(personaje)

        if personaje.nombre[0] in "CDG":
            personajes_cdg.append(personaje.nombre)

 
    while not pila_aux.esta_vacia():
        pila_personajes.apilar(pila_aux.desapilar())

   
    return {
        "posicion_rocket": posicion_rocket,
        "posicion_groot": posicion_groot,
        "personajes_mas_de_5": personajes_mas_de_5,
        "peliculas_black_widow": peliculas_black_widow,
        "personajes_cdg": personajes_cdg,
    }


pila_personajes = Pila()
pila_personajes.apilar(PersonajeMCU("Iron Man", 10))
pila_personajes.apilar(PersonajeMCU("Rocket Raccoon", 6))
pila_personajes.apilar(PersonajeMCU("Thor", 9))
pila_personajes.apilar(PersonajeMCU("Hulk", 8))
pila_personajes.apilar(PersonajeMCU("Hawkeye",6))
pila_personajes.apilar(PersonajeMCU("Nick Fury",10 ))
pila_personajes.apilar(PersonajeMCU("War Machine", 8))
pila_personajes.apilar(PersonajeMCU("Groot", 5))
pila_personajes.apilar(PersonajeMCU("Black Widow", 8))
pila_personajes.apilar(PersonajeMCU("Captain America", 9))
pila_personajes.apilar(PersonajeMCU("Doctor Strange", 4))

resultados = resolver_actividades(pila_personajes)
print("Posición de Rocket Raccoon:", resultados["posicion_rocket"])
print("Posición de Groot:", resultados["posicion_groot"])
print("Personajes en más de 5 películas:", resultados["personajes_mas_de_5"])
print("Películas de Black Widow:", resultados["peliculas_black_widow"])
print("Personajes cuyos nombres empiezan con C, D y G:", resultados["personajes_cdg"])