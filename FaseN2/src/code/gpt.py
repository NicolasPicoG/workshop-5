from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.storage import S3
from diagrams.aws.integration import SNS
from diagrams.aws.general import Users

# Crear el diagrama
with Diagram("Casos de Uso: Usuarios Visitantes vs Logueados", show=False, direction="TB"):

    with Cluster("Usuarios"):
        visitor = Users("Usuario Visitante")
        logged_in = Users("Usuario Logueado")

    with Cluster("Aplicación en AWS"):
        load_balancer = ELB("Load Balancer")
        
        with Cluster("Capa de Aplicación"):
            app_server = EC2("Servidor de Aplicación")
        
        database = RDS("Base de Datos")
        storage = S3("Almacenamiento de Datos")
        sns_notifications = SNS("Notificaciones")

    # Casos de uso para usuario visitante
    visitor >> load_balancer >> app_server
    app_server >> database.edge(label="Consultar información pública")

    # Casos de uso para usuario logueado
    logged_in >> load_balancer >> app_server
    app_server >> database.edge(label="CRUD operaciones")
    app_server >> storage.edge(label="Acceso a datos personales")
    app_server >> sns_notifications.edge(label="Recibir notificaciones")

#Crear Diagrama 2

from plantuml import PlantUML

plantuml = PlantUML(url='http://www.plantuml.com/plantuml/png/')

uml_code = """
@startuml

skinparam actorStyle awesome
skinparam usecase {
  BackgroundColor LightBlue
  BorderColor DarkBlue
  ArrowColor Navy
}

actor Visitor as "Usuario Visitante"
actor LoggedUser as "Usuario Logueado"
actor Resolutor

rectangle "Sistema de Gestión de Impedimentos" {
    usecase "Lectura de Transcripción" as UC1
    usecase "Identificación de Impedimentos Reportados" as UC2
    usecase "Predicción de Futuros Impedimentos" as UC3
    usecase "Clasificación de Impedimentos" as UC4
    usecase "Agendamiento de Sesiones con Resolutores" as UC5
    usecase "Notificación de Impedimentos" as UC6
    usecase "Registro de Impedimentos" as UC7
    usecase "Iniciar Sesión" as UC8
    usecase "Registrarse" as UC9
    usecase "Ver Estadísticas Públicas" as UC10
}

Visitor --> UC1
Visitor --> UC10
Visitor --> UC8
Visitor --> UC9

LoggedUser --> UC1
LoggedUser --> UC2
LoggedUser --> UC3
LoggedUser --> UC4
LoggedUser --> UC5
LoggedUser --> UC6
LoggedUser --> UC7
LoggedUser --> UC10

Resolutor --> UC5
Resolutor --> UC6
Resolutor --> UC7

note right of UC1
  Todos los usuarios pueden 
  leer transcripciones públicas
end note

note right of UC8
  Los visitantes pueden iniciar sesión
  para convertirse en usuarios logueados
end note

note bottom of Resolutor
  Los resolutores son usuarios logueados
  con permisos adicionales
end note

@enduml
"""

png_data = plantuml.processes(uml_code)
with open("diagrama_casos_uso.png", "wb") as f:
    f.write(png_data)

print("Diagrama generado como 'diagrama_casos_uso.png'")

# Diagrama de componentes en PlantUML

@startuml

#  Interacción de usuarios con el sistema
package "Capa de Presentación" {
    [Interfaz Web]
    [API REST]
}

# Servicios que encapsulan la lógica del negocio
package "Capa de Negocio" {
    [Servicio de Gestión de Impedimentos] as ServicioImpedimentos
    [Servicio de Gestión de Proyectos] as ServicioProyectos
    [Servicio de Gestión de Usuarios] as ServicioUsuarios
}

# Almacenamiento de la información estructurada en BD relacionales
package "Capa de Persistencia" {
    database "Base de Datos de Proyectos" as BDProyectos
    database "Base de Datos de Impedimentos" as BDImpedimentos
    database "Base de Datos de Usuarios" as BDUsuarios
}

[Interfaz Web] --> ServicioImpedimentos
[Interfaz Web] --> ServicioProyectos
[Interfaz Web] --> ServicioUsuarios

[API REST] --> ServicioImpedimentos
[API REST] --> ServicioProyectos
[API REST] --> ServicioUsuarios

ServicioImpedimentos --> BDImpedimentos
ServicioProyectos --> BDProyectos
ServicioUsuarios --> BDUsuarios

@enduml

# Diagrama1 de componentes en PlantUML

@startuml

skinparam actorStyle awesome
skinparam usecase {
  BackgroundColor LightBlue
  BorderColor DarkBlue
  ArrowColor Navy
}

actor Visitor as "Usuario Visitante"
actor LoggedUser as "Usuario Logueado"
actor Resolutor

rectangle "Sistema de Gestión de Impedimentos" {
    usecase "Lectura de Transcripción" as UC1
    usecase "Identificación de Impedimentos Reportados" as UC2
    usecase "Predicción de Futuros Impedimentos" as UC3
    usecase "Clasificación de Impedimentos" as UC4
    usecase "Agendamiento de Sesiones con Resolutores" as UC5
    usecase "Notificación de Impedimentos" as UC6
    usecase "Registro de Impedimentos" as UC7
    usecase "Iniciar Sesión" as UC8
    usecase "Registrarse" as UC9
    usecase "Ver Estadísticas Públicas" as UC10
}

Visitor --> UC1
Visitor --> UC10
Visitor --> UC8
Visitor --> UC9

LoggedUser --> UC1
LoggedUser --> UC2
LoggedUser --> UC3
LoggedUser --> UC4
LoggedUser --> UC5
LoggedUser --> UC6
LoggedUser --> UC7
LoggedUser --> UC10

Resolutor --> UC5
Resolutor --> UC6
Resolutor --> UC7

note right of UC1
  Todos los usuarios pueden 
  leer transcripciones públicas
end note

note right of UC8
  Los visitantes pueden iniciar sesión
  para convertirse en usuarios logueados
end note

note bottom of Resolutor
  Los resolutores son usuarios logueados
  con permisos adicionales
end note

@enduml

# Diagrama en formato Mermaid

graph TD
    subgraph Capa_de_Presentación
        Interfaz_Web
        API_REST
    end

    subgraph Capa_de_Negocio
        Servicio_Gestión_Impedimentos
        Servicio_Gestión_Proyectos
        Servicio_Gestión_Usuarios
    end

    subgraph Capa_de_Persistencia
        BD_Proyectos
        BD_Impedimentos
        BD_Usuarios
    end

    %% Relaciones de la capa de presentación con los servicios de negocio
    Interfaz_Web --> Servicio_Gestión_Impedimentos & Servicio_Gestión_Proyectos & Servicio_Gestión_Usuarios
    API_REST --> Servicio_Gestión_Impedimentos & Servicio_Gestión_Proyectos & Servicio_Gestión_Usuarios

    %% Relaciones de los servicios de negocio con la capa de persistencia
    Servicio_Gestión_Impedimentos --> BD_Impedimentos
    Servicio_Gestión_Proyectos --> BD_Proyectos
    Servicio_Gestión_Usuarios --> BD_Usuarios

# Diagrama de arquitectura con DiagramGPT
graph TD
    subgraph "Frontend"
        Web_Browser -->|HTTPS Request| AWS_CloudFront
        AWS_CloudFront -->|Route| API_Gateway
    end

    subgraph "API Gateway Layer"
        API_Gateway -->|REST API| Load_Balancer
    end

    subgraph "Microservices"
        Load_Balancer -->|Forward| MS_Impediment[Impediment Service]
        Load_Balancer -->|Forward| MS_Project[Project Service]
        Load_Balancer -->|Forward| MS_User[User Service]
        Load_Balancer -->|Forward| MS_Notification[Notification Service]
    end

    subgraph "Databases"
        MS_Impediment --> DB_Impediment[(RDS Impediment DB)]
        MS_Project --> DB_Project[(RDS Project DB)]
        MS_User --> DB_User[(RDS User DB)]
        MS_Notification --> DB_Notification[(RDS Notification DB)]
    end

    subgraph "AWS Services"
        AWS_CloudFront -->|Cache static content| S3_Bucket
        Load_Balancer --> ECS_EKS_Cluster[ECS/EKS Cluster]
        ECS_EKS_Cluster -->|Containers| MS_Impediment & MS_Project & MS_User & MS_Notification
    end
