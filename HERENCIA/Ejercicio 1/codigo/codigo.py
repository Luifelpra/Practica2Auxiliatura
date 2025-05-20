#1. Modelar diferentes tipos de vehículos. Las clases deben tener las siguientes características:
# Vehículo<marca, modelo, año, precio_base>
# Métodos: mostrar_info() muestra la información básica del vehículo
# Coche (hereda de Vehículo)< num_puertas, tipo_combustible>
# Métodos: mostrar_info() debe mostrar la información básica más losatributos adicionales
# Moto (hereda de Vehículo)< cilindrada, tipo_motor>
# Métodos: mostrar_info() debe mostrar la información básica más losatributos adicionales
# a) Implementa las clases con sus constructores, getters y setters.
# b) Crea instancias de Coche y Moto y muestra su información usando elmétodo mostrar_info().
# c) Muestra todos los coches que tienen más de 4 puertas.
# d) Mostrar los coches y motos actuales (gestión 2025)
class Vehiculo:
    def __init__(self, marca, modelo, año, precio_base):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio_base = precio_base
    
    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Precio Base: {self.precio_base}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, precio_base, num_puertas, tipo_combustible):
        super().__init__(marca, modelo, año, precio_base)
        self.num_puertas = num_puertas
        self.tipo_combustible = tipo_combustible
    
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Número de Puertas: {self.num_puertas}, Tipo de Combustible: {self.tipo_combustible}"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, precio_base, cilindrada, tipo_motor):
        super().__init__(marca, modelo, año, precio_base)
        self.cilindrada = cilindrada
        self.tipo_motor = tipo_motor
    
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Cilindrada: {self.cilindrada}, Tipo de Motor: {self.tipo_motor}"

coche1 = Coche("Toyota", "Corolla", 2022, 25000, 5, "Gasolina")
coche2 = Coche("Ford", "Mustang", 2025, 45000, 2, "Gasolina")
moto1 = Moto("Honda", "CBR600", 2021, 12000, "600cc", "4 tiempos")

print("Información de Vehículos")
print(coche1.mostrar_info())
print(coche2.mostrar_info())
print(moto1.mostrar_info())

print("\nCoches con más de 4 puertas")
coches = [coche1, coche2]
for coche in coches:
    if coche.num_puertas > 4:
        print(coche.mostrar_info())

print("\nVehículos de gestión 2025")
vehiculos = [coche1, coche2, moto1]
for vehiculo in vehiculos:
    if vehiculo.año == 2025:
        print(vehiculo.mostrar_info())