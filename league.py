# equipos
# partidos
# liga (motor con estadísticas)

# clases, objetos, herencia, polimorfismo
import random


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"


class Jugador(Persona):
    def __init__(self, nombre, edad, posicion):
        super().__init__(nombre, edad)
        self.posicion = posicion

    def presentarse(self):
        return f"{super().presentarse()} y juego como {self.posicion}"


# self representa la instancia del objeto, súper se usa es para llamar métodos de la súper clase
class Entrenador(Persona):
    def __init__(self, nombre, edad, estrategia):
        super().__init__(nombre, edad)
        self.estrategia = estrategia

    def presentarse(self):
        return f"{super().presentarse()} y mi estrategia es {self.estrategia}"


class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.goles_favor = 0
        self.goles_contra = 0

    def puntos_update(self, goles_favor, goles_contra):
        if goles_favor > goles_contra:
            self.puntos += 3
        elif goles_favor == goles_contra:
            self.puntos += 1
        self.goles_favor += goles_favor
        self.goles_contra += goles_contra


# partidos
class Partido:
    def __init__(self, equipo1, equipo2, jugador1, jugador2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def jugar(self):
        golesequipo1 = random.randint(0, 5)
        golesequipo2 = random.randint(0, 5)
        self.equipo1.puntos_update(golesequipo1, golesequipo2)
        self.equipo2.puntos_update(golesequipo2, golesequipo1)
        if golesequipo1 > golesequipo2:
            print(
                f"Resultado: el equipo {self.equipo1.nombre} ha ganado al equipo {self.equipo2.nombre} por {golesequipo1} a {golesequipo2}"
            )
        elif golesequipo2 > golesequipo1:
            print(
                f"Resultado: el equipo {self.equipo2.nombre} ha ganado al equipo {self.equipo1.nombre} por {golesequipo2} a {golesequipo1}"
            )
        elif golesequipo2 == golesequipo1:
            print(
                f"los equipos {self.equipo1.nombre} y {self.equipo2.nombre} han empatado"
            )
        print(
            f"los jugadores {self.jugador1.nombre} y {self.jugador2.nombre} estuvieron presentes"
        )


class Liga:
    def __init__(self, equipos, jugador1, jugador2):
        self.equipos = equipos
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def todos_contra_todos(self):
        for i in range(len(self.equipos)):
            for j in range(i + 1, len(self.equipos)):
                partido = Partido(
                    self.equipos[i], self.equipos[j], self.jugador1, self.jugador2
                )
                partido.jugar()

    def ordenar_equipos(self):
        self.equipos.sort(key=lambda x: x.puntos, reverse=True)
        print("Tabla de posiciones")
        for equipo in self.equipos:
            print(
                f"{equipo.nombre}: {equipo.puntos} puntos | GF = {equipo.goles_favor} | GC = {equipo.goles_contra}"
            )

    def obtener_campeon(self):
        equipo_campeon = max(self.equipos, key=lambda equipo: equipo.puntos)
        print(f"felicidades al campeón: {equipo_campeon.nombre}")


city = Equipo("Manchester City")
haaland = Jugador("Haaland", 25, "delantero")
print(haaland.presentarse())

arsenal = Equipo("Arsenal")
saka = Jugador("Saka", 22, "delantero")
print(saka.presentarse())

boca = Equipo("boca")
nacional = Equipo("nacional")

equipos = [city, arsenal, boca, nacional]

mundial_de_clubes = Liga(equipos, haaland, saka)
mundial_de_clubes.todos_contra_todos()
mundial_de_clubes.ordenar_equipos()
mundial_de_clubes.obtener_campeon()


"""
dt1 = Entrenador("Pep Guardiola", 45, "ofensivo")
print(dt1.presentarse())

partido1 = Partido(city, arsenal, haaland, saka)
partido1.jugar()

print(arsenal.puntos)
print(city.puntos)
"""
