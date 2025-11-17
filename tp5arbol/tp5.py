class NodoArbol:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe  # True: héroe, False: villano
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, es_heroe):
        def _insertar(nodo, nombre, es_heroe):
            if nodo is None:
                return NodoArbol(nombre, es_heroe)
            if nombre.lower() < nodo.nombre.lower():
                nodo.izq = _insertar(nodo.izq, nombre, es_heroe)
            else:
                nodo.der = _insertar(nodo.der, nombre, es_heroe)
            return nodo
        self.raiz = _insertar(self.raiz, nombre, es_heroe)

    def listar_villanos_ordenados(self):
        resultado = []
        def _inorden(nodo):
            if nodo:
                _inorden(nodo.izq)
                if not nodo.es_heroe:
                    resultado.append(nodo.nombre)
                _inorden(nodo.der)
        _inorden(self.raiz)
        return resultado

    def superheroes_con_C(self):
        resultado = []
        def _inorden(nodo):
            if nodo:
                _inorden(nodo.izq)
                if nodo.es_heroe and nodo.nombre.startswith('C'):
                    resultado.append(nodo.nombre)
                _inorden(nodo.der)
        _inorden(self.raiz)
        return resultado

    def contar_superheroes(self):
        def _contar(nodo):
            if nodo is None:
                return 0
            return _contar(nodo.izq) + _contar(nodo.der) + (1 if nodo.es_heroe else 0)
        return _contar(self.raiz)

    def buscar_y_modificar(self, nombre_prox, nuevo_nombre):
        def _buscar(nodo):
            if nodo is None:
                return False
            if nombre_prox.lower() in nodo.nombre.lower():
                nodo.nombre = nuevo_nombre
                return True
            return _buscar(nodo.izq) or _buscar(nodo.der)
        return _buscar(self.raiz)

    def listar_superheroes_descendente(self):
        resultado = []
        def _descendente(nodo):
            if nodo:
                _descendente(nodo.der)
                if nodo.es_heroe:
                    resultado.append(nodo.nombre)
                _descendente(nodo.izq)
        _descendente(self.raiz)
        return resultado

    def generar_bosque(self):
        arbol_heroes = ArbolBinario()
        arbol_villanos = ArbolBinario()
        def _recorrer(nodo):
            if nodo:
                if nodo.es_heroe:
                    arbol_heroes.insertar(nodo.nombre, True)
                else:
                    arbol_villanos.insertar(nodo.nombre, False)
                _recorrer(nodo.izq)
                _recorrer(nodo.der)
        _recorrer(self.raiz)
        return arbol_heroes, arbol_villanos

    def contar_nodos(self):
        def _contar(nodo):
            if nodo is None:
                return 0
            return 1 + _contar(nodo.izq) + _contar(nodo.der)
        return _contar(self.raiz)

    def barrido_ordenado(self):
        resultado = []
        def _inorden(nodo):
            if nodo:
                _inorden(nodo.izq)
                resultado.append(nodo.nombre)
                _inorden(nodo.der)
        _inorden(self.raiz)
        return resultado

# Ejemplo de uso:
arbol = ArbolBinario()
datos = [
    ("Iron Man", True), ("Thanos", False), ("Captain America", True),
    ("Loki", False), ("Doctor Strenge", True), ("Ultron", False),
    ("Black Widow", True), ("Hela", False), ("Hawkeye", True),
    ("Vision", True), ("Red Skull", False), ("Spider-Man", True),
    ("Captain Marvel", True), ("Dormammu", False)
]
for nombre, es_heroe in datos:
    arbol.insertar(nombre, es_heroe)

# b. Villanos ordenados
print("Villanos ordenados:", arbol.listar_villanos_ordenados())

# c. Superhéroes que empiezan con C
print("Superhéroes con C:", arbol.superheroes_con_C())

# d. Cantidad de superhéroes
print("Cantidad de superhéroes:", arbol.contar_superheroes())

# e. Corregir Doctor Strange
arbol.buscar_y_modificar("Strenge", "Doctor Strange")

# f. Superhéroes descendente
print("Superhéroes descendente:", arbol.listar_superheroes_descendente())

# g. Generar bosque y resolver tareas
arbol_heroes, arbol_villanos = arbol.generar_bosque()
print("Nodos en árbol de héroes:", arbol_heroes.contar_nodos())
print("Nodos en árbol de villanos:", arbol_villanos.contar_nodos())
print("Barrido héroes:", arbol_heroes.barrido_ordenado())
print("Barrido villanos:", arbol_villanos.barrido_ordenado())