"""
=====================================================================
KAROLINA SAYAY - Análisis, clases y registro de citas
Archivo: clases/cita.py
Contenido: Definición de la clase Cita (relaciona Paciente y Medico)
=====================================================================
"""


class Cita:
    """
    Representa una cita médica del sistema.

    La clase Cita se relaciona con Paciente (por cédula) y con Medico
    (por id_medico), cumpliendo el requisito de "mínimo dos clases
    relacionadas" que exige la guía de práctica.

    Atributos:
        id_cita (str): identificador único de la cita.
        cedula_paciente (str): cédula del paciente asociado.
        id_medico (str): identificador del médico asociado.
        fecha (str): fecha de la cita (formato AAAA-MM-DD).
        hora (str): hora de la cita (formato HH:MM).
        motivo (str): motivo de la consulta.
        estado (str): estado de la cita ("Pendiente", "Atendida", "Cancelada").
    """

    def __init__(self, id_cita, cedula_paciente, id_medico, fecha, hora,
                 motivo, estado="Pendiente"):
        # --- KAROLINA SAYAY: atributos de la clase Cita ---
        self.id_cita = id_cita
        self.cedula_paciente = cedula_paciente
        self.id_medico = id_medico
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = estado

    def to_dict(self):
        """Convierte el objeto Cita en un diccionario (para guardar en archivo)."""
        # --- KAROLINA SAYAY: soporte para persistencia de datos ---
        return {
            "id_cita": self.id_cita,
            "cedula_paciente": self.cedula_paciente,
            "id_medico": self.id_medico,
            "fecha": self.fecha,
            "hora": self.hora,
            "motivo": self.motivo,
            "estado": self.estado
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Cita a partir de un diccionario leído desde archivo."""
        return Cita(
            data["id_cita"],
            data["cedula_paciente"],
            data["id_medico"],
            data["fecha"],
            data["hora"],
            data["motivo"],
            data.get("estado", "Pendiente")
        )

    def __str__(self):
        return (f"ID Cita: {self.id_cita} | Paciente(cédula): {self.cedula_paciente} | "
                f"Médico(id): {self.id_medico} | Fecha: {self.fecha} | "
                f"Hora: {self.hora} | Motivo: {self.motivo} | Estado: {self.estado}")
