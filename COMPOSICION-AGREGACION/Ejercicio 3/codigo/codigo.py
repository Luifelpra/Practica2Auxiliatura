#3.Crea un POO de clases para modelar un avión y sus partes. El avión está compuesto por partes como el motor, las alas y el tren de aterrizaje. Si el avión se destruye, las partes también se destruyen.
# Parte<nombre, peso (en kg)Métodos: mostrar_info() (muestra el nombre y el peso de la parte)
# Avión<modelo, fabricante, partes (lista de objetos de tipo Parte)
# Métodos: agregar_parte(parte), mostrar_avión() (muestra el modelo, fabricante y la información de todas las partes)
#   a)Implementa las clases con sus constructores, getters y setters.
#   b)Crea un avión y agrega varias partes.
#   c)Muestra la información del avión y sus partes.
class Parte:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    def mostrar_info(self):
        print(f"Parte: {self.nombre}, Peso: {self.peso} kg")

class Avion:
    def __init__(self, modelo, fabricante):
        self.modelo = modelo
        self.fabricante = fabricante
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def mostrar_avion(self):
        print(f"Modelo: {self.modelo}, Fabricante: {self.fabricante}")
        for parte in self.partes:
            parte.mostrar_info()

avion = Avion("A320", "Airbus")
avion.agregar_parte(Parte("Motor", 1500))
avion.agregar_parte(Parte("Ala", 800))
avion.mostrar_avion()
