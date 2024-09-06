from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SQS, Eventbridge
from diagrams.aws.security import Cognito
from diagrams.aws.mobile import APIGateway
from diagrams.aws.network import ElasticLoadBalancing
from diagrams.aws.analytics import Kinesis

with Diagram("Arquitectura AWS App de Transporte", show=False):
    # Clientes
    api = APIGateway("API Gateway")
    
    with Cluster("Servicios de Autenticación"):
        cognito = Cognito("Cognito")
    
    with Cluster("Procesamiento de Solicitudes"):
        solicitud_viaje = Lambda("Solicitar Viaje")
        buscar_conductor = Lambda("Buscar Conductor")
        confirmar_viaje = Lambda("Confirmar Viaje")
    
    with Cluster("Gestión de Viajes"):
        iniciar_viaje = Lambda("Iniciar Viaje")
        finalizar_viaje = Lambda("Finalizar Viaje")
        calcular_tarifa = Lambda("Calcular Tarifa")
    
    with Cluster("Procesamiento de Pagos"):
        procesar_pago = Lambda("Procesar Pago")
    
    with Cluster("Almacenamiento de Datos"):
        db_usuarios = Dynamodb("DB Usuarios")
        db_viajes = Dynamodb("DB Viajes")
        db_pagos = Dynamodb("DB Pagos")
    
    cola_solicitudes = SQS("Cola de Solicitudes")
    stream_ubicaciones = Kinesis("Stream de Ubicaciones")
    bus_eventos = Eventbridge("Event Bus")

    # Flujo de la aplicación
    api >> cognito
    api >> solicitud_viaje >> cola_solicitudes >> buscar_conductor
    buscar_conductor >> confirmar_viaje
    confirmar_viaje >> iniciar_viaje >> stream_ubicaciones
    stream_ubicaciones >> finalizar_viaje >> calcular_tarifa >> procesar_pago
    
    # Interacciones con bases de datos
    [solicitud_viaje, buscar_conductor, confirmar_viaje] >> db_usuarios
    [iniciar_viaje, finalizar_viaje, calcular_tarifa] >> db_viajes
    procesar_pago >> db_pagos
    
    # Event-driven architecture
    [solicitud_viaje, confirmar_viaje, iniciar_viaje, finalizar_viaje, procesar_pago] >> bus_eventos