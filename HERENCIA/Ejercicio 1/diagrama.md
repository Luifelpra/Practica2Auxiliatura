```mermaid
classDiagram
    class Vehiculo {
        -marca: String
        -modelo: String
        -año: int
        -precioBase: double
        +mostrarInfo(): void
    }

    class Coche {
        -numPuertas: int
        -tipoCombustible: String
        +mostrarInfo(): void
    }

    class Moto {
        -cilindrada: int
        -tipoMotor: String
        +mostrarInfo(): void
    }

    Vehiculo <|-- Coche
    Vehiculo <|-- Moto
