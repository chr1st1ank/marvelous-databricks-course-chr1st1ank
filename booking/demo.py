"""Just a minimal test file to check if the environment is working."""
# Databricks notebook source

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
df = spark.read.table("samples.nyctaxi.trips")
df.show(5)

# COMMAND ----------

print("Test")
