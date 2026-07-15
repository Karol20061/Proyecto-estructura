"""
=====================================================================
KAROLINA SAYAY - Análisis, clases y registro de citas
Archivo: clases/medico.py
Contenido: Definición de la clase Medico
=====================================================================
"""


class Medico:
    """
    Representa a un médico del sistema de citas médicas.

    Atributos:
        id_medico (str): identificador único del médico.
        nombre (str): nombre completo del médico.
        especialidad (str): especialidad médica.
        horario (str): horario de atención (ej. "08:00 - 14:00").
    """

    def __init__(self, id_medico, nombre, especialidad, horario):
        # --- KAROLINA SAYAY: atributos de la clase Medico ---
        self.id_medico = id_medico
        self.nombre = nombre
        self.especialidad = especialidad
        self.horario = horario

    def to_dict(self):
        """Convierte el objeto Medico en un diccionario (para guardar en archivo)."""
        # --- KAROLINA SAYAY: soporte para persistencia de datos ---
        return {
            "id_medico": self.id_medico,
            "nombre": self.nombre,
            "especialidad": self.especialidad,
            "horario": self.horario
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Medico a partir de un diccionario leído desde archivo."""
        return Medico(
            data["id_medico"],
            data["nombre"],
            data["especialidad"],
            data["horario"]
        )

    def __str__(self):
        return (f"ID: {self.id_medico} | Nombre: {self.nombre} | "
                f"Especialidad: {self.especialidad} | Horario: {self.horario}")
