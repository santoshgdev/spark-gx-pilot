import sys


from spark_gx_pilot.utils.spark_utils import create_spark_session

print(sys.executable)


def main():
    spark = create_spark_session()

    df = spark.read.format("huggingface").load("DavidVivancos/MindBigData2022_MNIST_IN")


if __name__ == "__main__":
    main()
