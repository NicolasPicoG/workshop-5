from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import ECS, Lambda, ElasticContainerServiceService
from diagrams.aws.database import Dynamodb, ElastiCache
from diagrams.aws.integration import SQS, SNS, Eventbridge
from diagrams.aws.ml import Comprehend
from diagrams.aws.network import APIGateway, ELB
from diagrams.aws.storage import S3
from diagrams.aws.security import Cognito
from diagrams.aws.management import Cloudwatch
from diagrams.saas.chat import Slack

graph_attr = {
    "fontsize": "45",
    "bgcolor": "transparent"
}

with Diagram("Arquitectura de Microservicios para Gestión Inteligente de Impedimentos", show=False, direction="TB", graph_attr=graph_attr):
    # Entrada de datos
    api = APIGateway("API Gateway")
    auth = Cognito("Autenticación")

    with Cluster("Ingesta y Procesamiento"):
        sqs_transcriptions = SQS("Cola de Transcripciones")
        with Cluster("Microservicio de Procesamiento"):
            nlp_service = ECS("Servicio NLP")
            comprehend = Comprehend("Análisis de Texto")

    with Cluster("Gestión de Impedimentos"):
        eventbridge = Eventbridge("Event Bridge")
        with Cluster("Microservicio de Impedimentos"):
            impediment_service = ECS("Servicio de Impedimentos")
            impediment_db = Dynamodb("DB Impedimentos")
        
        with Cluster("Microservicio de Resolución"):
            resolution_service = ECS("Servicio de Resolución")
            resolution_db = Dynamodb("DB Resoluciones")

    with Cluster("Notificaciones"):
        sns = SNS("Servicio de Notificaciones")
        with Cluster("Microservicio de Integración Slack"):
            slack_service = Lambda("Integración Slack")
        slack = Slack("Slack")

    with Cluster("Microservicio de Calendario"):
        calendar_service = ECS("Servicio de Calendario")
        calendar_cache = ElastiCache("Cache de Calendario")

    s3 = S3("Almacenamiento de Transcripciones")
    cloudwatch = Cloudwatch("Monitoreo")

    # Flujo de datos
    api >> Edge(label="1. Ingesta") >> auth
    auth >> sqs_transcriptions
    sqs_transcriptions >> Edge(label="2. Procesa") >> nlp_service
    nlp_service - comprehend
    nlp_service >> s3
    nlp_service >> Edge(label="3. Detecta") >> eventbridge
    
    eventbridge >> Edge(label="4. Gestiona") >> impediment_service
    impediment_service - impediment_db
    
    impediment_service >> Edge(label="5. Resuelve") >> resolution_service
    resolution_service - resolution_db
    
    resolution_service >> Edge(label="6. Notifica") >> sns
    sns >> slack_service
    slack_service >> slack
    
    sns >> Edge(label="7. Agenda") >> calendar_service
    calendar_service - calendar_cache

    cloudwatch << Edge(label="Logs & Métricas") << [nlp_service, impediment_service, resolution_service, slack_service, calendar_service]