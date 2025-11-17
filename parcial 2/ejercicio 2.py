import heapq


class Grafo:
    def __init__(self):
        # grafo no dirigido: {personaje: [(otro_personaje, peso), ...]}
        self.adyacencia = {}
        # para saber en qué episodios aparece cada personaje
        self.episodios_por_personaje = {}

    def agregar_personaje(self, nombre, episodios=None):
        if nombre not in self.adyacencia:
            self.adyacencia[nombre] = []
        if episodios is not None:
            self.episodios_por_personaje[nombre] = set(episodios)

    def agregar_arista(self, p1, p2, episodios_en_comun):
        """Agrega una arista no dirigida entre p1 y p2 con peso = episodios en común."""
        if p1 not in self.adyacencia:
            self.adyacencia[p1] = []
        if p2 not in self.adyacencia:
            self.adyacencia[p2] = []
        self.adyacencia[p1].append((p2, episodios_en_comun))
        self.adyacencia[p2].append((p1, episodios_en_comun))

    # 1) Árbol de expansión mínimo (algoritmo de Prim)
    def arbol_expansion_minimo(self, origen):
        if origen not in self.adyacencia:
            return [], 0

        visitado = set([origen])
        heap = []

        # agregamos al heap todas las aristas que salen del origen
        for vecino, peso in self.adyacencia[origen]:
            heapq.heappush(heap, (peso, origen, vecino))

        aristas_mst = []
        peso_total = 0

        while heap and len(visitado) < len(self.adyacencia):
            peso, u, v = heapq.heappop(heap)
            if v in visitado:
                continue
            visitado.add(v)
            aristas_mst.append((u, v, peso))
            peso_total += peso

            # agregamos aristas que salen del nuevo vértice v
            for w, pw in self.adyacencia[v]:
                if w not in visitado:
                    heapq.heappush(heap, (pw, v, w))

        return aristas_mst, peso_total

    # 2) Máximo número de episodios que comparten dos personajes
    def max_episodios_en_comun(self):
        max_peso = 0
        pares = set()  # para no repetir (u, v) y (v, u)

        for u in self.adyacencia:
            for v, peso in self.adyacencia[u]:
                # solo consideramos un orden (u < v) para evitar duplicados
                if u < v:
                    if peso > max_peso:
                        max_peso = peso
                        pares = {(u, v)}
                    elif peso == max_peso:
                        pares.add((u, v))
        return max_peso, list(pares)

    # 3) Camino más corto entre dos personajes 
    def camino_mas_corto(self, origen, destino):
        if origen not in self.adyacencia or destino not in self.adyacencia:
            return float("inf"), []

        dist = {v: float("inf") for v in self.adyacencia}
        padre = {v: None for v in self.adyacencia}
        dist[origen] = 0

        heap = [(0, origen)]

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            if u == destino:
                break  # ya llegamos

            for v, peso in self.adyacencia[u]:
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    padre[v] = u
                    heapq.heappush(heap, (dist[v], v))

        if dist[destino] == float("inf"):
            return float("inf"), []

        # reconstruir camino desde destino hacia origen
        camino = []
        actual = destino
        while actual is not None:
            camino.append(actual)
            actual = padre[actual]
        camino.reverse()
        return dist[destino], camino

    # 4) Personajes que aparecieron en los 9 episodios
    def personajes_en_nueve_episodios(self):
        resultado = []
        for personaje, episodios in self.episodios_por_personaje.items():
            # suponemos que los episodios son del 1 al 9
            if episodios == set(range(1, 10)):
                resultado.append(personaje)
        return resultado


def main():
    grafo = Grafo()

    # Cargar personajes pedidos 
    personajes = [
        "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia",
        "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"
    ]

    # EJEMPLO: acá invento en qué episodios aparece cada uno.
    for p in personajes:
        if p in ["C-3PO", "R2-D2"]:  # por ejemplo, decimos que estos están en los 9
            grafo.agregar_personaje(p, episodios=range(1, 10))
        else:
            # ejemplo: están solo en algunos episodios 
            grafo.agregar_personaje(p, episodios=[4, 5, 6])

    # Agregar aristas 
    # Estos pesos son de ejemplo; adáptalos si tienes datos concretos.
    grafo.agregar_arista("Luke Skywalker", "Darth Vader", 3)
    grafo.agregar_arista("Luke Skywalker", "Leia", 4)
    grafo.agregar_arista("Luke Skywalker", "Han Solo", 3)
    grafo.agregar_arista("Leia", "Han Solo", 4)
    grafo.agregar_arista("Han Solo", "Chewbacca", 5)
    grafo.agregar_arista("C-3PO", "R2-D2", 6)
    grafo.agregar_arista("C-3PO", "Luke Skywalker", 4)
    grafo.agregar_arista("R2-D2", "Luke Skywalker", 4)
    grafo.agregar_arista("Yoda", "Luke Skywalker", 2)
    grafo.agregar_arista("Yoda", "Darth Vader", 1)
    grafo.agregar_arista("Rey", "BB-8", 2)
    grafo.agregar_arista("Rey", "Kylo Ren", 2)
    grafo.agregar_arista("Kylo Ren", "Leia", 1)
    grafo.agregar_arista("Boba Fett", "Darth Vader", 1)

    # a) Árbol de expansión mínimo desde C-3PO, Yoda y Leia
    for origen in ["C-3PO", "Yoda", "Leia"]:
        mst, peso_total = grafo.arbol_expansion_minimo(origen)
        print(f"\nÁrbol de expansión mínimo desde {origen}:")
        for u, v, w in mst:
            print(f"  {u} - {v} (episodios en común: {w})")
        print(f"Peso total del árbol: {peso_total}")

    # b) Máximo número de episodios que comparten dos personajes
    max_peso, pares = grafo.max_episodios_en_comun()
    print(f"\nMáximo número de episodios compartidos por una pareja: {max_peso}")
    print("Pares de personajes que comparten esa cantidad:")
    for u, v in pares:
        print(f"  {u} - {v}")

    # c) Camino más corto desde C-3PO a R2-D2 y desde Yoda a Darth Vader
    dist1, camino1 = grafo.camino_mas_corto("C-3PO", "R2-D2")
    print(f"\nCamino más corto C-3PO -> R2-D2 (suma de pesos = {dist1}): {camino1}")

    dist2, camino2 = grafo.camino_mas_corto("Yoda", "Darth Vader")
    print(f"Camino más corto Yoda -> Darth Vader (suma de pesos = {dist2}): {camino2}")

    # d) Personajes que aparecieron en los nueve episodios de la saga
    en_nueve = grafo.personajes_en_nueve_episodios()
    print("\nPersonajes que aparecieron en los 9 episodios de la saga:")
    if not en_nueve:
        print("  Ninguno con los datos cargados.")
    else:
        for p in en_nueve:
            print(" ", p)


if __name__ == "__main__":
    main()
    