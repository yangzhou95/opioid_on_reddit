'''
This file will format csv files that need to be SVM Classified.

File Format:

<Label><Tab><Text>

'''



def reformat(filePath, newFileName):
    newFile = open(newFileName,'w')
    with open(filePath, 'r') as oldFile:
        for line in oldFile:
            line = line.split(',')
            newLine = line[1].replace('\n','') + '\t' + line[0].replace('\n','') + '\n'
            #print(newLine)
            newFile.write(newLine)



if (__name__ == "__main__"):

    old_train_file = '/home/jf/PycharmProjects/harvey-classifier/r/data/train-rescue-500.csv'
    old_test_file = '/home/jf/PycharmProjects/harvey-classifier/r/data/test-rescue-500.csv'

    new_train_file = '/home/jf/PycharmProjects/harvey-classifier/r/data/new-train-rescue-500.txt'
    new_test_file = '/home/jf/PycharmProjects/harvey-classifier/r/data/new-test-rescue-500.txt'

    print("Reformatting Files..")
    reformat(old_test_file, new_test_file)
    reformat(old_train_file, new_train_file)
    print("Reformat Complete.")

