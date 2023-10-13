INTRODUCCIÓN

Amazon, un líder indiscutible en innovación y satisfacción del cliente, busca mantener su posición destacada en el mercado estadounidense al colaborar con nuestra consultora. Este proyecto aprovecha los datos históricos de Amazon, incluyendo millones de reseñas y metadatos, para impulsar futuras ventas y mejoras. Nuestra misión es fusionar la analítica de ventas y reseñas con la inteligencia artificial, creando un sistema de recomendación que mejore la experiencia del cliente y aumente las ventas. Este sistema personalizado se basa en datos de usuario y utiliza avanzados análisis de sentimientos y modelos inteligentes.
En un mundo donde los datos son esenciales, estamos construyendo una arquitectura de datos sólida. Con pipelines eficientes y un dashboard informativo, permitimos decisiones informadas, incluso al manejar grandes volúmenes de datos. Nos enfocamos en la categoría hogar, considerada clave para aumentar las ventas, y adaptamos nuestras estrategias según las tendencias del mercado. Este proyecto promete innovación y éxito en un mercado competitivo.

OBJETIVO GENERAL 

Desarrollar y desplegar un sistema de recomendación de productos basados en análisis de datos, inteligencia artificial y análisis de sentimiento de reseñas, utilizando los datos históricos de Amazon, con el propósito de mejorar significativamente la experiencia del cliente y aumentar las ventas, manteniendo así el propósito de liderazgo de Amazon en el mercado.
OBJETIVOS ESPECÍFICOS
1 Diseñar y construir una arquitectura de datos eficiente y escalable que permita la adquisición, procesamiento y análisis de grandes volúmenes de datos históricos de Amazon, incluyendo reseñas y metadatos de productos
2 Desarrollar modelos avanzados de inteligencia artificial y análisis de sentimiento que permitan comprender a fondo las opiniones y preferencias de los clientes a partir de las reseñas, generando así recomendaciones de productos altamente personalizadas y precisas.
3 Implementar un sistema de recomendación de productos en la categoría hogar, alineado con las tendencias actuales, basado en historiales de compras y análisis de sentimiento, con el fin de aumentar la satisfacción del cliente y las ventas.


PRIMERA SEMANA

Colaboración con Amazon: Obtener datos de productos y recomendaciones de Amazon.
Creación de un entorno virtual en Azure: Configurar un entorno virtual en Azure para procesar los datos
EDA preliminar y diccionario de datos
ETL: Realizar la extracción, transformación y carga de los datos de Amazon en el entorno de local.
Creación del repositorio Github
Creación del diagrama de Gantt


SEGUNDA SEMANA


Machine Learning: Desarrollar modelos de análisis de sentimiento y recomendación de productos.
Diagrama de arquitectura de datos
Creación y automatización del datawarehouse
Carga incremental de datos
MVP Dashboard
Modelos y MVP producto ML
MVP Streamlit

Se realizó en primera instancia la investigación sobre esta herramienta, se crea un entorno virtual para trabajar en local inicialmente, luego se instalan las librerías streamlit, requests, y se importan las clases streamlit_lottie y PIL. Se realiza el código el cual se distribuye por 9 contenedores en los cuales se encuentra el titulo, nuestra mision, clientes, productos funcionamiento de sistema de recomendación, y formato de contacto, también se encuentran otros archivos los cuales son necesarios para el funcionamiento de la página, para darle diseño y recibir la información del usuario.

TERCERA SEMANA


Interfaz de usuarios: Crear una interfaz que permita a los usuarios recibir recomendaciones de productos.


ARQUITECTURA DE DATOS
Optamos por llevar a cabo nuestro proyecto aprovechando las ventajas de los servicios en la nube de Azure, mediante su capa gratuita que proporciona un bono de 200 USD para utilizar en distintos servicios ofrecidos por este proveedor. Para estructurar nuestro enfoque, hemos categorizado las herramientas en tres clasificaciones principales: almacenamiento, procesamiento y visualización, cada una desempeñando un papel fundamental en el desarrollo y éxito de nuestro proyecto.

![aruitecturadedatos](https://github.com/AngelaMina/Proyecto-Grupal-Amazon/blob/main/imagenes/arquitecturadedatos.png)

Almacenamiento:

Azure Data Lake Storage Blob Storage: la utilizamos para almacenar vastas cantidades de datos en las diversas etapas del proyecto. Su escalabilidad fue clave para la gestión eficiente de grandes volúmenes de información, facilitando el proceso de almacenamiento en diferentes fases del proyecto.

Azure SQL Database: esta base de datos relacional en la nube desempeñó un papel fundamental en la creación del data warehouse. Al alojar datos limpios y estructurados, nos permitió trabajar eficazmente y generar las herramientas de visualización necesarias para el proyecto.

Procesamiento:

Azure Databricks: integramos Azure Databricks en nuestro flujo de procesamiento para aprovechar su plataforma colaborativa basada en Apache Spark. Esta herramienta fue esencial para llevar a cabo la limpieza, transformación y análisis de datos a gran escala. Facilitó la ejecución de tareas distribuidas, asegurando eficiencia en el manejo de conjuntos de datos extensos.

Azure Data Factory: la orquestación y automatización del flujo de datos se lograron mediante Azure Data Factory. Esta herramienta nos permitió gestionar de manera eficiente la ingesta, preparación y transformación de datos, asegurando un flujo continuo y coherente en todas las etapas del proyecto.

Databricks Machine Learning: para la construcción de modelos de machine learning a gran escala, recurrimos a Databricks Machine Learning, parte integral de la plataforma Databricks. Con algoritmos avanzados y capacidad de procesamiento distribuido, esta herramienta nos permitió entrenar modelos con conjuntos de datos extensos, contribuyendo así a la mejora de nuestras capacidades predictivas.

Visualización:

Streamleat (Web Framework): la capa de visualización de nuestro proyecto fue potenciada por Streamleat, un robusto framework web. Este framework proporcionó la estructura necesaria para la presentación de datos de manera intuitiva y atractiva. Su flexibilidad nos permitió diseñar interfaces de usuario interactivas, facilitando la experiencia del usuario final en la exploración de los resultados obtenidos.

Power BI: para la creación de dashboards dinámicos y la generación de informes visuales, optamos por Power BI. Esta herramienta de Microsoft no solo se integra sin problemas con otras soluciones de Azure, sino que también ofrece una amplia gama de opciones de visualización. Desde gráficos interactivos hasta tablas dinámicas, Power BI fue esencial para transformar datos en información comprensible y accionable. La combinación de Streamleat y Power BI proporcionó una experiencia completa de visualización, asegurando que los resultados del proyecto fueran accesibles y fácilmente interpretados.

ENTREGABLES

Reportes sobre análisis de sentimientos
Modelo de recomendación de sentimientos
Código fuente del sistema de recomendación
Interfaz de usuario funcional
Diccionario de datos.
Documentación del proyecto

RESTRICCIONES Y LIMITACIONES

Volumen de datos: Aunque nuestro proyecto está diseñado para manejar grandes cantidades de datos, las limitaciones de capacidad de almacenamiento y procesamiento pueden surgir, especialmente si Amazon proporciona datos adicionales o actualizaciones a largo plazo.
Recursos: La elección de las herramientas y tecnologías pueden incurrir en retrasos o incurrir en gastos económicos.
Plazos de entrega: El proyecto tiene plazos establecidos, y cualquier retraso puede afectar la calidad y completitud de las entregas.
Recomendaciones seccionadas: Debido al tamaño de los datos, el proyecto se centrará en seccionar y analizar ciertas categorías de productos de Amazon, por lo que es importante considerar que las categorías son más relevantes y estratégicas para el cliente y sus usuarios.
 
