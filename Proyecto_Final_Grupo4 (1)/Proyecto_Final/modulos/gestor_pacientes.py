"""
=====================================================================
KAROLINA SAYAY - Análisis, clases y registro de citas
Archivo: modulos/gestor_pacientes.py
Contenido: Registro de pacientes + operaciones de apoyo (consulta interna,
             modificación y eliminación, reutilizadas por otros integrantes)
=====================================================================
"""

from clases.paciente import Paciente
from modulos import gestor_archivos as archivos
from modulos import validaciones as val

ARCHIVO_PACIENTES = "pacientes.json"


def cargar_pacientes():
    """Carga la lista de pacientes desde el archivo y la convierte en objetos."""
    datos = archivos.cargar_datos(ARCHIVO_PACIENTES)
    return [Paciente.from_dict(d) for d in datos]


def guardar_pacientes(lista_pacientes):
    """Guarda la lista de objetos Paciente en el archivo JSON."""
    datos = [p.to_dict() for p in lista_pacientes]
    return archivos.guardar_datos(ARCHIVO_PACIENTES, datos)


def buscar_paciente_por_cedula(lista_pacientes, cedula):
    """Devuelve el objeto Paciente que coincide con la cédula, o None."""
    for paciente in lista_pacientes:
        if paciente.cedula == cedula:
            return paciente
    return None


def registrar_paciente():
    """
    --- KAROLINA SAYAY: registro de pacientes ---
    Solicita los datos de un nuevo paciente, los valida y los guarda.
    """
    print("\n--- REGISTRO DE PACIENTE ---")
    pacientes = cargar_pacientes()

    cedula = val.pedir_dato(
        "Cédula (10 dígitos): ", val.validar_cedula,
        "La cédula debe tener 10 dígitos numéricos."
    )

    if buscar_paciente_por_cedula(pacientes, cedula):
        print("⚠ Ya existe un paciente registrado con esa cédula.")
        return

    nombre = val.pedir_dato(
        "Nombre completo: ", val.validar_texto_no_vacio,
        "El nombre no puede estar vacío."
    )
    edad = val.pedir_dato(
        "Edad: ", val.validar_entero_positivo,
        "La edad debe ser un número entero positivo."
    )
    telefono = val.pedir_dato(
        "Teléfono (7 a 10 dígitos): ", val.validar_telefono,
        "El teléfono debe tener entre 7 y 10 dígitos numéricos."
    )
    direccion = val.pedir_dato(
        "Dirección: ", val.validar_texto_no_vacio,
        "La dirección no puede estar vacía."
    )

    nuevo_paciente = Paciente(cedula, nombre, int(edad), telefono, direccion)
    pacientes.append(nuevo_paciente)

    if guardar_pacientes(pacientes):
        print("Paciente registrado correctamente.")
    else:
        print(" No se pudo guardar el paciente.")


# ==================================
# Consultas y búsquedas
# ==================================

def consultar_pacientes():
    """Muestra en pantalla todos los pacientes registrados."""
    pacientes = cargar_pacientes()
    print("\n--- LISTADO DE PACIENTES ---")
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    for paciente in pacientes:
        print(paciente)


def buscar_pacientes():
    """Busca pacientes por cédula o por nombre (coincidencia parcial)."""
    pacientes = cargar_pacientes()
    print("\n--- BUSCAR PACIENTE ---")
    print("1. Buscar por cédula")
    print("2. Buscar por nombre")
    opcion = input("Seleccione una opción: ").strip()

    encontrados = []
    if opcion == "1":
        cedula = input("Ingrese la cédula: ").strip()
        paciente = buscar_paciente_por_cedula(pacientes, cedula)
        if paciente:
            encontrados.append(paciente)
    elif opcion == "2":
        nombre = input("Ingrese el nombre (o parte de él): ").strip().lower()
        encontrados = [p for p in pacientes if nombre in p.nombre.lower()]
    else:
        print("⚠ Opción no válida.")
        return

    if not encontrados:
        print("No se encontraron coincidencias.")
    else:
        for paciente in encontrados:
            print(paciente)


# ======================================================
# FERNANDO VASCO - Modificación, eliminación y archivos
# =====================================================

def modificar_paciente():
    """Modifica los datos de un paciente existente, identificado por cédula."""
    pacientes = cargar_pacientes()
    print("\n--- MODIFICAR PACIENTE ---")
    cedula = input("Ingrese la cédula del paciente a modificar: ").strip()
    paciente = buscar_paciente_por_cedula(pacientes, cedula)

    if not paciente:
        print("⚠ No se encontró un paciente con esa cédula.")
        return

    print(f"Datos actuales -> {paciente}")
    print("Deje el campo vacío si no desea modificarlo.")

    nombre = input(f"Nuevo nombre [{paciente.nombre}]: ").strip()
    edad = input(f"Nueva edad [{paciente.edad}]: ").strip()
    telefono = input(f"Nuevo teléfono [{paciente.telefono}]: ").strip()
    direccion = input(f"Nueva dirección [{paciente.direccion}]: ").strip()

    if nombre and val.validar_texto_no_vacio(nombre):
        paciente.nombre = nombre
    if edad and val.validar_entero_positivo(edad):
        paciente.edad = int(edad)
    if telefono and val.validar_telefono(telefono):
        paciente.telefono = telefono
    if direccion and val.validar_texto_no_vacio(direccion):
        paciente.direccion = direccion

    if guardar_pacientes(pacientes):
        print(" Paciente modificado correctamente.")
    else:
        print(" No se pudo guardar el cambio.")


def eliminar_paciente():
    """Elimina un paciente del sistema, identificado por cédula."""
    pacientes = cargar_pacientes()
    print("\n--- ELIMINAR PACIENTE ---")
    cedula = input("Ingrese la cédula del paciente a eliminar: ").strip()
    paciente = buscar_paciente_por_cedula(pacientes, cedula)

    if not paciente:
        print(" No se encontró un paciente con esa cédula.")
        return

    confirmacion = input(f"¿Confirma eliminar a {paciente.nombre}? (S/N): ").strip().lower()
    if confirmacion == "s":
        pacientes.remove(paciente)
        if guardar_pacientes(pacientes):
            print("Paciente eliminado correctamente.")
        else:
            print("No se pudo guardar el cambio.")
    else:
        print("Operación cancelada.")
