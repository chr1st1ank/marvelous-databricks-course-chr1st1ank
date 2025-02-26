def load_csv(spark, data_file):
    return spark.read.csv(data_file, header=True)


def train_test_split(df, test_ratio=0.2):
    return df.randomSplit([1 - test_ratio, test_ratio])


def save_to_catalog(df, catalog_name, schema_name, table_name):
    df.write.mode("overwrite").saveAsTable(".".join([catalog_name, schema_name, table_name]))
