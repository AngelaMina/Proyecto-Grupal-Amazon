## Descripcion de base de datos

La  base de datos que se proporciona al equipo se compone de dos tipos de tablas: una tabla de metadatos generales, que alberga variables relacionadas con cada producto en el diverso catálogo de Amazon; y  24 tablas de reseñas de usuarios, todas categorizadas por productos. En este contexto, enfocaremos nuestra atención en cinco de estas categorías primordiales, a saber:

- **Grocery and Gourmet Food**

- **Home and Kitchen**

- **Patio, Lawn and Garden**  

- **Pet Supplies**

- **Tools and Home Improvement**

En lo que respecta a la dimensión temporal que abarca esta base de datos, se extiende desde el **7 de noviembre de 1999** (siendo la categoría *Tools and Home Improvement* la que alberga la reseña más antigua documentada)  hasta el **22 de julio de 2014**, marcando el punto más reciente de nuestro registro.

## Diccionario de Datos

### Tabla de Reviews:

- **reviewerID:** Identificador del usuario que realizó la revisión (no es único).
- **asin:** Identificador del producto al que se hizo la revisión.
- **reviewerName:** Nombre del usuario que realizó la revisión.
- **helpful:** Calificación de la revisión, en el formato "número de personas que la calificaron como útil / número total de revisiones sobre el producto". Su tipo de dato es una lista.
- **reviewText:** Contenido de la revisión.
- **overall:** Puntuación dada al producto en una escala del 1 al 5.
- **summary:** Resumen de la revisión.
- **unixReviewTime:** Fecha de la revisión en formato Unix time.
- **reviewTime:** Fecha de la revisión en formato legible.

### Tabla de Metadata de Productos:

- **asin:** Identificador del producto.
- **salesRank:** Ranking del producto en una categoría específica (donde mejor rankeado esté).
- **imUrl:** URL de la imagen del producto.
- **categories:** Categorías en las que aparece el producto (puede haber más de una categoría por producto).
- **title:** Nombre del producto.
- **description:** Breve descripción del producto.
- **price:** Precio en dólares del producto.
- **related:** Productos relacionados, que pueden incluir productos comprados juntos, también revisados, comprados por el mismo usuario, o comprados luego de verlos. Utiliza ID de productos y usuarios respectivamente.
- **brand:** Nombre de la marca del producto.

---


## EDA preliminar

**Tablas de Reviews**

Para la realización de este Análisis Exploratorio de Datos (EDA) preliminar, se utilizó el 100% de los datos de cada tabla. Se observaron las siguientes características:

- No contienen valores nulos significativos, con un porcentaje de valores faltantes que oscila entre el 0.5% y el 1.2% del total de los datos en cada tabla, respectivamente. Estos valores nulos se limitan únicamente a las columnas de "reviewerName", los cuales serán reemplazados por "NoData".

- No se encontraron valores duplicados en ninguna de las tablas.

**Tablas de Metadata**

Para la realización de este análisis exploratorio de datos (EDA) preliminar, se utilizaron los primeros 500,000 registros del conjunto total. Durante este proceso, se observaron las siguientes características:

- La columna "brand" contiene una cantidad significativa de valores faltantes. De los 500,000 datos, 499,619 presentan valores faltantes en esta columna. Al tratarse de una columna sumamente importante para nuestro analisis, intentaremos imputar sus valores faltantes consiguiendo estos datos a travez de otros medios.

- La columna "description", que proporciona una breve descripción del producto, contiene aproximadamente el 30% de valores faltantes. Es posible que esta columna no sea necesaria para nuestro análisis, por lo que será eliminada.

- En la columna "price" falta aproximadamente el 20% de los valores. De ser necesaria esta columna, intentaremos imputar los valores faltantes por otro medio.

- La mayoría de las otras columnas mantienen casi la totalidad de la integridad de los datos. Sin embargo, en la columna "title", que se refiere al nombre del producto, encontramos cerca del 1% de valores nulos o faltantes. Estos registros sin nombre se eliminarán.

Además, para facilitar el análisis, podríamos considerar las siguientes transformaciones:

- En la columna "categories", se podría realizar una desagregación de listas, posiblemente utilizando algún método de codificación que optimice el espacio y el procesamiento. Esto crearía una columna separada para cada una de las categorías, donde los valores podrían ser True o False, indicando la presencia o ausencia de la categoría en el producto.

- Para tratar eficazmente la columna "helpfull", se podria crea una nueva columna para almacenar solo la cantidad total de reviews y otra columna donde se almacene el porcentaje de reviews que fueron provechozas sobre el total.

- Es necesario determinar si se utilizara la columna **reviewTime** o **unixReviewTime**, de ser así se deberian realizar las transformaciones necesesarias y elegir una sola de ellas. 

- Se podría crear una columna donde se almacene un analisis de sentimientos de la columna "reviewText" y "summary" combinadas. Para esto podriamos aplicar el modelo *RoBERTa* o *VADER*. Con esto podriamos reducir significativamente el tamaño de nuestra base de datos.

---



## Convenciones de Nombramiento

Se renombrarán las columnas de los diferentes datasets utilizando el formato "snake_case". Además, se renombrarán las siguientes columnas para mantener la homogeneidad de la base de datos.

**Tablas de Reviews**
- reviewerID = reviewer_id
- asin = product_id
- overall = product_score
- reviewText = review_text
- reviewTime = review_time
- reviewerName = reviewer_name

**Tablas de Metadata**
- asin = product_id
- brand = product_brand
- main_cat = main_category
- title = product_name
- price = product_price
- imUrl = product_imurl
