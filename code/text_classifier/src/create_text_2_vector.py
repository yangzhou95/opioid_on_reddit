import argparse
from core.text_to_number import TextToNumber
import pandas as pd
import numpy as np

def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Tweet Cleaning and Creating Corpus and Dictionary files")
    parser.add_argument("-i",
                        "--input",
                        dest="inputs",
                        help="the path of the csv input file",
                        default='input/arule-text.csv')

    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    inputFile = args.inputs

    outputFile = inputFile[0:(len(inputFile)-4)] + '.vec.csv'

    textToNumber = TextToNumber()

    texts = []
    with open(inputFile) as f:
        for line in f:
            line = line.replace(',', ' ')
            texts.append(line)

    text_vecs = textToNumber.create_number_vector(texts, output_file=None, append_indicators=None,
                                                        padding_position='post', padding_maxlen=None)

    myMax = np.max(text_vecs)

    with open(outputFile, 'w') as f:
        for vec in text_vecs:
            items = []
            for i in vec:
                if i > 0:
                    items.append(i)
            line = ', '.join(str(x) for x in items)
            f.write(line + '\n')

    print('done, total unique terms:' + str(myMax))

