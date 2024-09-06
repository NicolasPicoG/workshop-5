from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.storage import S3
from diagrams.aws.integration import SNS
from diagrams.aws.general import Client
 
# Crear el diagrama
with Diagram("Arquitectura de Aplicación de Transporte", show=False, direction="TB"):
 
    client_user = Client("Usuario")
    client_driver = Client("Conductor")
 
    with Cluster("Aplicación en AWS"):
        load_balancer = ELB("Load Balancer")
        with Cluster("Capa de Aplicación"):
            app_server = [EC2("Servidor de Aplicación 1"),
                          EC2("Servidor de Aplicación 2")]
        database = RDS("Base de Datos")
        storage = S3("Almacenamiento de Datos")
        # Notificaciones
        sns_notifications = SNS("Notificaciones")
 
    # Flujo del cliente a la app y la base de datos
    client_user >> load_balancer >> app_server
    client_driver >> load_balancer >> app_server
    app_server >> database
    app_server >> storage
    app_server >> sns_notifications