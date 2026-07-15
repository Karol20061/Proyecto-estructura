# Manual de Usuario — Sistema de Gestión de Citas Médicas

## 1. Requisitos

- Python 3.8 o superior instalado.
- No requiere instalar librerías adicionales.

## 2. Ejecución

Desde la carpeta `Proyecto_Final`, ejecutar:

```bash
python3 main.py
```

Se mostrará el **menú principal**:

```
==========================================
   SISTEMA DE GESTIÓN DE CITAS MÉDICAS 
==========================================
1. Gestión de pacientes
2. Gestión de médicos
3. Gestión de citas
0. Salir
```

## 3. Orden recomendado de uso

1. **Gestión de médicos → Registrar médico**: registre al menos un médico
   antes de agendar citas.
2. **Gestión de pacientes → Registrar paciente**: registre al menos un
   paciente.
3. **Gestión de citas → Registrar cita**: ingrese la cédula del paciente y el
   ID del médico previamente registrados, junto con fecha, hora y motivo.

## 4. Gestión de pacientes

| Opción | Acción |
|---|---|
| 1 | Registrar un nuevo paciente (cédula, nombre, edad, teléfono, dirección) |
| 2 | Consultar el listado completo de pacientes |
| 3 | Buscar un paciente por cédula o por nombre |
| 4 | Modificar los datos de un paciente existente |
| 5 | Eliminar un paciente (con confirmación) |

## 5. Gestión de médicos

| Opción | Acción |
|---|---|
| 1 | Registrar un nuevo médico (ID, nombre, especialidad, horario) |
| 2 | Consultar el listado completo de médicos |
| 3 | Eliminar un médico (con confirmación) |

## 6. Gestión de citas

| Opción | Acción |
|---|---|
| 1 | Registrar una nueva cita (paciente + médico + fecha + hora + motivo) |
| 2 | Consultar el listado completo de citas |
| 3 | Buscar citas por fecha, por médico o por cédula del paciente |
| 4 | Modificar fecha, hora, motivo o estado de una cita |
| 5 | Eliminar una cita (con confirmación) |

## 7. Formatos de datos esperados

- **Cédula**: 10 dígitos numéricos.
- **Teléfono**: entre 7 y 10 dígitos numéricos.
- **Fecha**: `AAAA-MM-DD` (ejemplo: `2026-08-10`).
- **Hora**: `HH:MM` en formato 24 horas (ejemplo: `09:30`).
- **Estado de la cita**: `Pendiente`, `Atendida` o `Cancelada`.

## 8. Persistencia de la información

Toda la información se guarda automáticamente en la carpeta `datos/` en
formato JSON (`pacientes.json`, `medicos.json`, `citas.json`). No es
necesario guardar manualmente: cada registro, modificación o eliminación
actualiza el archivo correspondiente de inmediato. Al volver a abrir el
programa, la información se carga automáticamente.

## 9. Salir del sistema

Seleccione la opción `0` en el menú principal para cerrar la aplicación de
forma segura.
