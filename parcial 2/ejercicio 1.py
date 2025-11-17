from collections import deque
from dataclasses import dataclass
from typing import Any, List, Optional, Tuple




@dataclass
class Pokemon:
    numero: int
    nombre: str
    tipos: List[str]
    debilidades: List[str]
    mega: bool
    gigamax: bool



# Árbol binario de búsqueda genérico


class NodoABB:
    def __init__(self, clave: Any, dato: Any):
        self.clave = clave
        self.dato = dato        
        self.izq: Optional['NodoABB'] = None
        self.der: Optional['NodoABB'] = None


def insertar(raiz: Optional[NodoABB], clave: Any, dato: Any) -> NodoABB:
    """Inserta por clave en un ABB. Si la raíz es None, crea el nodo."""
    if raiz is None:
        return NodoABB(clave, dato)
    if clave < raiz.clave:
        raiz.izq = insertar(raiz.izq, clave, dato)
    elif clave > raiz.clave:
        raiz.der = insertar(raiz.der, clave, dato)
    else:
        
        raiz.dato = dato
    return raiz


def buscar(raiz: Optional[NodoABB], clave: Any) -> Optional[NodoABB]:
    """Búsqueda estándar en ABB."""
    if raiz is None:
        return None
    if clave == raiz.clave:
        return raiz
    if clave < raiz.clave:
        return buscar(raiz.izq, clave)
    else:
        return buscar(raiz.der, clave)


def inorden(raiz: Optional[NodoABB], visitar) -> None:
    """Recorrido inorden (izq, nodo, der). 'visitar' es una función."""
    if raiz is None:
        return
    inorden(raiz.izq, visitar)
    visitar(raiz)
    inorden(raiz.der, visitar)


def por_niveles(raiz: Optional[NodoABB], visitar) -> None:
    """Recorrido por niveles (BFS)."""
    if raiz is None:
        return
    q = deque([raiz])
    while q:
        nodo = q.popleft()
        visitar(nodo)
        if nodo.izq:
            q.append(nodo.izq)
        if nodo.der:
            q.append(nodo.der)



# Construcción de los tres árboles
#   - árbol por número
#   - árbol por nombre
#   - árbol por tipo


def construir_arboles(pokemons: List[Pokemon]) -> Tuple[NodoABB, NodoABB, NodoABB]:
    arbol_numero: Optional[NodoABB] = None
    arbol_nombre: Optional[NodoABB] = None
    arbol_tipo: Optional[NodoABB] = None

    for p in pokemons:
        # Normalizamos a minúsculas para las claves de texto
        nombre_clave = p.nombre.lower()
        arbol_numero = insertar(arbol_numero, p.numero, p)
        arbol_nombre = insertar(arbol_nombre, nombre_clave, p)

        # Para el árbol de tipo, la clave es el tipo (str) y el dato es una lista de pokémon
        for t in p.tipos:
            tipo_clave = t.lower()
            nodo_tipo = buscar(arbol_tipo, tipo_clave)
            if nodo_tipo is None:
                # Creamos la lista con este primer pokémon
                arbol_tipo = insertar(arbol_tipo, tipo_clave, [p])
            else:
                nodo_tipo.dato.append(p)

    # Por tipado, garantizamos no-None para retorno (asumimos al menos 1 pokémon)
    return arbol_numero, arbol_nombre, arbol_tipo



# 1) Mostrar todos los datos de un Pokémon por número


def buscar_por_numero(arbol_numero: NodoABB, numero: int) -> Optional[Pokemon]:
    nodo = buscar(arbol_numero, numero)
    return nodo.dato if nodo else None



# 2) Mostrar datos por nombre con búsqueda por proximidad
#    (subcadena, por ejemplo "bul")


def buscar_por_nombre_proximidad(arbol_nombre: NodoABB, subcadena: str) -> List[Pokemon]:
    sub = subcadena.lower()
    resultado: List[Pokemon] = []

    def visitar(nodo: NodoABB):
        if sub in nodo.clave:      # nodo.clave es el nombre en lower
            resultado.append(nodo.dato)

    inorden(arbol_nombre, visitar)
    return resultado



# 3) Mostrar todos los nombres de los pokémon de un tipo dado
#    (fantasma, fuego, acero, eléctrico, etc.)


def nombres_por_tipo(arbol_tipo: NodoABB, tipo: str) -> List[str]:
    tipo_clave = tipo.lower()
    nodo = buscar(arbol_tipo, tipo_clave)
    if nodo is None:
        return []
    return [p.nombre for p in nodo.dato]



# 4) Listado ascendente por número y por nombre,
#    y listado por niveles por nombre


def listado_ascendente_por_numero(arbol_numero: NodoABB) -> List[Pokemon]:
    lista: List[Pokemon] = []

    def visitar(nodo: NodoABB):
        lista.append(nodo.dato)

    inorden(arbol_numero, visitar)
    return lista


def listado_ascendente_por_nombre(arbol_nombre: NodoABB) -> List[Pokemon]:
    lista: List[Pokemon] = []

    def visitar(nodo: NodoABB):
        lista.append(nodo.dato)

    inorden(arbol_nombre, visitar)
    return lista


def listado_por_niveles_nombre(arbol_nombre: NodoABB) -> List[Pokemon]:
    lista: List[Pokemon] = []

    def visitar(nodo: NodoABB):
        lista.append(nodo.dato)

    por_niveles(arbol_nombre, visitar)
    return lista



# 5) Mostrar todos los pokémon que son débiles frente a
#   Jolteon, Lycanroc y Tyrantrum


def buscar_por_nombre_exacta(arbol_nombre: NodoABB, nombre: str) -> Optional[Pokemon]:
    """Búsqueda exacta por nombre (no por proximidad)."""
    nodo = buscar(arbol_nombre, nombre.lower())
    return nodo.dato if nodo else None


def debiles_frente_a(arbol_nombre: NodoABB,
                     arbol_numero: NodoABB,
                     nombres_atacantes: List[str]) -> List[Pokemon]:
    # 1) Obtener tipos de los atacantes
    tipos_ataque = set()
    for nom in nombres_atacantes:
        p = buscar_por_nombre_exacta(arbol_nombre, nom)
        if p:
            for t in p.tipos:
                tipos_ataque.add(t.lower())

    # 2) Recorrer todos los pokémon y ver si tienen alguna debilidad en esos tipos
    resultado: List[Pokemon] = []

    def visitar(nodo: NodoABB):
        p = nodo.dato
        for deb in p.debilidades:
            if deb.lower() in tipos_ataque:
                resultado.append(p)
                break

    inorden(arbol_numero, visitar)
    return resultado


# ---------------------------------------------------------
# 6) Mostrar todos los tipos de pokémon y cuántos hay de cada tipo
# ---------------------------------------------------------

def cantidad_por_tipo(arbol_tipo: NodoABB) -> List[Tuple[str, int]]:
    res: List[Tuple[str, int]] = []

    def visitar(nodo: NodoABB):
        tipo = nodo.clave          # string
        cantidad = len(nodo.dato)  # lista de Pokemon
        res.append((tipo, cantidad))

    inorden(arbol_tipo, visitar)
    return res



# 7) Determinar cuántos pokémon tienen megaevolución
# 8) Determinar cuántos tienen forma gigamax


def contar_mega_y_gigamax(arbol_numero: NodoABB) -> Tuple[int, int]:
    mega = 0
    giga = 0

    def visitar(nodo: NodoABB):
        nonlocal mega, giga
        p = nodo.dato
        if p.mega:
            mega += 1
        if p.gigamax:
            giga += 1

    inorden(arbol_numero, visitar)
    return mega, giga



# EJEMPLO DE USO 


if __name__ == "__main__":
    # Ejemplo mínimo para probar:
    pokemons = [
        Pokemon(25, "Pikachu", ["Eléctrico"], ["Tierra"], mega=False, gigamax=True),
        Pokemon(135, "Jolteon", ["Eléctrico"], ["Tierra"], mega=False, gigamax=False),
        Pokemon(744, "Rockruff", ["Roca"], ["Agua", "Planta", "Acero", "Lucha", "Tierra"], mega=False, gigamax=False),
        Pokemon(745, "Lycanroc", ["Roca"], ["Agua", "Planta", "Acero", "Lucha", "Tierra"], mega=False, gigamax=False),
        Pokemon(697, "Tyrantrum", ["Roca", "Dragón"], ["Acero", "Hada", "Dragón", "Lucha", "Tierra", "Hielo"], mega=False, gigamax=False),
        Pokemon(1, "Bulbasaur", ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"], mega=False, gigamax=False),
    ]

    arbol_numero, arbol_nombre, arbol_tipo = construir_arboles(pokemons)

    # a) Buscar por número
    p = buscar_por_numero(arbol_numero, 25)
    if p:
        print("Por número 25:", p)

    # b) Buscar por nombre proximidad
    encontrados = buscar_por_nombre_proximidad(arbol_nombre, "bul")
    print("Búsqueda por 'bul':", [x.nombre for x in encontrados])

    # c) Nombres por tipo
    print("Tipo eléctrico:", nombres_por_tipo(arbol_tipo, "eléctrico"))

    # d) Listado ascendente por número
    print("Ascendente por número:", [p.nombre for p in listado_ascendente_por_numero(arbol_numero)])

    # e) Listado por niveles por nombre
    print("Por niveles (nombre):", [p.nombre for p in listado_por_niveles_nombre(arbol_nombre)])

    # f) Débiles frente a Jolteon, Lycanroc y Tyrantrum
    debiles = debiles_frente_a(arbol_nombre, arbol_numero,
                               ["Jolteon", "Lycanroc", "Tyrantrum"])
    print("Débiles frente a Jolteon/Lycanroc/Tyrantrum:",
          [p.nombre for p in debiles])

    # g) Cantidad por tipo
    print("Cantidad por tipo:", cantidad_por_tipo(arbol_tipo))

    # h) Mega y Gigamax
    mega, giga = contar_mega_y_gigamax(arbol_numero)
    print("Con megaevolución:", mega)
    print("Con gigamax:", giga)
    