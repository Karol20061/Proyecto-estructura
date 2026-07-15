"""
=====================================================================
Archivo: modulos/gestor_citas.py
Contenido: Registro, consulta, búsqueda, modificación y eliminación
             de citas médicas. Es el módulo central del sistema, ya
             que relaciona a Paciente y Medico a través de la clase Cita.
=====================================================================
"""

from clases.cita import Cita
from modulos import gestor_archivos as archivos
from modulos import gestor_pacientes as pac
from modulos import gestor_medicos as med
from modulos import validaciones as val

ARCHIVO_CITAS = "citas.json"


def cargar_citas():
    """Carga la lista de citas desde el archivo y la convierte en objetos."""
    datos = archivos.cargar_datos(ARCHIVO_CITAS)
    return [Cita.from_dict(d) for d in datos]


def guardar_citas(lista_citas):
    """Guarda la lista de objetos Cita en el archivo JSON."""
    datos = [c.to_dict() for c in lista_citas]
    return archivos.guardar_datos(ARCHIVO_CITAS, datos)


def _generar_id_cita(lista_citas):
    """Genera un identificador incremental simple para una nueva cita."""
    if not lista_citas:
        return "C001"
    numeros = [int(c.id_cita[1:]) for c in lista_citas if c.id_cita[1:].isdigit()]
    siguiente = max(numeros, default=0) + 1
    return f"C{siguiente:03d}"


# =======================================
#  Análisis, clases y registro de citas
# =======================================

def registrar_cita():
    """
    --- KAROLINA SAYAY: registro de citas ---
    Solicita los datos de una nueva cita, valida que el paciente y el
    médico existan, y guarda la relación entre ambos en una nueva Cita.
    """
    print("\n--- REGISTRO DE CITA ---")
    pacientes = pac.cargar_pacientes()
    medicos = med.cargar_medicos()
    citas = cargar_citas()

    if not pacientes:
        print("No hay pacientes registrados. Registre un paciente primero.")
        return
    if not medicos:
        print(" No hay médicos registrados. Registre un médico primero.")
        return

    cedula = input("Cédula del paciente: ").strip()
    paciente = pac.buscar_paciente_por_cedula(pacientes, cedula)
    if not paciente:
        print("No existe un paciente con esa cédula.")
        return

    id_medico = input("ID del médico: ").strip()
    medico = med.buscar_medico_por_id(medicos, id_medico)
    if not medico:
        print("No existe un médico con ese ID.")
        return

    fecha = val.pedir_dato(
        "Fecha de la cita (AAAA-MM-DD): ", val.validar_fecha,
        "Formato de fecha inválido. Use AAAA-MM-DD."
    )
    hora = val.pedir_dato(
        "Hora de la cita (HH:MM): ", val.validar_hora,
        "Formato de hora inválido. Use HH:MM."
    )
    motivo = val.pedir_dato(
        "Motivo de la consulta: ", val.validar_texto_no_vacio,
        "El motivo no puede estar vacío."
    )

    nueva_cita = Cita(_generar_id_cita(citas), paciente.cedula, medico.id_medico,
                       fecha, hora, motivo, "Pendiente")
    citas.append(nueva_cita)

    if guardar_citas(citas):
        print(f" Cita registrada correctamente con ID {nueva_cita.id_cita}.")
    else:
        print(" No se pudo guardar la cita.")


# ========================
#  Consultas y búsquedas
# ========================

def _describir_cita(cita, pacientes, medicos):
    """Función de apoyo que arma una descripción legible de una cita,
    mostrando el nombre del paciente y del médico en lugar de solo sus IDs."""
    paciente = pac.buscar_paciente_por_cedula(pacientes, cita.cedula_paciente)
    medico = med.buscar_medico_por_id(medicos, cita.id_medico)
    nombre_paciente = paciente.nombre if paciente else "Desconocido"
    nombre_medico = medico.nombre if medico else "Desconocido"
    return (f"ID: {cita.id_cita} | Paciente: {nombre_paciente} | "
            f"Médico: {nombre_medico} | Fecha: {cita.fecha} {cita.hora} | "
            f"Motivo: {cita.motivo} | Estado: {cita.estado}")


def consultar_citas():
    """Muestra en pantalla todas las citas registradas."""
    citas = cargar_citas()
    pacientes = pac.cargar_pacientes()
    medicos = med.cargar_medicos()

    print("\n--- LISTADO DE CITAS ---")
    if not citas:
        print("No hay citas registradas.")
        return
    for cita in citas:
        print(_describir_cita(cita, pacientes, medicos))


def buscar_citas():
    """Busca citas por fecha o por nombre del médico."""
    citas = cargar_citas()
    pacientes = pac.cargar_pacientes()
    medicos = med.cargar_medicos()

    print("\n--- BUSCAR CITA ---")
    print("1. Buscar por fecha")
    print("2. Buscar por médico")
    print("3. Buscar por cédula de paciente")
    opcion = input("Seleccione una opción: ").strip()

    encontradas = []
    if opcion == "1":
        fecha = input("Ingrese la fecha (AAAA-MM-DD): ").strip()
        encontradas = [c for c in citas if c.fecha == fecha]
    elif opcion == "2":
        nombre = input("Ingrese el nombre del médico (o parte de él): ").strip().lower()
        ids_medicos = [m.id_medico for m in medicos if nombre in m.nombre.lower()]
        encontradas = [c for c in citas if c.id_medico in ids_medicos]
    elif opcion == "3":
        cedula = input("Ingrese la cédula del paciente: ").strip()
        encontradas = [c for c in citas if c.cedula_paciente == cedula]
    else:
        print("⚠ Opción no válida.")
        return

    if not encontradas:
        print("No se encontraron coincidencias.")
    else:
        for cita in encontradas:
            print(_describir_cita(cita, pacientes, medicos))


# =====================================================================
# FERNANDO VASCO - Modificación, eliminación y archivos
# =====================================================================

def modificar_cita():
    """Modifica los datos de una cita existente (fecha, hora, motivo o estado)."""
    citas = cargar_citas()
    print("\n--- MODIFICAR CITA ---")
    id_cita = input("Ingrese el ID de la cita a modificar: ").strip()
    cita = next((c for c in citas if c.id_cita == id_cita), None)

    if not cita:
        print("No se encontró una cita con ese ID.")
        return

    print(f"Datos actuales -> {cita}")
    print("Deje el campo vacío si no desea modificarlo.")

    fecha = input(f"Nueva fecha (AAAA-MM-DD) [{cita.fecha}]: ").strip()
    hora = input(f"Nueva hora (HH:MM) [{cita.hora}]: ").strip()
    motivo = input(f"Nuevo motivo [{cita.motivo}]: ").strip()
    estado = input(f"Nuevo estado (Pendiente/Atendida/Cancelada) [{cita.estado}]: ").strip()

    if fecha and val.validar_fecha(fecha):
        cita.fecha = fecha
    if hora and val.validar_hora(hora):
        cita.hora = hora
    if motivo and val.validar_texto_no_vacio(motivo):
        cita.motivo = motivo
    if estado and estado.capitalize() in ("Pendiente", "Atendida", "Cancelada"):
        cita.estado = estado.capitalize()

    if guardar_citas(citas):
        print(" Cita modificada correctamente.")
    else:
        print("No se pudo guardar el cambio.")


def eliminar_cita():
    """Elimina una cita del sistema, identificada por su ID."""
    citas = cargar_citas()
    print("\n--- ELIMINAR CITA ---")
    id_cita = input("Ingrese el ID de la cita a eliminar: ").strip()
    cita = next((c for c in citas if c.id_cita == id_cita), None)

    if not cita:
        print("⚠ No se encontró una cita con ese ID.")
        return

    confirmacion = input(f"¿Confirma eliminar la cita {cita.id_cita}? (S/N): ").strip().lower()
    if confirmacion == "s":
        citas.remove(cita)
        if guardar_citas(citas):
            print(" Cita eliminada correctamente.")
        else:
            print(" No se pudo guardar el cambio.")
    else:
        print("Operación cancelada.")
