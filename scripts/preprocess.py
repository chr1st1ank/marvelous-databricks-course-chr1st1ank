
# COMMAND ----------
import pathlib
from pyspark.sql import SparkSession
from booking import preprocessing
import pandas as pd

class Config:
    data_file = "/Volumes/xdiv_sbox_dev/uc_sandbox/data/Hotel Reservations.csv"
    catalog_name = "xdiv_sbox_dev"
    schema_name = "uc_sandbox"
    table_name_prefix = "ck_hotel_reservations"

config = Config()

# COMMAND ----------
spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

df = preprocessing.load_csv(spark, config.data_file)
df.head(5)

# COMMAND ----------
train, test = preprocessing.train_test_split(df, test_ratio=0.2)
test.head(5)

# COMMAND ----------
preprocessing.save_to_catalog(train, config.catalog_name, config.schema_name, f"{config.table_name_prefix}_train")
preprocessing.save_to_catalog(test, config.catalog_name, config.schema_name, f"{config.table_name_prefix}_test")
