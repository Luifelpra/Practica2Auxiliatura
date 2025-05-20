//1.Sean las siguientes clases:Habitación<nombre, tamaño (en metros cuadrados)
//Métodos: mostrar_info() (muestra el nombre y tamaño de la habitación)
//Casa<dirección, habitaciones (lista de objetos de tipo Habitación) Métodos: agregar_habitacion(habitacion), mostrar_casa() (muestra la dirección y la información de todas las habitaciones)
//  a)Implementa las clases con sus constructores, getters y setters.
//  b)Crea una casa y agrega varias habitaciones.
//  c)Muestra la información de la casa y sus habitaciones.
import java.util.ArrayList;
public class Habitacion {
    private String nombre;
    private double tamano;

    public Habitacion(String nombre, double tamano) {
        this.nombre = nombre;
        this.tamano = tamano;
    }

    public void mostrarInfo() {
        System.out.println("Habitación: " + nombre + ", Tamaño: " + tamano + " m2");
    }
}

class Casa {
    private String direccion;
    private ArrayList<Habitacion> habitaciones;

    public Casa(String direccion) {
        this.direccion = direccion;
        this.habitaciones = new ArrayList<>();
    }

    public void agregarHabitacion(Habitacion habitacion) {
        habitaciones.add(habitacion);
    }

    public void mostrarCasa() {
        System.out.println("Dirección: " + direccion);
        for (Habitacion h : habitaciones) {
            h.mostrarInfo();
        }
    }

    public static void main(String[] args) {
        Casa casa = new Casa("Av. Siempre Viva 742");
        casa.agregarHabitacion(new Habitacion("Sala", 20));
        casa.agregarHabitacion(new Habitacion("Cocina", 12));
        casa.mostrarCasa();
    }
}
