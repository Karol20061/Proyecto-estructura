"""
=====================================================================
FERNANDO VASCO - Modificación, eliminación y archivos
Archivo: modulos/gestor_archivos.py
Contenido: Funciones genéricas de lectura y escritura de archivos (JSON)
             utilizadas para dar persistencia a pacientes, médicos y citas.
=====================================================================
"""

import json
import os

CARPETA_DATOS = "datos"


def _ruta(nombre_archivo):
    """Construye la ruta completa dentro de la carpeta 'datos/'."""
    # --- FERNANDO VASCO: manejo de rutas de archivos ---
    if not os.path.exists(CARPETA_DATOS):
        os.makedirs(CARPETA_DATOS)
    return os.path.join(CARPETA_DATOS, nombre_archivo)


def guardar_datos(nombre_archivo, lista_diccionarios):
    """
    Escribe (persiste) una lista de diccionarios en un archivo JSON.
    Se usa después de cada registro, modificación o eliminación.
    """
    # --- FERNANDO VASCO: escritura de archivos / persistencia de datos ---
    try:
        with open(_ruta(nombre_archivo), "w", encoding="utf-8") as archivo:
            json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)
        return True
    except (IOError, OSError) as error:
        print(f" Error al guardar el archivo '{nombre_archivo}': {error}")
        return False


def cargar_datos(nombre_archivo):
    """
    Lee un archivo JSON y devuelve la lista de diccionarios almacenada.
    Si el archivo no existe o está vacío, devuelve una lista vacía.
    """
    # --- FERNANDO VASCO: lectura de archivos / persistencia de datos ---
    ruta = _ruta(nombre_archivo)
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
            if not contenido:
                return []
            return json.loads(contenido)
    except (IOError, OSError, json.JSONDecodeError) as error:
        print(f"Error al leer el archivo '{nombre_archivo}': {error}")
        return []
