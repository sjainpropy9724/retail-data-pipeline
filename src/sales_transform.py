from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def clean_sales(df):
  return df.filter(col("amount") > 0)

if __name__ == "main":
  spark = SparkSession.builder.appName("RetailSales").getOrCreate()
  data = [("1", 100.0), ("2", -5.0), ("3", 250.0)]
  df = spark.createDataFrame(data, ["order_id", "amount"])
  clean_sales(df).show()
