//1. Modelar diferentes tipos de vehículos. Las clases deben tener las siguientes características:
//Vehículo<marca, modelo, año, precio_base>
//Métodos: mostrar_info() muestra la información básica del vehículo
//Coche (hereda de Vehículo)< num_puertas, tipo_combustible>
//Métodos: mostrar_info() debe mostrar la información básica más losatributos adicionales
//Moto (hereda de Vehículo)< cilindrada, tipo_motor>
//Métodos: mostrar_info() debe mostrar la información básica más losatributos adicionales
//  a) Implementa las clases con sus constructores, getters y setters.
//  b) Crea instancias de Coche y Moto y muestra su información usando elmétodo mostrar_info().
//  c) Muestra todos los coches que tienen más de 4 puertas.
//  d) Mostrar los coches y motos actuales (gestión 2025)
// Clase base Vehiculo
// Ejercicio 1 - HERENCIA
// Modelar Vehiculo, Coche y Moto con método mostrar_info() y filtros

class Vehiculo {
    protected String marca;
    protected String modelo;
    protected int año;
    protected double precioBase;

    public Vehiculo(String marca, String modelo, int año, double precioBase) {
        this.marca = marca;
        this.modelo = modelo;
        this.año = año;
        this.precioBase = precioBase;
    }

    public void mostrarInfo() {
        System.out.println("Marca: " + marca + ", Modelo: " + modelo + ", Año: " + año + ", Precio: " + precioBase);
    }

    public int getAño() {
        return año;
    }
}

class Coche extends Vehiculo {
    private int numPuertas;
    private String tipoCombustible;

    public Coche(String marca, String modelo, int año, double precioBase, int numPuertas, String tipoCombustible) {
        super(marca, modelo, año, precioBase);
        this.numPuertas = numPuertas;
        this.tipoCombustible = tipoCombustible;
    }

    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Puertas: " + numPuertas + ", Combustible: " + tipoCombustible);
    }

    public int getNumPuertas() {
        return numPuertas;
    }
}

class Moto extends Vehiculo {
    private int cilindrada;
    private String tipoMotor;

    public Moto(String marca, String modelo, int año, double precioBase, int cilindrada, String tipoMotor) {
        super(marca, modelo, año, precioBase);
        this.cilindrada = cilindrada;
        this.tipoMotor = tipoMotor;
    }

    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Cilindrada: " + cilindrada + "cc, Motor: " + tipoMotor);
    }
}

public class Main {
    public static void main(String[] args) {
        Coche c1 = new Coche("Toyota", "Corolla", 2025, 15000, 5, "Gasolina");
        Coche c2 = new Coche("Ford", "Focus", 2020, 13000, 3, "Diesel");
        Moto m1 = new Moto("Yamaha", "R3", 2025, 7000, 321, "2T");

        Vehiculo[] vehiculos = {c1, c2, m1};

        for (Vehiculo v : vehiculos) {
            if (v instanceof Coche coche && coche.getNumPuertas() > 4) {
                System.out.println("Coche con más de 4 puertas:");
                coche.mostrarInfo();
            }

            if (v.getAño() == 2025) {
                System.out.println("Vehículo de la gestión 2025:");
                v.mostrarInfo();
            }
        }
    }
}
