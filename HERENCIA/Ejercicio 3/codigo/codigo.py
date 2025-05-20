#3.Definir las clases:
# Persona <ci, nombre, apellido, celular, fecha_Nac>Estudiante (heredado de persona) <ru, fecha_Ingreso, semestre> Docente (heredado de persona) <nit, profesión, especialidad>
#   a)Diseñar el diagrama UML de las clases anteriores.
#   b)Implementa las clases con sus constructores, datos por defecto y mostrar.
#   c)Mostrar los estudiantes mayores de 25 años.
#   d)Mostrar al docente que tiene la profesión de “Ingeniero”, es del sexo masculino y es el mayor de todos.
#   e)Mostrar a los estudiantes y docentes que tienen el mismo apellido
from datetime import datetime

class Persona:
    def __init__(self, ci, nombre, apellido, celular, fecha_nac):
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.fecha_nac = fecha_nac
    
    def mostrar(self):
        return f"CI: {self.ci}, Nombre: {self.nombre} {self.apellido}, Celular: {self.celular}, Fecha Nacimiento: {self.fecha_nac}"
    
    def calcular_edad(self):
        hoy = datetime.now().date()
        nacimiento = datetime.strptime(self.fecha_nac, "%Y-%m-%d").date()
        edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
        return edad

class Estudiante(Persona):
    def __init__(self, ci, nombre, apellido, celular, fecha_nac, ru, fecha_ingreso, semestre):
        super().__init__(ci, nombre, apellido, celular, fecha_nac)
        self.ru = ru
        self.fecha_ingreso = fecha_ingreso
        self.semestre = semestre
    
    def mostrar(self):
        info_base = super().mostrar()
        return f"{info_base}, RU: {self.ru}, Fecha Ingreso: {self.fecha_ingreso}, Semestre: {self.semestre}"

class Docente(Persona):
    def __init__(self, ci, nombre, apellido, celular, fecha_nac, nit, profesion, especialidad):
        super().__init__(ci, nombre, apellido, celular, fecha_nac)
        self.nit = nit
        self.profesion = profesion
        self.especialidad = especialidad
    
    def mostrar(self):
        info_base = super().mostrar()
        return f"{info_base}, NIT: {self.nit}, Profesión: {self.profesion}, Especialidad: {self.especialidad}"
estudiante1 = Estudiante("1234567", "Juan", "Perez", "77712345", "1995-05-15", "200000001", "2020-01-15", 8)
estudiante2 = Estudiante("7654321", "Maria", "Gomez", "77754321", "2000-08-20", "200000002", "2021-01-15", 5)
docente1 = Docente("9876543", "Carlos", "Lopez", "77798765", "1980-03-10", "123456789", "Ingeniero", "Sistemas")
docente2 = Docente("4567890", "Ana", "Gomez", "77745678", "1975-11-25", "987654321", "Licenciada", "Informática")


print("Estudiantes mayores de 25 años ")
estudiantes = [estudiante1, estudiante2]
for estudiante in estudiantes:
    if estudiante.calcular_edad() > 25:
        print(estudiante.mostrar())


print("\nDocente Ingeniero masculino mayor")
docentes = [docente1, docente2]
docente_mayor = None
max_edad = 0

for docente in docentes:
    edad = docente.calcular_edad()
    if docente.profesion == "Ingeniero" and edad > max_edad:
        max_edad = edad
        docente_mayor = docente

if docente_mayor:
    print(docente_mayor.mostrar())

print("\n Personas con mismo apellido")
apellidos = {}
personas = estudiantes + docentes

for persona in personas:
    if persona.apellido not in apellidos:
        apellidos[persona.apellido] = []
    apellidos[persona.apellido].append(persona)

for apellido, lista_personas in apellidos.items():
    if len(lista_personas) > 1:
        print(f"\nApellido: {apellido}")
        for persona in lista_personas:
            print(persona.mostrar())