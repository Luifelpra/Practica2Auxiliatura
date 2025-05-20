#5.Desarrolla un POO para un equipo de fútbol y sus jugadores. El equipo está compuesto por jugadores, y si el equipo se destruye, los jugadores también se destruyen. Además, los jugadores pueden ser de diferentes tipos (portero, defensa, mediocampista, delantero).
# Clase Padre: Jugador<nombre, número, posición>
# Métodos: mostrar_info() (muestra el nombre, número y posición del jugador)
# Clases Derivadas: Portero, Defensa, Mediocampista, Delantero (heredan de Jugador)
# Atributos adicionales: habilidad_especial (ej: "Atajadas", "Marcaje", "Pases", "Goles")
# Clase: Equipo<nombre, jugadores (lista de objetos de tipo Jugador)>
# Métodos: agregar_jugador(jugador), mostrar_equipo() (muestra el nombre del equipo y la información de todos los jugadores)
#   a)Implementa las clases con sus constructores, getters y setters.
#   b)Crea un equipo y agrega varios jugadores de diferentes tipos.
#   c)Muestra la información del equipo y sus jugadores.
class Jugador:
    def __init__(self, nombre, numero, posicion):
        self.nombre = nombre
        self.numero = numero
        self.posicion = posicion

    def mostrar_info(self):
        print(f"{self.nombre} - #{self.numero} - Posición: {self.posicion}")

class Portero(Jugador):
    def __init__(self, nombre, numero, habilidad):
        super().__init__(nombre, numero, "Portero")
        self.habilidad = habilidad

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Habilidad especial: {self.habilidad}")

class Defensa(Jugador):
    def __init__(self, nombre, numero, habilidad):
        super().__init__(nombre, numero, "Defensa")
        self.habilidad = habilidad

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Habilidad especial: {self.habilidad}")

class Mediocampista(Jugador):
    def __init__(self, nombre, numero, habilidad):
        super().__init__(nombre, numero, "Mediocampista")
        self.habilidad = habilidad

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Habilidad especial: {self.habilidad}")

class Delantero(Jugador):
    def __init__(self, nombre, numero, habilidad):
        super().__init__(nombre, numero, "Delantero")
        self.habilidad = habilidad

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Habilidad especial: {self.habilidad}")

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def mostrar_equipo(self):
        print(f"Equipo: {self.nombre}")
        for j in self.jugadores:
            j.mostrar_info()

equipo = Equipo("Los Tigres")
equipo.agregar_jugador(Portero("Carlos", 1, "Atajadas"))
equipo.agregar_jugador(Defensa("Juan", 5, "Marcaje"))
equipo.agregar_jugador(Mediocampista("Luis", 8, "Pases"))
equipo.agregar_jugador(Delantero("Pedro", 9, "Goles"))
equipo.mostrar_equipo()
