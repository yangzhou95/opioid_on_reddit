import csv


with open('data/items.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    transactionId = "1"
    transactionItems = []
    transactionItems.append(transactionId)

    transactions = []
    for row in reader:
        if row[0] == "label":
            continue

        if row[1] == transactionId:
            transactionItems.append(row[2])
        else:
            transactions.append(transactionItems)
            transactionId = row[1]
            transactionItems = [transactionId]

with open('data/transactions.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for trans in transactions:
        writer.writerow(trans)
