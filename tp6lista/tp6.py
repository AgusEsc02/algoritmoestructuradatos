class Superheroe:
    def __init__(self, nombre, anio_aparicion, casa, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSuperheroes:
    def __init__(self):
        self.inicio = None

    def agregar(self, superheroe):
        nodo = Nodo(superheroe)
        nodo.siguiente = self.inicio
        self.inicio = nodo

    def eliminar_por_nombre(self, nombre):
        actual = self.inicio
        anterior = None
        while actual:
            if actual.dato.nombre == nombre:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.inicio = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar_por_nombre(self, nombre):
        actual = self.inicio
        while actual:
            if actual.dato.nombre == nombre:
                return actual.dato
            actual = actual.siguiente
        return None

    def cambiar_casa(self, nombre, nueva_casa):
        heroe = self.buscar_por_nombre(nombre)
        if heroe:
            heroe.casa = nueva_casa

    def mostrar_por_palabra_biografia(self, palabras):
        actual = self.inicio
        resultado = []
        while actual:
            if any(palabra in actual.dato.biografia.lower() for palabra in palabras):
                resultado.append(actual.dato.nombre)
            actual = actual.siguiente
        return resultado

    def mostrar_antes_de_anio(self, anio):
        actual = self.inicio
        resultado = []
        while actual:
            if actual.dato.anio_aparicion < anio:
                resultado.append((actual.dato.nombre, actual.dato.casa))
            actual = actual.siguiente
        return resultado

    def mostrar_casa_de(self, nombres):
        resultado = {}
        for nombre in nombres:
            heroe = self.buscar_por_nombre(nombre)
            if heroe:
                resultado[nombre] = heroe.casa
        return resultado

    def mostrar_info_de(self, nombres):
        resultado = []
        for nombre in nombres:
            heroe = self.buscar_por_nombre(nombre)
            if heroe:
                resultado.append(vars(heroe))
        return resultado

    def listar_por_letras(self, letras):
        actual = self.inicio
        resultado = []
        letras = [letra.upper() for letra in letras]
        while actual:
            if actual.dato.nombre[0].upper() in letras:
                resultado.append(actual.dato.nombre)
            actual = actual.siguiente
        return resultado

    def contar_por_casa(self):
        actual = self.inicio
        conteo = {}
        while actual:
            casa = actual.dato.casa
            conteo[casa] = conteo.get(casa, 0) + 1
            actual = actual.siguiente
        return conteo

# Ejemplo de uso:
lista = ListaSuperheroes()
lista.agregar(Superheroe("Linterna Verde", 1940, "DC", "Usa un anillo y traje especial"))
lista.agregar(Superheroe("Wolverine", 1974, "Marvel", "Tiene garras y armadura"))
lista.agregar(Superheroe("Dr. Strange", 1963, "DC", "Hechicero con traje místico"))
lista.agregar(Superheroe("Capitana Marvel", 1967, "Marvel", "Poderosa con traje especial"))
lista.agregar(Superheroe("Mujer Maravilla", 1941, "DC", "Guerrera con armadura"))
lista.agregar(Superheroe("Flash", 1940, "DC", "Velocidad y traje rojo"))
lista.agregar(Superheroe("Star-Lord", 1976, "Marvel", "Líder con armadura espacial"))
lista.agregar(Superheroe("Batman", 1939, "DC", "Detective con traje y gadgets"))
lista.agregar(Superheroe("Spider-Man", 1962, "Marvel", "Traje de araña"))
lista.agregar(Superheroe("Superman", 1938, "DC", "Traje azul y capa roja"))

# a. Eliminar Linterna Verde
lista.eliminar_por_nombre("Linterna Verde")

# b. Mostrar año de aparición de Wolverine
print(lista.buscar_por_nombre("Wolverine").anio_aparicion)

# c. Cambiar casa de Dr. Strange a Marvel
lista.cambiar_casa("Dr. Strange", "Marvel")

# d. Mostrar nombres con "traje" o "armadura" en biografía
print(lista.mostrar_por_palabra_biografia(["traje", "armadura"]))

# e. Mostrar nombre y casa de los que aparecieron antes de 1963
print(lista.mostrar_antes_de_anio(1963))

# f. Mostrar casa de Capitana Marvel y Mujer Maravilla
print(lista.mostrar_casa_de(["Capitana Marvel", "Mujer Maravilla"]))

# g. Mostrar toda la información de Flash y Star-Lord
print(lista.mostrar_info_de(["Flash", "Star-Lord"]))

# h. Listar superhéroes que comienzan con B, M y S
print(lista.listar_por_letras(["B", "M", "S"]))

# i. Determinar cuántos superhéroes hay de cada casa
print(lista.contar_por_casa())