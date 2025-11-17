from collections import deque
from collections import Counter

class Criatura:
    def __init__(self, nombre, derrotado_por=None, descripcion="", capturada_por=None):
        self.nombre = nombre
        self.derrotado_por = derrotado_por if derrotado_por else []
        self.descripcion = descripcion
        self.capturada_por = capturada_por
        self.izq = None
        self.der = None

class ArbolCriaturas:
    def __init__(self):
        self.raiz = None

    def insertar(self, criatura):
        def _insertar(nodo, criatura):
            if not nodo:
                return criatura
            if criatura.nombre < nodo.nombre:
                nodo.izq = _insertar(nodo.izq, criatura)
            else:
                nodo.der = _insertar(nodo.der, criatura)
            return nodo
        self.raiz = _insertar(self.raiz, criatura)

    def inorden(self):
        res = []
        def _inorden(nodo):
            if nodo:
                _inorden(nodo.izq)
                res.append((nodo.nombre, nodo.derrotado_por))
                _inorden(nodo.der)
        _inorden(self.raiz)
        return res

    def buscar(self, nombre):
        def _buscar(nodo, nombre):
            if not nodo:
                return None
            if nodo.nombre == nombre:
                return nodo
            elif nombre < nodo.nombre:
                return _buscar(nodo.izq, nombre)
            else:
                return _buscar(nodo.der, nombre)
        return _buscar(self.raiz, nombre)

    def modificar_nombre(self, viejo, nuevo):
        nodo = self.buscar(viejo)
        if nodo:
            nodo.nombre = nuevo

    def modificar_descripcion(self, nombre, descripcion):
        nodo = self.buscar(nombre)
        if nodo:
            nodo.descripcion = descripcion

    def modificar_captura(self, nombre, capturador):
        nodo = self.buscar(nombre)
        if nodo:
            nodo.capturada_por = capturador

    def eliminar(self, nombre):
        def _eliminar(nodo, nombre):
            if not nodo:
                return None
            if nombre < nodo.nombre:
                nodo.izq = _eliminar(nodo.izq, nombre)
            elif nombre > nodo.nombre:
                nodo.der = _eliminar(nodo.der, nombre)
            else:
                if not nodo.izq:
                    return nodo.der
                if not nodo.der:
                    return nodo.izq
                temp = nodo.der
                while temp.izq:
                    temp = temp.izq
                nodo.nombre, nodo.derrotado_por, nodo.descripcion, nodo.capturada_por = temp.nombre, temp.derrotado_por, temp.descripcion, temp.capturada_por
                nodo.der = _eliminar(nodo.der, temp.nombre)
            return nodo
        self.raiz = _eliminar(self.raiz, nombre)

    def listar_por_nivel(self):
        res = []
        q = deque()
        if self.raiz:
            q.append(self.raiz)
        while q:
            nodo = q.popleft()
            res.append(nodo.nombre)
            if nodo.izq:
                q.append(nodo.izq)
            if nodo.der:
                q.append(nodo.der)
        return res

    def criaturas_derrotadas_por(self, heroe):
        res = []
        def _recorrer(nodo):
            if nodo:
                if heroe in nodo.derrotado_por:
                    res.append(nodo.nombre)
                _recorrer(nodo.izq)
                _recorrer(nodo.der)
        _recorrer(self.raiz)
        return res

    def criaturas_no_derrotadas(self):
        res = []
        def _recorrer(nodo):
            if nodo:
                if not nodo.derrotado_por:
                    res.append(nodo.nombre)
                _recorrer(nodo.izq)
                _recorrer(nodo.der)
        _recorrer(self.raiz)
        return res

    def criaturas_capturadas_por(self, heroe):
        res = []
        def _recorrer(nodo):
            if nodo:
                if nodo.capturada_por == heroe:
                    res.append(nodo.nombre)
                _recorrer(nodo.izq)
                _recorrer(nodo.der)
        _recorrer(self.raiz)
        return res

    def busqueda_coincidencia(self, texto):
        res = []
        def _recorrer(nodo):
            if nodo:
                if texto.lower() in nodo.nombre.lower():
                    res.append(nodo.nombre)
                _recorrer(nodo.izq)
                _recorrer(nodo.der)
        _recorrer(self.raiz)
        return res

    def top_derrotadores(self, top_n=3):
        derrotadores = []
        def _recorrer(nodo):
            if nodo:
                derrotadores.extend(nodo.derrotado_por)
                _recorrer(nodo.izq)
                _recorrer(nodo.der)
        _recorrer(self.raiz)
        return Counter(derrotadores).most_common(top_n)

# Cargar criaturas según la tabla
criaturas_data = [
    ("Ceto", [], ""),
    ("Tifón", ["Zeus"], ""),
    ("Equidna", ["Argos Panoptes"], ""),
    ("Dino", [], ""),
    ("Pefredo", [], ""),
    ("Enio", [], ""),
    ("Escila", [], ""),
    ("Caribdis", [], ""),
    ("Euríale", [], ""),
    ("Esteno", [], ""),
    ("Medusa", ["Perseo"], ""),
    ("Ladón", ["Heracles", "Argos Panoptes", "Hermes"], ""),
    ("Águila del Cáucaso", [], ""),
    ("Quimera", ["Belerofonte"], ""),
    ("Hidra de Lerna", ["Heracles"], ""),
    ("León de Nemea", ["Heracles"], ""),
    ("Esfinge", ["Edipo"], ""),
    ("Dragón de la Cólquida", [], ""),
    ("Cerbero", [], ""),
    ("Cerda de Cromión", ["Teseo"], ""),
    ("Ortro", ["Heracles"], ""),
    ("Toro de Creta", ["Teseo"], ""),
    ("Jabalí de Calidón", ["Atalanta"], ""),
    ("Carcinos", [], ""),
    ("Gerión", ["Heracles"], ""),
    ("Cloto", [], ""),
    ("Láquesis", [], ""),
    ("Átropos", [], ""),
    ("Minotauro de Creta", ["Teseo"], ""),
    ("Harpías", [], ""),
    ("Aves del Estínfalo", [], ""),
    ("Talos", ["Medea"], ""),
    ("Sirenas", [], ""),
    ("Pitón", ["Apolo"], ""),
    ("Cierva de Cerinea", [], ""),
    ("Basilisco", [], ""),
    ("Jabalí de Erimanto", [], ""),
]

arbol = ArbolCriaturas()
for nombre, derrotado_por, descripcion in criaturas_data:
    arbol.insertar(Criatura(nombre, derrotado_por, descripcion))

# b. Permitir cargar descripción
arbol.modificar_descripcion("Talos", "Gigante de bronce que protegía Creta.")

# c. Mostrar toda la información de Talos
talos = arbol.buscar("Talos")
if talos:
    print(f"Nombre: {talos.nombre}\nDerrotado por: {talos.derrotado_por}\nDescripción: {talos.descripcion}\nCapturada por: {talos.capturada_por}")

# h. Modificar nodos indicando que Heracles las atrapó
for nombre in ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]:
    arbol.modificar_captura(nombre, "Heracles")

# j. Eliminar Basilisco y Sirenas
arbol.eliminar("Basilisco")
arbol.eliminar("Sirenas")

# k. Modificar Aves del Estínfalo, agregando que Heracles derrotó a varias
aves = arbol.buscar("Aves del Estínfalo")
if aves:
    aves.derrotado_por.append("Heracles")

# l. Modificar nombre Ladón por Dragón Ladón
arbol.modificar_nombre("Ladón", "Dragón Ladón")

# Ejemplo de consultas:
# a. Listado inorden de criaturas y quienes la derrotaron
print("Inorden:")
for nombre, derrotadores in arbol.inorden():
    print(f"{nombre}: {derrotadores}")

# d. Top 3 héroes/dioses que derrotaron más criaturas
print("Top derrotadores:", arbol.top_derrotadores())

# e. Listar criaturas derrotadas por Heracles
print("Derrotadas por Heracles:", arbol.criaturas_derrotadas_por("Heracles"))

# f. Listar criaturas no derrotadas
print("No derrotadas:", arbol.criaturas_no_derrotadas())

# m. Listado por nivel
print("Por nivel:", arbol.listar_por_nivel())

# n. Criaturas capturadas por Heracles
print("Capturadas por Heracles:", arbol.criaturas_capturadas_por("Heracles"))

# i. Búsqueda por coincidencia
print("Coincidencia 'Dragón':", arbol.busqueda_coincidencia("Dragón"))