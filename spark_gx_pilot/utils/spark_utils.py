"""Module with spark related functions."""

import os
import sys

from pyspark.sql import SparkSession


def create_spark_session() -> SparkSession:
    """Return a local spark session."""
    # Explicitly set the python executable for pyspark to use.
    # This helps avoid 'java gateway exited' errors in some environments.
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
    spark = (
        SparkSession.builder.appName("Datasets to Spark DF")
        .master("local[*]")  # Use local machine with all available cores
        .getOrCreate()
    )

    return spark
