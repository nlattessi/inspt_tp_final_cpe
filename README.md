# TP Final Seminario - INSPT

### Diseño de CPE (Control Parque Equipos)

<br>

**Necesidad**

Un sistema que permita llevar un control del estado del parque de equipos, conformado por handhelds, asignadas a los vendedores de pie para su tarea diaria. Actualmente se utilizan planillas de cálculo para realizar la tarea.

<br>

**Objetivo**

Poder llevar un control más eficiente que permita detectar problemas y mejoras en la operatoria diaria. También, se busca tener un historial de información, necesario para elaborar los reportes y documentación para la presentación en la auditoría anual.

<br>

**Forma de uso del sistema propuesto**

El sistema, en su operatoria diaria, será usado por 2 tipos de usuarios distintos: administradores y de incidentes. Un administrador puede realizar tareas de cambio de datos en la base del sistema, ya sea con altas, bajas, modificaciones, cambios de estado, creación de nuevos usuarios, etc. En sí, tiene acceso al panel de administración. Por otro lado, un usuario de incidentes sólo puede cargar incidentes, los cuales son vistos por el administrador para poder realizar el cambio pertinente en los datos del sistema. Esta es la operatoria diaria prevista por el área que utilizará el sistema.

<br>

**Modelo de datos**

__Datos maestros:__

* Usuarios

* Estados

* Sucursales

* Handhelds

* Cambio de estado de handhelds

* Modalidad de venta

* Vendedores

* Tipos de incidente

* Incidentes

Usuarios:

Usuarios que pueden utilizar el sistema. Divididos en 2 grupos: administradores y de incidentes. El modelo está conformados por un nombre de usuario, un password, y dos variables booleanas que determinan si el usuario está activo y si es administrador.

Estados:

Posibles estados que puede tener una handheld. Son determinados previamente a su asociación a un equipo. Se consideran para este desarrollo los siguientes: Operativo (asignada a vendedor y en uso), Backup (sin asignar), Fuera de servicio (sin uso pero tampoco se manda a reparar por alguna razón como ser el alto costo de reparación por ejemplo), A reparar (se tiene que enviar a reparación), En reparación (se envió a reparar y se está esperando su devolución) y Robo (fue robada).

Sucursales:

El nombre y el código de cada sucursal de la empresa, a las cuales pertenecen cada handheld. En este desarrollo se van a utilizar las siguientes: Alvarado, Bahía Blanca, Córdoba, Mar del Plata, Mendoza, Neuquén, Posadas, Resistencia, Rosario, San Juan, Santa Fe y Tucuman.

Handhelds:

Tienen un número de serie (único) de 11 caracteres, un modelo, una sucursal asociada, un estado actual y la fecha del último cambio de estado realizado. Se asignan a un vendedor.

Modalidad de venta:

Es la forma de venta que pueden emplear los vendedores. Existen al momento las siguientes: Remoto y Local.

Vendedores:

Consisten en un legajo (único) de 8 números, una modalidad de venta, un nombre, apellido y una handheld asignada.

Tipos de incidentes:

Listado de los distintos tipos que puede ser un incidente. Se agregaron para este desarrollo los siguientes: Comunicación (por ejemplo no había señal suficiente), Hardware (por ejemplo se rompio la pantalla de un equipo) y Otros.

Incidentes:

Se arman con un tipo de incidente, una descripción, una solución, una handheld asociada, un vendedor asociado y una fecha de carga. Son creados por un usuario del sistema.

Cantidad de elementos actual aproximada:
* Usuarios del sistema: 4
* Parque de equipos: 600 Handhelds.
* Vendedores: 300

<br>

**Sistema propuesto**

*Casos de uso:*

* Dashboard:
    * Pantalla de control donde se ve por cada sucursal las handhelds asignadas según su estado, junto con el total del parque de equipos.
    * También muestra el *total* de equipos del parque y el *disponible* (que es el total de los equipos menos la cantidad de equipos no disponibles (es decir, robados más fuera de servicio)
* Ver incidentes del día:
    * Es una vista que lista los incidentes del día, para que el admin revise los cambios que debe cargar al sistema
* Cambiar el estado de un equipo del parque.
* Asignar y remover una handheld a un vendedor.
* Cambiar la sucursal a la cual está asociada una handheld.
* Cargar un incidente.
* Realizar tareas de administración (alta, baja y modificación de datos).

Navegación:

* Anónimo:

    * Login

* Administradores:

    * Home

    * Panel de administración

    * Dashboard

    * Ver incidentes del día

    * Ver todos los incidentes

    * Buscar handheld

    * Buscar vendedor

    * Logout

* De incidentes:

    * Cargar incidente

    * Logout

Pantallas:

* Login

* Dashboard

* Carga de incidente

* Incidentes del día

* Todos los incidentes

* Panel de administración y sus subpantallas (Django Admin)

* Cambiar estado de handheld

* Cambiar la sucursal de una handheld

* Asignar handheld a un vendedor

* Remover handheld asignada a vendedor

* Acceso denegado

Volumen de uso diario actual aproximada:

* Cargas de incidentes: 10

* Cambios en el parque de equipos: 3

**Posibles extensiones al sistema**

* Generación de reportes.

* Revisión del historial de cambio de estados.

URLs del sistema:

* Repositorio Github: 
