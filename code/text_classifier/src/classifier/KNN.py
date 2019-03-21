from heapq import nlargest
from operator import itemgetter
from ..util import *

class KNN:
    def __init__(self, nn: int = 20):

        self.nn = nn
        self.clsUtil = ClassifierUtil

    #training_data is array of object {data: xxx, label: yyy}
    #training_data should be balanced classes (number of + is the same as number of -
    def run(self, training_data, testing_data, distance_function:callable, clean_text:bool = False):
            #run and return measures (precision, recall, f-measure

            distanceScores = []
            estimatedResult = []
            for test_item in testing_data:

                if clean_text == True:
                    test_item = pur
                # compute distance from test_item to all the training_data
                for train_item in training_data:
                    distance = distance_function(test_item, train_item)
                    myDistanceItem = {"distance": distance, "label": train_item.label}
                    distanceScores.append(myDistanceItem)

                #get k nearest neighbor
                nearestItems = nlargest(self.nn, distanceScores, key=itemgetter(1))
                positiveCount = 0
                negativeCount = 0

                # count the classes in the nearest list
                for item in nearestItems:
                    if item.label == 1:
                        positiveCount += 1
                    else:
                        negativeCount += 1

                # estimate class bases on comparison between number of positive and negative samples
                if positiveCount > negativeCount:
                    estimatedResult.append(1)
                else:
                    estimatedResult.append(0)

