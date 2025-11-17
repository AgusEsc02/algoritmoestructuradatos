from collections import deque
import heapq

class Graph:
    def __init__(self):
        # adj[nodo] = { vecino: peso, ... }
        self.adj = {}
        # types[nodo] = "pc" / "notebook" / "servidor" / "router" / "switch" / "impresora"
        self.types = {}

    def add_node(self, name, node_type):
        self.types[name] = node_type
        self.adj.setdefault(name, {})

    def add_edge(self, u, v, w):
        self.adj.setdefault(u, {})
        self.adj.setdefault(v, {})
        self.adj[u][v] = w
        self.adj[v][u] = w   # grafo no dirigido

    def remove_edge(self, u, v):
        if u in self.adj and v in self.adj[u]:
            del self.adj[u][v]
        if v in self.adj and u in self.adj[v]:
            del self.adj[v][u]

    # ---------- recorridos ----------

    def bfs(self, start):
        """Barrido en amplitud desde start."""
        visited = set([start])
        order = []
        q = deque([start])

        while q:
            u = q.popleft()
            order.append(u)
            # vecinos ordenados por nombre para tener un resultado determinista
            for v in sorted(self.adj[u].keys()):
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return order

    def dfs(self, start):
        """Barrido en profundidad desde start."""
        visited = set()
        order = []

        def _dfs(u):
            visited.add(u)
            order.append(u)
            for v in sorted(self.adj[u].keys()):
                if v not in visited:
                    _dfs(v)

        _dfs(start)
        return order

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
        """Reconstruye el camino hasta 'target' usando el diccionario prev."""
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


def build_network():
    """Carga el grafo de la figura."""
    g = Graph()

    # a) nodos con tipo
    # computadoras
    g.add_node("Ubuntu", "pc")
    g.add_node("Mint", "pc")
    g.add_node("Manjaro", "pc")
    g.add_node("Fedora", "pc")
    g.add_node("Parrot", "pc")

    # notebooks
    g.add_node("Red Hat", "notebook")
    g.add_node("Debian", "notebook")
    g.add_node("Arch", "notebook")

    # impresora
    g.add_node("Impresora", "impresora")

    # servidores
    g.add_node("Guaraní", "servidor")
    g.add_node("MongoDB", "servidor")

    # switches
    g.add_node("Switch 1", "switch")
    g.add_node("Switch 2", "switch")

    # routers
    g.add_node("Router 1", "router")
    g.add_node("Router 2", "router")
    g.add_node("Router 3", "router")

    # aristas (no dirigidas) con pesos tomados del esquema
    # zona izquierda
    g.add_edge("Debian", "Switch 1", 17)
    g.add_edge("Ubuntu", "Switch 1", 18)
    g.add_edge("Mint", "Switch 1", 80)
    g.add_edge("Impresora", "Switch 1", 22)

    g.add_edge("Switch 1", "Router 1", 29)

    g.add_edge("Router 1", "Router 2", 37)
    g.add_edge("Router 2", "Router 3", 50)
    g.add_edge("Router 1", "Router 3", 43)

    g.add_edge("Router 2", "Red Hat", 25)
    g.add_edge("Router 2", "Guaraní", 9)

    # zona derecha
    g.add_edge("Router 3", "Switch 2", 61)

    g.add_edge("Switch 2", "Manjaro", 40)
    g.add_edge("Switch 2", "Parrot", 12)
    g.add_edge("Switch 2", "Arch", 56)
    g.add_edge("Switch 2", "Fedora", 3)
    g.add_edge("Switch 2", "MongoDB", 5)

    return g


def main():
    g = build_network()

    # b) barrido en profundidad y amplitud desde las tres notebooks
    notebooks = ["Red Hat", "Debian", "Arch"]
    print("b) Barridos DFS y BFS desde las notebooks:\n")
    for nb in notebooks:
        print(f"  Notebook: {nb}")
        print("    DFS:", " -> ".join(g.dfs(nb)))
        print("    BFS:", " -> ".join(g.bfs(nb)))
        print()

    # c) camino más corto desde Manjaro, Red Hat, Fedora hasta la impresora
    print("c) Caminos más cortos hasta la impresora:\n")
    origenes = ["Manjaro", "Red Hat", "Fedora"]
    for src in origenes:
        dist, prev = g.dijkstra(src)
        d = dist["Impresora"]
        path = Graph.build_path(prev, "Impresora")
        print(f"  Desde {src}: distancia = {d}, camino = {' -> '.join(path)}")
    print()

    # d) árbol de expansión mínima
    print("d) Árbol de expansión mínima (Kruskal):\n")
    mst, total = g.minimum_spanning_tree()
    for u, v, w in mst:
        print(f"  {u} -- {v} (peso {w})")
    print(f"  Peso total del árbol: {total}\n")

    # e) desde qué PC (no notebook) es más corto el camino a Guaraní
    print('e) PC con camino más corto al servidor "Guaraní":\n')
    pcs = [n for n, t in g.types.items() if t == "pc"]
    mejor_pc = None
    mejor_dist = float("inf")
    mejor_camino = None
    for pc in pcs:
        dist, prev = g.dijkstra(pc)
        d = dist["Guaraní"]
        path = Graph.build_path(prev, "Guaraní")
        print(f"  Desde {pc}: distancia = {d}, camino = {' -> '.join(path)}")
        if d < mejor_dist:
            mejor_dist = d
            mejor_pc = pc
            mejor_camino = path
    print(f"\n  Mejor PC: {mejor_pc}, distancia = {mejor_dist}")
    print("  Camino:", " -> ".join(mejor_camino))
    print()

    # f) desde qué computadora conectada al Switch 1 es más corto el camino a MongoDB
    print('f) Computadora del Switch 1 con camino más corto a "MongoDB":\n')
    comp_switch1 = [
        n for n in g.adj["Switch 1"]
        if g.types[n] in ("pc", "notebook")  # solo computadoras
    ]
    mejor_comp = None
    mejor_dist = float("inf")
    mejor_camino = None
    for comp in comp_switch1:
        dist, prev = g.dijkstra(comp)
        d = dist["MongoDB"]
        path = Graph.build_path(prev, "MongoDB")
        print(f"  Desde {comp}: distancia = {d}, camino = {' -> '.join(path)}")
        if d < mejor_dist:
            mejor_dist = d
            mejor_comp = comp
            mejor_camino = path
    print(f"\n  Mejor computadora del Switch 1: {mejor_comp}, distancia = {mejor_dist}")
    print("  Camino:", " -> ".join(mejor_camino))
    print()

    # g) cambiar la conexión de la impresora al Router 2 y repetir punto b
    print("g) Cambiando la impresora al Router 2 y repitiendo barridos:\n")
    # quitar arista impresora - switch 1
    g.remove_edge("Impresora", "Switch 1")
    # conectar impresora - router 2 con el mismo peso (22) o el que defina el enunciado
    g.add_edge("Impresora", "Router 2", 22)

    for nb in notebooks:
        print(f"  Notebook: {nb}")
        print("    DFS:", " -> ".join(g.dfs(nb)))
        print("    BFS:", " -> ".join(g.bfs(nb)))
        print()


if __name__ == "__main__":
    main()