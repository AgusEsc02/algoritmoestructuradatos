from typing import List, Dict

# Estructura de datos para cada Jedi
class Jedi:
    def __init__(self, nombre: str, maestros: List[str], colores_sable: List[str], especie: str):
        self.nombre = nombre
        self.maestros = maestros
        self.colores_sable = colores_sable
        self.especie = especie

# Ejemplo de lista de Jedi 
jedis = [
    Jedi("Ahsoka Tano", ["Anakin Skywalker"], ["verde", "azul"], "togruta"),
    Jedi("Kit Fisto", ["Yoda"], ["verde"], "nautolan"),
    Jedi("Luke Skywalker", ["Yoda", "Obi-Wan Kenobi"], ["verde", "azul"], "humano"),
    Jedi("Qui-Gon Jin", ["Count Dooku"], ["verde"], "humano"),
    Jedi("Mace Windu", ["Cyslin Myr"], ["violeta"], "humano"),
    Jedi("Anakin Skywalker", ["Obi-Wan Kenobi"], ["azul", "rojo"], "humano"),
    Jedi("Aayla Secura", ["Quinlan Vos"], ["azul"], "twi'lek"),
    Jedi("Yoda", [], ["verde"], "unknown"),
   
]

# a. Listado ordenado por nombre y por especie
def listar_jedis_ordenados(jedis: List[Jedi]):
    por_nombre = sorted(jedis, key=lambda x: x.nombre)
    por_especie = sorted(jedis, key=lambda x: x.especie)
    return por_nombre, por_especie

# b. Mostrar toda la información de Ahsoka Tano y Kit Fisto
def mostrar_info_jedis(jedis: List[Jedi], nombres: List[str]):
    return [j for j in jedis if j.nombre in nombres]

# c. Mostrar todos los padawan de Yoda y Luke Skywalker
def padawans_de(jedis: List[Jedi], maestros: List[str]):
    return [j for j in jedis if any(m in j.maestros for m in maestros)]

# d. Mostrar los Jedi de especie humana y twi'lek
def jedis_por_especie(jedis: List[Jedi], especies: List[str]):
    return [j for j in jedis if j.especie in especies]

# e. Listar todos los Jedi que comienzan con A
def jedis_comienzan_con(jedis: List[Jedi], letra: str):
    return [j for j in jedis if j.nombre.startswith(letra)]

# f. Mostrar los Jedi que usaron sable de luz de más de un color
def jedis_multiples_colores(jedis: List[Jedi]):
    return [j for j in jedis if len(j.colores_sable) > 1]

# g. Indicar los Jedi que utilizaron sable de luz amarillo o violeta
def jedis_color_amarillo_violeta(jedis: List[Jedi]):
    return [j for j in jedis if "amarillo" in j.colores_sable or "violeta" in j.colores_sable]

# h. Indicar los nombres de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron
def nombres_padawans_de(jedis: List[Jedi], maestros: List[str]):
    return [j.nombre for j in jedis if any(m in j.maestros for m in maestros)]

# Ejemplo de uso:
if __name__ == "__main__":
    por_nombre, por_especie = listar_jedis_ordenados(jedis)
    info_ahsoka_kit = mostrar_info_jedis(jedis, ["Ahsoka Tano", "Kit Fisto"])
    padawans_yoda_luke = padawans_de(jedis, ["Yoda", "Luke Skywalker"])
    humanos_twilek = jedis_por_especie(jedis, ["humano", "twi'lek"])
    jedis_con_a = jedis_comienzan_con(jedis, "A")
    jedis_varios_colores = jedis_multiples_colores(jedis)
    jedis_amarillo_violeta = jedis_color_amarillo_violeta(jedis)
    padawans_quigon_mace = nombres_padawans_de(jedis, ["Qui-Gon Jin", "Mace Windu"])
