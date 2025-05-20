#5.Definir las siguientes clases:
# Empleado<nombre, apellido, salario_base, años_antigüedad Métodos: calcular_salario() (retorna el salario base más un bono del 5% por cada año de antigüedad)Gerente (hereda de Empleado)< departamento, bono_gerencial>
# Métodos: calcular_salario() (debe sumar el bono gerencial al salario calculado en la clase base)
# Desarrollador (hereda de Empleado) <lenguaje_programación, horas_extras>
# Métodos: calcular_salario() (debe sumar un monto adicional por horas extras al salario calculado en la clase base)
#   a)Implementa las clases con sus constructores, getters y setters.
#   b)Crea instancias de Gerente y Desarrollador y muestra su salario calculado.
#   c)Muestra todos los gerentes que tienen un bono gerencial mayor a 1000.
#   d)Muestra todos los desarrolladores que trabajan más de 10 horas extras.
class Empleado:
    def __init__(self, nombre, apellido, salario_base, años_antigüedad):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base = salario_base
        self.años_antigüedad = años_antigüedad
    
    def calcular_salario(self):
        bono = self.salario_base * 0.05 * self.años_antigüedad
        return self.salario_base + bono
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre} {self.apellido}, Salario Base: {self.salario_base}, Años Antigüedad: {self.años_antigüedad}"

class Gerente(Empleado):
    def __init__(self, nombre, apellido, salario_base, años_antigüedad, departamento, bono_gerencial):
        super().__init__(nombre, apellido, salario_base, años_antigüedad)
        self.departamento = departamento
        self.bono_gerencial = bono_gerencial
    
    def calcular_salario(self):
        salario_base = super().calcular_salario()
        return salario_base + self.bono_gerencial
    
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Departamento: {self.departamento}, Bono Gerencial: {self.bono_gerencial}"

class Desarrollador(Empleado):
    def __init__(self, nombre, apellido, salario_base, años_antigüedad, lenguaje_programación, horas_extras):
        super().__init__(nombre, apellido, salario_base, años_antigüedad)
        self.lenguaje_programación = lenguaje_programación
        self.horas_extras = horas_extras
    
    def calcular_salario(self):
        salario_base = super().calcular_salario()
        return salario_base + (self.horas_extras * 20)
    
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Lenguaje: {self.lenguaje_programación}, Horas Extras: {self.horas_extras}"

gerente1 = Gerente("Laura", "Martinez", 5000, 5, "TI", 1500)
gerente2 = Gerente("Pedro", "Gonzalez", 6000, 8, "Finanzas", 800)
desarrollador1 = Desarrollador("Carlos", "Sanchez", 3000, 3, "Python", 15)
desarrollador2 = Desarrollador("Ana", "Rodriguez", 3500, 4, "Java", 8)

print("--- Salarios de empleados ---")
print(f"{gerente1.nombre}: ${gerente1.calcular_salario():.2f}")
print(f"{gerente2.nombre}: ${gerente2.calcular_salario():.2f}")
print(f"{desarrollador1.nombre}: ${desarrollador1.calcular_salario():.2f}")
print(f"{desarrollador2.nombre}: ${desarrollador2.calcular_salario():.2f}")

print("\n--- Gerentes con bono > 1000 ---")
gerentes = [gerente1, gerente2]
for gerente in gerentes:
    if gerente.bono_gerencial > 1000:
        print(gerente.mostrar_info())

print("\n--- Desarrolladores con más de 10 horas extras ---")
desarrolladores = [desarrollador1, desarrollador2]
for desarrollador in desarrolladores:
    if desarrollador.horas_extras > 10:
        print(desarrollador.mostrar_info())