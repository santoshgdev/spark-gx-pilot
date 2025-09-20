"""Main Module."""

import sys

import pyspark_huggingface  # noqa: F401

from spark_gx_pilot.utils.spark_utils import create_spark_session

print(sys.executable)


def main():
    """Entry point."""
    spark = create_spark_session()

    df = spark.read.format("huggingface").load("DavidVivancos/MindBigData2022_MNIST_IN")
    print(df.schema)


if __name__ == "__main__":
    main()
