#the program read a big file with a certain number of lines and produce output.
import pandas as pd
import argparse
import logging
from sklearn.model_selection import train_test_split

def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Extract a part of file for testing purpose")
    parser.add_argument("-i",
                        "--input-file",
                        dest="input",
                        help="File name of the input csv file",
                        default=None)

    parser.add_argument("-o",
                        "--output-file",
                        dest="output",
                        help="Output csv file",
                        default="output.csv")

    parser.add_argument("-c",
                        "--count",
                        dest="count",
                        help="Line count to be extracted",
                        default=2000)

    parser.add_argument("-t",
                        "--test-size",
                        dest="testSize",
                        help="Percentage of test size",
                        default=None)

    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    fileInput = args.input
    fileOutput = args.output
    count = int(args.count)
    testSize = args.testSize

    fp = pd.read_csv(fileInput, sep=',', header=None, chunksize=count)

    if ".csv" not in fileOutput:
        fileOutput = fileOutput + '.csv'

    for line in fp:
        line.to_csv(fileOutput, index=False, header=None)

        if testSize is not None:
            traindf, testdf = train_test_split(line, test_size=float(testSize))
            traindf.to_csv('train.csv', index=False, header=None)
            testdf.to_csv('test.csv', index=False, header=None)

        break



    logging.warning("Done")
