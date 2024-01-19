from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("recommendation") \
    .getOrCreate()
