# 🚀 Workshop 5

¡Bienvenido al repositorio del **Workshop N°5**! 🎉 Aquí encontrarás la solución completa del workshop, organizada en tres fases. Este proyecto tiene como objetivo resolver los desafíos presentados en el Workshop N°5. A lo largo de este documento, te guiaremos a través de las tres fases principales del desarrollo.


## 📋 Contenido

- [Fase 1: Construyendo diagramas con GenAI](FaseN1)
- [Fase 2: Planeando un software con GenAI](FaseN2)
- [Fase 3: Trabajando como Tech Lead con GenAI](FaseN3)

## 🛠️ Fase 1: Construyendo diagramas con GenAI

Para esta parte, usaremos ChatGPT y Claude en paralelo. Cada prompt lo trabajaremos tanto en ChatGPT como en Claude.

### Prompts:

1. **Prompt #1**: Dame un ejemplo de un diagrama de secuencia en PlantUML de una app de transporte similar a Uber.
    - Analiza la respuesta, incorpórala en un archivo markdown en un proyecto nuevo en Cursor.
2. **Prompt #2**: Me puedes mostrar la gráfica de ese lenguaje?
    - Analiza la respuesta y compara la que te da ChatGPT con la que te da Claude.
3. **Prompt #3**: Ahora ayúdame a crear el diagrama de arquitectura utilizando la librería Diagrams y Python para pintarla suponiendo que uso AWS.
    - Descríbele inspirándote en estos prompts (compara los dos LLMs) la prueba que estás haciendo para tu proyecto (el demo que tienes pensado para el MVP).
    - Trata de describirle todos los componentes clave a nivel arquitectónico y hacer iteraciones hasta que llegues a la versión que realmente refleja la prueba que quieres hacer, genera el diagrama de secuencia, un diagrama de interacción de entidades y la arquitectura tentativa para AWS.

## 📝 Fase 2: Planeando un software con GenAI

Vamos a iniciar con una investigación del tipo de sistemas que queremos trabajar, utilizando GenAI.

### Prompts:

1. **Prompt 1**: Eres un experto en producto, con experiencia en [TU TIPO DE SISTEMA]. ¿Qué funcionalidades básicas tiene un [TU TIPO DE SISTEMA]? Descríbemelas en un listado, ordenado de mayor a menor prioridad.
2. **Prompt 2**: ¿Qué beneficios obtiene el cliente de un [TU TIPO DE SISTEMA] para considerar su uso?
3. **Prompt 3**: ¿Cómo es el customer journey normal de un cliente que usa un [TU TIPO DE SISTEMA]? Descríbeme paso a paso todas las interacciones.

Ahora iniciemos con la planeación del sistema desde los casos de uso.

### Prompts:

1. **Prompt 1**: Eres un analista de software experto. Estoy construyendo un MVP de un [TU TIPO DE SISTEMA] que sólamente haga [LA PARTE CLAVE QUE QUIERES PROBAR]. Enumera y describe brevemente los casos de uso más importantes a implementar para lograr una funcionalidad básica.
2. **Prompt 2**: Representa estos casos de uso en el tipo de diagrama más adecuado usando el formato plantUML. Diferencia entre usuarios visitantes y usuarios logueados. Acorde a la sintaxis y buenas prácticas UML, define y describe lo que sea necesario.

Diseñemos ahora las entidades principales para la base de datos.

### Prompts:

1. **Prompt 1**: Eres un arquitecto de software experto. ¿Cuáles son las 3 entidades de modelo de datos esenciales en un sistema de [TU TIPO DE SISTEMA]? Dame algunos campos esenciales de cada una y cómo se relacionan.
2. **Prompt 2**: Eres un arquitecto de software. Eres capaz de diseñar, explicar y diagramar los diferentes aspectos de un sistema de software. Estoy construyendo un sistema de [TU TIPO DE SISTEMA]. He definido las entidades [MENCIONA LAS 3 PRINCIPALES ENTIDADES], con sus campos y relaciones.
3. **Prompt 3**: Generame un diagrama Mermaid de este sistema.

Ahora pruebe a generar el diagrama de arquitectura con DiagramGPT.

### Prompt:

1. **Prompt 1**: A microservices architecture for an [YOUR SYSTEM TYPE] system like Expedia. Each MS has its own database. Also has a frontend that communicates through API. Cloud provider is AWS, use proper services. Include load balancing and CDN.

## 💼 Fase 3: Trabajando como Tech Lead con GenAI

Ahora trabajaremos generando las User Stories y los Tasks (o tickets de Jira) para iniciar el desarrollo. Para esto generaremos un documento de especificación de requerimientos con todo lo que construimos en la Fase 2. Tenga este documento listo en un Word o un PDF (incluye los diagramas en gráfico, pero también en lenguaje Mermaid o PlantUML).

### Prompts:

1. **Prompt 1**: Ten en cuenta el siguiente documento de especificación de requerimientos. (Subir el documento o copiar el texto). Responde: “entiendo el documento”, pero no lo expliques.
2. **Prompt 2**: Actuando como un Analista de Software, construye un listado de las principales User Stories para completar el MVP de [DESCRIPCIÓN DE TU MVP] del sistema [TU TIPO DE SISTEMA].
3. **Prompt 3**: Actuando como un Product Owner, descríbeme la User Story [PRIMERA USER STORY] de forma detallada.
4. **Prompt 4**: Actuando como un Software Architect y un Tech Lead, genérame los tickets de trabajo (tasks) de Jira para realizar la user story [TU PRIMERA USER STORY]. Quiero que los tickets tengan:
    - ID del Ticket:
    - Título del Ticket:
    - Descripción:
    - Criterios de aceptación:
    - Prioridad:
    - Estimación de esfuerzo (en horas):
    - Tareas Técnicas:
    - Notas
---

¡Gracias por visitar el repositorio del Workshop N°5! Si tienes alguna pregunta, no dudes en abrir un issue o contactarnos. 😊
