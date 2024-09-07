from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SQS, Eventbridge
from diagrams.aws.ml import Comprehend
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.saas.chat import Slack
from diagrams.aws.security import Cognito

with Diagram("Arquitectura de Gestión Inteligente de Impedimentos", show=False):
    # Entrada de datos
    api = APIGateway("API Gateway")
    auth = Cognito("Autenticación")

    with Cluster("Procesamiento de Transcripciones"):
        sqs_transcriptions = SQS("Cola de Transcripciones")
        lambda_process = Lambda("Procesador de Transcripciones")
        comprehend = Comprehend("Análisis de Texto")

    with Cluster("Gestión de Impedimentos"):
        eventbridge = Eventbridge("Event Bridge")
        lambda_impediment = Lambda("Gestor de Impedimentos")
        dynamodb = Dynamodb("Base de Datos")

    with Cluster("Integración Externa"):
        lambda_slack = Lambda("Integración Slack")
        slack = Slack("Slack")

    s3 = S3("Almacenamiento de Transcripciones")

    # Flujo de datos
    api >> auth
    auth >> sqs_transcriptions
    sqs_transcriptions >> lambda_process
    lambda_process >> comprehend
    lambda_process >> s3
    lambda_process >> eventbridge
    
    eventbridge >> lambda_impediment
    lambda_impediment >> dynamodb
    lambda_impediment >> lambda_slack
    
    lambda_slack >> slack