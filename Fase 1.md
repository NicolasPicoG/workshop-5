# Construyendo diagramas con GenAI

Prompt #1 GPT


Pront #1 CLAUDE

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
