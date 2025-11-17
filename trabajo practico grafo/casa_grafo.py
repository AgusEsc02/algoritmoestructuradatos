import heapq


class Graph:
    def __init__(self):
        # adj[vertice] = { vecino: peso, ... }
        self.adj = {}

    def add_node(self, name):
        self.adj.setdefault(name, {})

    def add_edge(self, u, v, w):
        """Agrega una arista no dirigida con peso w (en metros)."""
        self.adj.setdefault(u, {})
        self.adj.setdefault(v, {})
        self.adj[u][v] = w
        self.adj[v][u] = w

    # ---------- caminos mínimos (Dijkstra) ----------

    def dijkstra(self, source):
        """Devuelve distancias y predecesores desde 'source'."""
        dist = {node: float("inf") for node in self.adj}
        prev = {node: None for node in self.adj}
        dist[source] = 0
        heap = [(0, source)]

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in self.adj[u].items():
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(heap, (nd, v))

        return dist, prev

    @staticmethod
    def build_path(prev, target):
        if prev[target] is None:
            return [target]
        path = []
        u = target
        while u is not None:
            path.append(u)
            u = prev[u]
        path.reverse()
        return path

    # ---------- Árbol de expansión mínima (Kruskal) ----------

    def minimum_spanning_tree(self):
        """Devuelve lista de aristas (u, v, w) del árbol de expansión mínima y su peso total."""
        # construir lista de aristas sin duplicados
        edges = []
        seen = set()
        for u in self.adj:
            for v, w in self.adj[u].items():
                if (v, u) not in seen:
                    edges.append((w, u, v))
                    seen.add((u, v))

        # ordenar por peso
        edges.sort()

        # estructura Union-Find
        parent = {}
        rank = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
            return True

        for node in self.adj:
            parent[node] = node
            rank[node] = 0

        mst = []
        total = 0
        for w, u, v in edges:
            if union(u, v):
                mst.append((u, v, w))
                total += w

        return mst, total


# ------------- Carga del grafo de la casa -------------

AMBIENTES = [
    "Cocina",
    "Comedor",
    "Cochera",
    "Quincho",
    "Baño 1",
    "Baño 2",
    "Habitación 1",
    "Habitación 2",
    "Sala de estar",
    "Terraza",
    "Patio",
]


def build_house_graph():
    g = Graph()

    # a) crear los vértices
    for amb in AMBIENTES:
        g.add_node(amb)

    # b) cargar aristas (distancias en metros)
    # Sala de estar como ambiente central
    g.add_edge("Sala de estar", "Comedor", 4)
    g.add_edge("Sala de estar", "Cocina", 6)
    g.add_edge("Sala de estar", "Habitación 1", 5)
    g.add_edge("Sala de estar", "Terraza", 3)
    g.add_edge("Sala de estar", "Patio", 7)
    g.add_edge("Sala de estar", "Cochera", 9)

    # zona cocina / comedor / terraza / patio
    g.add_edge("Comedor", "Cocina", 3)
    g.add_edge("Comedor", "Terraza", 5)
    g.add_edge("Cocina", "Patio", 4)

    # zona habitaciones y baños
    g.add_edge("Habitación 1", "Baño 1", 2)
    g.add_edge("Habitación 1", "Habitación 2", 3)
    g.add_edge("Habitación 2", "Baño 2", 2)
    g.add_edge("Habitación 2", "Patio", 5)
    g.add_edge("Baño 1", "Baño 2", 4)
    g.add_edge("Baño 1", "Terraza", 6)

    # zona exterior: patio, cochera, quincho
    g.add_edge("Patio", "Terraza", 4)
    g.add_edge("Patio", "Cochera", 6)
    g.add_edge("Patio", "Quincho", 5)
    g.add_edge("Cochera", "Quincho", 7)
    g.add_edge("Baño 2", "Quincho", 8)

    # Con estas conexiones, todos los ambientes tienen al menos 3 aristas
    # y dos ambientes (Sala de estar y Patio) tienen 5 o más.

    return g


def main():
    g = build_house_graph()

    # c) Árbol de expansión mínima
    mst, total = g.minimum_spanning_tree()
    print("Árbol de expansión mínima:")
    for u, v, w in mst:
        print(f"  {u} -- {v} : {w} m")
    print(f"Total de metros de cable necesarios para conectar todos los ambientes: {total} m\n")

    # d) Camino más corto desde Habitación 1 hasta Sala de estar
    origen = "Habitación 1"
    destino = "Sala de estar"
    dist, prev = g.dijkstra(origen)
    camino = Graph.build_path(prev, destino)
    print(f"Camino más corto desde '{origen}' hasta '{destino}':")
    print("  " + " -> ".join(camino))
    print(f"Distancia total: {dist[destino]} m")


if __name__ == "__main__":
    main()
