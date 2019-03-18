import csv
import numpy as np
import matplotlib.pyplot as plt


def createSizesGraph():
    # Initializing arrays here, later
    year = []
    teen_y = []
    twenties_y = []
    thirties_y = []
    fourties_y = []
    fifties_y = []
    sixties_y = []

    # Read from CSV file
    with open('OverdoseRatesByAges.csv') as csvfile:
        # CSV Reader, seperates values based on keys from the first row of csv
        reader = csv.DictReader(csvfile)
        for row in reader:
            year.append(row['Year'])  # Appending value from the row
            teen_y.append(float(row['15-24']))
            twenties_y.append(float(row['25-34']))
            thirties_y.append(float(row['35-44']))
            fourties_y.append(float(row['45-54']))
            fifties_y.append(float(row['55-64']))
            sixties_y.append(float(row['65 and over']))

    # evenly sampled time at 200ms intervals
    # X values, Y values, Decoration, Label for legend
    plt.plot(year, teen_y, 'g-^', label="15-24")
    plt.plot(year, twenties_y, 'b-o', label="25-34")
    plt.plot(year, thirties_y, 'r-s', label="35-44")
    plt.plot(year, fourties_y, 'm-+', label="45-54")
    plt.plot(year, fifties_y, 'y-D', label="55-64")
    plt.plot(year, sixties_y, 'k-p', label="65 and over")

    # Setting X Ticks and Labels
    plt.xticks(["2000", "2002", "2004", "2006", "2008",
                "2010", "2012", "2014", "2016"])  # Array
    plt.xlabel('Years')

    # Setting Y Ticks and Labels
    plt.yticks(np.arange(0, 18000, 2000))  # Array
    plt.ylabel('Number of Deaths')

    # Setting Chart Title
    plt.title("Drug Overdose Death Rates By Age")
    # Informing to include legend
    plt.legend()

    plt.show()


if __name__ == '__main__':
    createSizesGraph()
