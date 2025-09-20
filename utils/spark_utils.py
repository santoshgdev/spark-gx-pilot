"""Module with spark related functions."""

from pyspark.sql import SparkSession


def create_spark_session() -> SparkSession:
    """Return a local spark session."""
    return (
        SparkSession.builder.appName("Datasets to Spark DF")
        .master("local[*]")  # Use local machine with all available cores
        .getOrCreate()
    )
