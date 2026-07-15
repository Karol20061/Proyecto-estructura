"""
=====================================================================
KAROLINA SAYAY - Análisis, clases y registro de citas
Archivo: clases/paciente.py
Contenido: Definición de la clase Paciente
=====================================================================
"""


class Paciente:
    """
    Representa a un paciente del sistema de citas médicas.

    Atributos:
        cedula (str): identificador único del paciente.
        nombre (str): nombre completo del paciente.
        edad (int): edad del paciente.
        telefono (str): número de contacto.
        direccion (str): dirección de residencia.
    """

    def __init__(self, cedula, nombre, edad, telefono, direccion):
        # --- KAROLINA SAYAY: atributos de la clase Paciente ---
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion

    def to_dict(self):
        """Convierte el objeto Paciente en un diccionario (para guardar en archivo)."""
        # --- KAROLINA SAYAY: soporte para persistencia de datos ---
        return {
            "cedula": self.cedula,
            "nombre": self.nombre,
            "edad": self.edad,
            "telefono": self.telefono,
            "direccion": self.direccion
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Paciente a partir de un diccionario leído desde archivo."""
        return Paciente(
            data["cedula"],
            data["nombre"],
            data["edad"],
            data["telefono"],
            data["direccion"]
        )

    def __str__(self):
        return (f"Cédula: {self.cedula} | Nombre: {self.nombre} | "
                f"Edad: {self.edad} | Teléfono: {self.telefono} | "
                f"Dirección: {self.direccion}")
