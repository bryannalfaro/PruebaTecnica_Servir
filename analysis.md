# Documento técnico para implementación de manejo de asistencia de empleados
### Fecha de elaboración: 30 de mayo de 2024
### Elaborado por: Bryann Alfaro

## Resumen
Se busca la implementación de una nueva funcionalidad dentro del sistema que pueda brindar el apoyo en el control de asistencia de los empleados los cuales se encontrarán en distintos centros de trabajo. Este control se basa en una planificación mensual y será verificada por medio de llamadas telefónicas diarias a los encargados de cada centro de trabajo. 

## Propósito

El propósito del documento es el poder facilitar la comprensión de la nueva implementación sobre asistencia de empleados dentro del sistema actual definiendo el diseño de cada componente y la forma en que se agregará a la aplicación.

## Alcance

Esta implementación incluye actualización en el diseño de base de datos actual agregando las entidades necesarias para el correcto funcionamiento del sistema. Además, la descripción de las pantallas que se necesitan desarrollar y los distintos procesos y suposiciones que esto conlleva.

## Audiencia

Dirigida a desarrolladores, project managers, testers, gerencia y clientes.

## Objetivos

1. Documentar la asistencia diaria de los empleados en los distintos centros de trabajo.
2. Proveer de información valiosa para utilizarse en la planificación mensual de los empleados.
3. Agilizar el control de asistencia en los distintos centros de trabajo. 

# Análisis y diseño

# Componentes

## Tablas

Para la correcta implementación de la nueva funcionalidad es necesario agregar las siguientes entidades:

### Entidad Centro de trabajo 
#### Nombre tabla: work_center

#### Propiedades

`id_center`: Identificador unico del centro de trabajo <br>
`name_center`: Nombre del centro de trabajo<br>
`location_center`: Ubicación del centro de trabajo<br>
`manager_center_id`: Identificador del encargado del centro<br>
`number_center`: Numero del centro de trabajo

### Entidad Asistencia 
#### Nombre tabla: attendance_employee

#### Propiedades

`id_attendance`: Identificador unico del registro de asistencia <br>
`creation_date`: Fecha de creacion del registro<br>
`state_attendance`: Presente / Ausente<br>
`manager_attendance_id`: Encargado del registro<br>
`employee_id`: Identificador del empleado<br>
`center_id`: Identificador del centro

## Pantallas
### Pantalla - Manejo de centro de trabajo
En esta pantalla se busca tener las distintas opciones para el manejo del centro de trabajo (Listar, crear, eliminar y editar) lo que implica la creación de las pantallas para estos controles. 

### Pantalla - Asistencia de empleado

En esta pantalla se llevara a cabo el registro de la asistencia de cada empleado utilizando el código del mismo y los datos necesarios.

### Pantalla - Visualización de asistencia
Listar la información de asistencia de un empleado para poder verificar su historial y récord. De igual forma tener una pantalla con la información de asistencia de manera general de empleados y centros a los que pertenece.




### Procesos

1. Al momento de realizar el registro de asistencia el encargado ingresa al sistema y tiene la opción de llenar los datos y enviar el formulario con la respectiva llamada.

2. El usuario ingresa al área de visualización de asistencia y puede comprobar la información de un empleado en específico y verificar su desarrollo. Además se podría implementar otras características en un nuevo diseño como filtro por centro de trabajo para tener un mejor panorama.

### Suposiciones

1. El número telefónico al que se llama es el del centro de trabajo. 
2. La planificacion mensual se realiza fuera del sistema
3. Cada centro de trabajo únicamente tiene un encargado asignado. 
4. El encargado tiene el conocimiento del sistema para el ingreso de la información requerida de asistencia. 
5. El encargado no se cambiará de centro de trabajo.

### Consultas

1. ¿El encargado puede ser transferido a otro centro de trabajo y cómo sería el proceso?
2. ¿Solo habrán cambios mensuales o pueden existir durante el periodo del mes?
3. ¿Existe algún estándar al momento de realizar el diseño del sistema?
4. ¿Qué características agregarían valor al sistema?
5. ¿Se necesitará seguimiento luego de la implementación de la funcionalidad?


