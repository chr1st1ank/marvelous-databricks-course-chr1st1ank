"""
Load the source data, split it into train and test sets, and save them to a catalog table.
"""

# COMMAND ----------
from pathlib import Path

from pyspark.sql import SparkSession

from booking import preprocessing
from booking.config import Config

config = Config.from_toml(Path("../project_config.toml"))
config

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
