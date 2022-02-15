from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
spark
schema= StructType([
    StructField("Order ID",StringType(),True),
    StructField("Product",StringType(),True),
    StructField("Quantity Ordered",StringType(),True),
    StructField("Price Each",StringType(),True),
    StructField("Order Date",StringType(),True),
    StructField("Purchase Address",StringType(),True)
])
sales_raw_df=spark.read.option('header','true').schema(schema).csv('salesdata',inferSchema=True)
sales_raw_df.show(10)
sales_raw_df.printSchema()
