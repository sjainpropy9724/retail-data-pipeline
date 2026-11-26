# COMMAND -------
print("Running Sales Notebook")

# COMMAND -------
df = spark.createDataFrame([("CUST_1", "North"), ("CUST_2", "South")], ["customer_id", "region"])
display(df)

