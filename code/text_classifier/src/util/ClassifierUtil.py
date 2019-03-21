class ClassifierUtil:

    #estimationList: list of 1 and 0 to tell the class
    def generate_measures(self, realList, estimationList):
        if (len(realList) != len(estimationList)):
            raise Exception('real data and estimation have length mismatched')

            # results[0] : TP
            # results[1] : FN
            # results[2] : FP
            # results[3] : TN
            # results[4] : Precision
            # results[5] : Recall
            # results[6] : F_measure
            # results[7] : Accuracy

        results = [0, 0, 0, 0, 0, 0, 0, 0]

        for i in range(len(realList)):
            if realList[i] == 1 and estimationList[i] == 1:
                results[0] = results[0] + 1
            elif realList[i] == 1 and estimationList[i] == 0:
                results[1] = results[1] + 1
            elif realList[i] == 0 and estimationList[i] == 1:
                results[2] = results[2] + 1
            else:
                results[3] = results[3] + 1

        results[4] = 1.0 * results[0] / (results[0] + results[2])
        results[5] = 1.0 * results[0] / (results[0] + results[1])
        results[6] = 2.0 * results[0] / (2 * results[0] + results[2] + results[1])
        results[7] = 1.0 * (results[0] + results[3]) / (results[0] + results[1] + results[2] + results[3])

        return results