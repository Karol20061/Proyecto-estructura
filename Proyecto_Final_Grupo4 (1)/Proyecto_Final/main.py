"""
Sistema de Gestión de Citas Médicas
Proyecto Final 
Grupo 4

Integrantes 
  - Karolina Sayay: Análisis, clases (Paciente, Medico, Cita) y registro, Menú principal, consultas y búsquedas
  - Fernando Vasco: Modificación, eliminación y manejo de archivos, Interfaz HTML, documentación y presentación

Archivo: main.py
Contenido: Punto de entrada del programa y menú principal del sistema
"""

from modulos import gestor_pacientes as pac
from modulos import gestor_medicos as med
from modulos import gestor_citas as citas


# ===================================
# Menú principal y menús secundarios
# ===================================

def menu_pacientes():
    """Submenú para la gestión de pacientes."""
    while True:
        print("\n===== GESTIÓN DE PACIENTES =====")
        print("1. Registrar paciente")
        print("2. Consultar pacientes")
        print("3. Buscar paciente")
        print("4. Modificar paciente")
        print("5. Eliminar paciente")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()
        

        if opcion == "1":
            pac.registrar_paciente()          
        elif opcion == "2":
            pac.consultar_pacientes()         
        elif opcion == "3":
            pac.buscar_pacientes()           
        elif opcion == "4":
            pac.modificar_paciente()          
        elif opcion == "5":
            pac.eliminar_paciente()          
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def menu_medicos():
    """Submenú para la gestión de médicos."""
    while True:
        print("\n===== GESTIÓN DE MÉDICOS =====")
        print("1. Registrar médico")
        print("2. Consultar médicos")
        print("3. Eliminar médico")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            med.registrar_medico()            
        elif opcion == "2":
            med.consultar_medicos()           
        elif opcion == "3":
            med.eliminar_medico()             
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def menu_citas():
    """Submenú para la gestión de citas médicas."""
    while True:
        print("\n===== GESTIÓN DE CITAS =====")
        print("1. Registrar cita")
        print("2. Consultar citas")
        print("3. Buscar cita")
        print("4. Modificar cita")
        print("5. Eliminar cita")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            citas.registrar_cita()           
        elif opcion == "2":
            citas.consultar_citas()           
        elif opcion == "3":
            citas.buscar_citas()              
        elif opcion == "4":
            citas.modificar_cita()            
        elif opcion == "5":
            citas.eliminar_cita()             
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def menu_principal():
    """Menú principal del Sistema de Gestión de Citas Médicas."""
    while True:
        print("\n" + "=" * 50)
        print("   SISTEMA DE GESTIÓN DE CITAS MÉDICAS")
        print("=" * 50)
        print("1. Gestión de pacientes")
        print("2. Gestión de médicos")
        print("3. Gestión de citas")
        print("0. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if not opcion.isdigit():
            print("Error: Solo se permiten números enteros. Intente de nuevo.")
            continue

        if opcion == "1":
            menu_pacientes()
        elif opcion == "2":
            menu_medicos()
        elif opcion == "3":
            menu_citas()
        elif opcion == "0":
            print("\nGracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu_principal()
