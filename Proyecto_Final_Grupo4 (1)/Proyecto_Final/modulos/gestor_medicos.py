"""
=====================================================================
KAROLINA SAYAY - Análisis, clases y registro de citas
Archivo: modulos/gestor_medicos.py
Contenido: Registro de médicos (catálogo base necesario para agendar citas)
=====================================================================
"""

from clases.medico import Medico
from modulos import gestor_archivos as archivos
from modulos import validaciones as val

ARCHIVO_MEDICOS = "medicos.json"


def cargar_medicos():
    """Carga la lista de médicos desde el archivo y la convierte en objetos."""
    datos = archivos.cargar_datos(ARCHIVO_MEDICOS)
    return [Medico.from_dict(d) for d in datos]


def guardar_medicos(lista_medicos):
    """Guarda la lista de objetos Medico en el archivo JSON."""
    datos = [m.to_dict() for m in lista_medicos]
    return archivos.guardar_datos(ARCHIVO_MEDICOS, datos)


def buscar_medico_por_id(lista_medicos, id_medico):
    """Devuelve el objeto Medico que coincide con el id, o None."""
    for medico in lista_medicos:
        if medico.id_medico == id_medico:
            return medico
    return None


def registrar_medico():
    """
    --- KAROLINA SAYAY: registro de médicos ---
    Solicita los datos de un nuevo médico, los valida y los guarda.
    """
    print("\n--- REGISTRO DE MÉDICO ---")
    medicos = cargar_medicos()

    id_medico = val.pedir_dato(
        "ID del médico (ej. M001): ", val.validar_texto_no_vacio,
        "El ID no puede estar vacío."
    )

    if buscar_medico_por_id(medicos, id_medico):
        print("Ya existe un médico registrado con ese ID.")
        return

    nombre = val.pedir_dato(
        "Nombre completo: ", val.validar_texto_no_vacio,
        "El nombre no puede estar vacío."
    )
    especialidad = val.pedir_dato(
        "Especialidad: ", val.validar_texto_no_vacio,
        "La especialidad no puede estar vacía."
    )
    horario = val.pedir_dato(
        "Horario de atención (ej. 08:00-14:00): ", val.validar_texto_no_vacio,
        "El horario no puede estar vacío."
    )

    nuevo_medico = Medico(id_medico, nombre, especialidad, horario)
    medicos.append(nuevo_medico)

    if guardar_medicos(medicos):
        print("Médico registrado correctamente.")
    else:
        print(" No se pudo guardar el médico.")


# =====================================================================
# EDDY BAQUE - Consultas y búsquedas
# =====================================================================

def consultar_medicos():
    """Muestra en pantalla todos los médicos registrados."""
    medicos = cargar_medicos()
    print("\n--- LISTADO DE MÉDICOS ---")
    if not medicos:
        print("No hay médicos registrados.")
        return
    for medico in medicos:
        print(medico)


# =====================================================================
# FERNANDO VASCO - Modificación, eliminación y archivos
# =====================================================================

def eliminar_medico():
    """Elimina un médico del sistema, identificado por ID."""
    medicos = cargar_medicos()
    print("\n--- ELIMINAR MÉDICO ---")
    id_medico = input("Ingrese el ID del médico a eliminar: ").strip()
    medico = buscar_medico_por_id(medicos, id_medico)

    if not medico:
        print(" No se encontró un médico con ese ID.")
        return

    confirmacion = input(f"¿Confirma eliminar a {medico.nombre}? (S/N): ").strip().lower()
    if confirmacion == "s":
        medicos.remove(medico)
        if guardar_medicos(medicos):
            print(" Médico eliminado correctamente.")
        else:
            print("No se pudo guardar el cambio.")
    else:
        print("Operación cancelada.")
