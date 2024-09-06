from diagrams import Diagram, Cluster
from diagrams.aws.compute import ECS, Lambda
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.network import ELB, APIGateway
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.aws.security import Cognito
from diagrams.aws.mobile import APIGateway

with Diagram("Arquitectura App de Transporte en AWS", show=False):
    # Clientes
    api_gateway = APIGateway("API Gateway")

    # Autenticación
    cognito = Cognito("Cognito")

    with Cluster("Servicios de Aplicación"):
        app_services = [
            ECS("Servicio de Usuarios"),
            ECS("Servicio de Viajes"),
            ECS("Servicio de Pagos"),
            Lambda("Servicio de Notificaciones")
        ]

    # Base de datos y caché
    db = RDS("Base de Datos")
    cache = ElastiCache("Cache")

    # Cola de mensajes
    queue = SQS("Cola de Eventos")

    # Almacenamiento
    storage = S3("Almacenamiento")

    # Flujo de la aplicación
    api_gateway >> cognito
    cognito >> app_services
    api_gateway >> app_services
    app_services >> db
    app_services >> cache
    app_services >> queue
    app_services >> storage