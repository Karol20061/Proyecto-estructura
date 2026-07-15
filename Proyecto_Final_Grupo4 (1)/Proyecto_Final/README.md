# Sistema de Gestión de Citas Médicas — Grupo 4

Proyecto Final de la asignatura **Estructura de Datos** (UNEMI).

## Descripción

Aplicación de consola en Python que permite administrar pacientes, médicos y
citas médicas de un consultorio: registro, consulta, búsqueda, modificación,
eliminación y persistencia en archivos JSON. Incluye una interfaz de apoyo en
HTML (`html/index.html`) para la exposición del proyecto.

## Estructura del proyecto

```
Proyecto_Final/
├── main.py                  # Punto de entrada y menú principal
├── clases/
│   ├── paciente.py          # Clase Paciente
│   ├── medico.py            # Clase Medico
│   └── cita.py              # Clase Cita (relaciona Paciente y Medico)
├── modulos/
│   ├── validaciones.py      # Validación de datos ingresados
│   ├── gestor_archivos.py   # Lectura/escritura de archivos JSON
│   ├── gestor_pacientes.py  # CRUD de pacientes
│   ├── gestor_medicos.py    # CRUD de médicos
│   └── gestor_citas.py      # CRUD de citas
├── datos/                   # Archivos JSON con la información persistida
│   ├── pacientes.json
│   ├── medicos.json
│   └── citas.json
├── html/
│   ├── index.html           # Interfaz de presentación del proyecto
│   ├── css/estilos.css
│   └── imagenes/            # Capturas de pantalla del sistema
├── README.md
└── Manual_Usuario.md
```

## Cómo ejecutar

Requiere Python 3.8.

```bash
cd Proyecto_Final
python3 main.py
```

## División del trabajo por integrante

Cada archivo de código incluye comentarios que identifican qué integrante
desarrolló cada sección, según la siguiente distribución:

| Integrante | Responsabilidad |
|---|---|
| **Karolina Sayay** | Análisis, clases (`Paciente`, `Medico`, `Cita`) y registro de pacientes/médicos/citas ,  Menú principal, menús secundarios, consultas y búsquedas  |
| **Fernando Vasco** | Modificación, eliminación y manejo de archivos (persistencia), Interfaz HTML, documentación (README, Manual de Usuario) y presentación | |

## Contenidos aplicados

Variables y tipos de datos, entrada/salida, operadores, condicionales, ciclos,
funciones, listas, manejo de cadenas, programación orientada a objetos (clases,
objetos, métodos, atributos), organización en módulos, y lectura/escritura de
archivos para persistencia — conforme a los requisitos de la Guía de Práctica
N.º 4 de Estructura de Datos.
