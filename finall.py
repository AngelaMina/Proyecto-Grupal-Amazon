from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType
from pyspark.ml.feature import Tokenizer, StopWordsRemover, StringIndexer
from pyspark.ml.feature import HashingTF, IDF
from pyspark.ml import Pipeline
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import lit
from pyspark.sql.functions import monotonically_increasing_id
from pyspark.sql.functions import col
from pyspark.sql.functions import desc
from pyspark.sql.functions import expr
import shutil


# Función para iniciar una sesión de Spark
def iniciar_sesion_spark():
    spark = SparkSession.builder.appName("Recommend").getOrCreate()
    return spark

# Función para obtener recomendaciones usando ALS
def obtener_recomendaciones_als(spark, product_id_input):
    # Importar biblioteca para la base de datos
    import pyodbc

    # Configurar la información de la base de datos
    jdbcHostname = "amazonhenry.database.windows.net"
    jdbcDatabase = "amazon"
    jdbcPort = "1433"
    username = "amazon"
    password = "Agec1234"

    # Construir la URL JDBC con el controlador de Microsoft SQL Server
    jdbcUrl = "jdbc:sqlserver://{0}:{1};database={2}".format(jdbcHostname, jdbcPort, jdbcDatabase)

    # Propiedades de conexión
    connectionProperties = {
        "user": username,
        "password": password,
        "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
    }

    # Consulta SQL
    pushdown_query = "(SELECT * FROM dbo.total_data) as total_data"
    # Leer datos desde SQL Server y cargar en un DataFrame
    df = spark.read.jdbc(url=jdbcUrl, table=pushdown_query, properties=connectionProperties)

    # Realizar preprocesamiento de datos
    # Tokenización de reseñas
    tokenizer = Tokenizer(inputCol="review_text", outputCol="words")
    df = tokenizer.transform(df)

    # Eliminación de stopwords de las palabras tokenizadas
    remover = StopWordsRemover(inputCol="words", outputCol="filtered_words")
    df = remover.transform(df)

    # Cambiar el nombre de las columnas en el DataFrame con alias
    df = df.withColumnRenamed("product_nro", "product_nro_alias")

    # Crear un índice numérico para la columna "product_id"
    indexer = StringIndexer(inputCol="product_id", outputCol="product_nro_alias")
    df = indexer.fit(df).transform(df)

    # Crear un índice numérico para la columna "reviewer_id"
    reviewer_indexer = StringIndexer(inputCol="reviewer_id", outputCol="reviewer_id_alias")
    df = reviewer_indexer.fit(df).transform(df)

    # Crear un modelo ALS (Alternating Least Squares) para recomendación
    als = ALS(maxIter=60, regParam=0.01, userCol="reviewer_id_alias", itemCol="product_nro_alias", ratingCol="product_score", coldStartStrategy="drop")

    # Ajustar el modelo ALS
    model = als.fit(df)

    # Obtener el product_nro_alias para el product_id de entrada
    product_nro_alias = df.filter(col("product_id") == product_id_input).select("product_nro_alias").collect()

    if product_nro_alias:
        product_nro_alias = product_nro_alias[0][0]
        user_recs = model.recommendForUserSubset(df.filter(col("product_nro_alias") == product_nro_alias), 3)

        # Obtener información de los productos recomendados
        recommendations = user_recs.select("recommendations.product_nro_alias").collect()[0][0]
        recommended_products = df.filter(col("product_nro_alias").isin(recommendations)).select("product_name", "product_id", "product_imurl").distinct()
        return recommended_products
    else:
        return "Producto no encontrado en los datos."
