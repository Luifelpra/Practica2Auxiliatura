#1.Sean las siguientes clases:Habitación<nombre, tamaño (en metros cuadrados)
# Métodos: mostrar_info() (muestra el nombre y tamaño de la habitación)
# Casa<dirección, habitaciones (lista de objetos de tipo Habitación) Métodos: agregar_habitacion(habitacion), mostrar_casa() (muestra la dirección y la información de todas las habitaciones)
#   a)Implementa las clases con sus constructores, getters y setters.
#   b)Crea una casa y agrega varias habitaciones.
#   c)Muestra la información de la casa y sus habitaciones.
class Habitacion:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano

    def mostrar_info(self):
        print(f"Habitación: {self.nombre}, Tamaño: {self.tamano} m2")

class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_casa(self):
        print(f"Dirección: {self.direccion}")
        for h in self.habitaciones:
            h.mostrar_info()

casa = Casa("Av. Siempre Viva 742")
casa.agregar_habitacion(Habitacion("Sala", 20))
casa.agregar_habitacion(Habitacion("Cocina", 12))
casa.mostrar_casa()
