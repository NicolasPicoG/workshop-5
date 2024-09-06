# Construyendo diagramas con GenAI

Prompt #1 GPT

@startuml
actor Usuario as U
participant "App de Transporte" as App
participant "Sistema de Gestión de Conductores" as SGC
participant "Conductor" as C

U -> App: Solicitar viaje
App -> SGC: Buscar conductor disponible
SGC -> C: Notificar solicitud de viaje
C -> SGC: Aceptar solicitud
SGC -> App: Conductor asignado
App -> U: Conductor asignado (datos del conductor)
U -> C: Confirmar ubicación
C -> U: Conductor en camino
C -> App: Conductor ha llegado
App -> U: Notificar llegada del conductor
U -> C: Iniciar viaje
C -> App: Viaje en curso
App -> U: Viaje en curso
C -> App: Finalizar viaje
App -> U: Notificar fin del viaje
U -> App: Realizar pago
App -> C: Confirmar pago
@enduml


Descripción:
Usuario solicita un viaje desde la app.
La App de Transporte consulta al Sistema de Gestión de Conductores (SGC) para encontrar un conductor disponible.
El Sistema de Gestión de Conductores notifica a los conductores cercanos.
Un Conductor acepta la solicitud, y la información se devuelve al usuario.
El Usuario confirma la ubicación y el Conductor se dirige hacia ��l.
Al llegar, el conductor notifica a la App, que a su vez notifica al usuario.
El Viaje comienza y, al finalizar, el pago se procesa a través de la app.

Prompt #1 CLAUDE

```
sequenceDiagram
    actor Usuario
    participant App
    participant Sistema
    actor Conductor
    participant SistemaPago

    Usuario->>App: Solicita viaje
    App->>Sistema: Envía solicitud de viaje
    Sistema->>Conductor: Notifica nuevo viaje disponible
    Conductor->>Sistema: Acepta el viaje
    Sistema->>App: Confirma viaje y asigna conductor
    App->>Usuario: Muestra información del conductor y vehículo

    Usuario->>App: Confirma ubicación de recogida
    App->>Conductor: Envía ubicación de recogida
    Conductor->>App: Confirma llegada al punto de recogida
    App->>Usuario: Notifica llegada del conductor

    Usuario->>Conductor: Aborda el vehículo
    Conductor->>App: Inicia el viaje
    App->>Usuario: Actualiza estado del viaje

    Conductor->>App: Finaliza el viaje
    App->>Sistema: Registra fin del viaje
    Sistema->>SistemaPago: Procesa el pago
    SistemaPago->>Sistema: Confirma pago exitoso
    Sistema->>App: Notifica pago completado
    App->>Usuario: Muestra resumen del viaje y solicita calificación
    App->>Conductor: Solicita calificación del usuario

    Usuario->>App: Envía calificación del conductor
    Conductor->>App: Envía calificación del usuario
    App->>Sistema: Registra calificaciones

```

Prompt #2 GPT

```
![Diagrama de secuencia generado por GPT](../src/images/gpt-prompt2.webp)
```

Prompt #2 CLAUDE

```
![Diagrama de secuencia generado por GPT](../src/images/gpt-prompt-2)

```


Prompt #3 GPT

### Ahora ayúdame a crear el diagrams de arquitectura utilizando la librería Diagram y Python para pintarla suponiendo que uso AWS

```
![Diagrama de secuencia generado por GPT](../src/images/gpt-prompt2.webp)
```

Prompt #3 CLAUDE

### Ahora ayúdame a crear el diagrams de arquitectura utilizando la librería Diagram y Python para pintarla suponiendo que uso AWS
```
![Diagrama de secuencia generado por GPT](../src/images/gpt-prompt-2)
