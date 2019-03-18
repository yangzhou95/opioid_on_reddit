import json
import csv
from netgraphjson import *


def convertCSV():
    file = NetGraphJson()
    names = []
    # Read from CSV file
    with open('out.csv') as csvfile:
        reader = csv.reader(csvfile)
        line = 0
        for row in reader:
            # Get the number of columns in the row
            columns = len(row) - 1
            for col in range(0, columns):
                # Col 0 and row 0 are Node Names
                if line == 0 and col != 0:
                    file.nodes.append(Nodes(row[col]))
                    names.append(row[col])
                else:
                    # only add link if column/row intersection is greater than  0
                    if col > 0 and int(row[col]) > 0 and col != 0:
                        file.links.append(
                            Links(row[0], names[col - 1], int(row[col])))
            line += 1
            # write the data to a file.
    with open('netgraphjson.json', 'w') as outfile:
        json.dump(file.reprJSON(),  outfile, cls=ComplexEncoder, indent=4)


if __name__ == '__main__':
    convertCSV()
