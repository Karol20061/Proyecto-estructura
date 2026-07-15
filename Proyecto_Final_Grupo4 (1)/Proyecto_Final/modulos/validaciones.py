"""
=====================================================================
KAROLINA SAYAY - Análisis, clases y registro de citas
Archivo: modulos/validaciones.py
Contenido: Funciones de validación de datos ingresados por el usuario
=====================================================================
"""


def validar_texto_no_vacio(texto):
    """Valida que un texto no esté vacío ni contenga solo espacios."""
    return bool(texto and texto.strip())


def validar_cedula(cedula):
    """Valida que la cédula tenga exactamente 10 dígitos numéricos."""
    return cedula.isdigit() and len(cedula) == 10


def validar_entero_positivo(valor):
    """Valida que el valor ingresado sea un número entero positivo."""
    try:
        numero = int(valor)
        return numero > 0
    except ValueError:
        return False


def validar_telefono(telefono):
    """Valida que el teléfono tenga entre 7 y 10 dígitos numéricos."""
    return telefono.isdigit() and 7 <= len(telefono) <= 10


def validar_fecha(fecha):
    """Valida el formato de fecha AAAA-MM-DD usando datetime."""
    from datetime import datetime
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validar_hora(hora):
    """Valida el formato de hora HH:MM (24 horas)."""
    from datetime import datetime
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False


def pedir_dato(mensaje, funcion_validacion, mensaje_error):
    """
    Solicita un dato al usuario en un bucle hasta que sea válido.
    Reutilizada en los módulos de registro (Karolina Sayay) y
    modificación (Fernando Vasco) para mantener la validación centralizada.
    """
    while True:
        dato = input(mensaje).strip()
        if funcion_validacion(dato):
            return dato
        print(f"{mensaje_error}")
