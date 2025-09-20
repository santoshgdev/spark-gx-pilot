import sys
print(sys.executable)
from datasets import load_dataset

import pyspark
import great_expectations


def main():
    df = load_dataset("DavidVivancos/MindBigData2022_MNIST_IN")
    training_dataset = df['train']
    training_df = training_dataset.to_spark()


if __name__ == "__main__":
    main()
