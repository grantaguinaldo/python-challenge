#PyBank
import os, csv
csvpath = os.path.join('budget_data_1.csv')

with open(csvpath) as f:
    readcsv = csv.reader(f, delimiter=',')

    next(readcsv)

    revenue_list = []
    transaction_list = []

    revtotal = 0

    for row in readcsv:
        revtotal = revtotal + int(row[1])
        revenue_list.append(row[1])
        transaction_list.append(row[0])

    print(revenue_list)
    print(transaction_list)

    print("Financial Summary")
    print("----------------------------------------------------------")
    print("Total Revenue: ", revtotal)
    print("Minimin Revenue: ", min(revenue_list))
    print("Maximum Revneue: ", max(revenue_list))
    print("Total Number of Transactions: ", len(transaction_list))
    print("Average: ", float(int(revtotal)/int(len(transaction_list))))

    #Need to find maximum value from revenue list and return the index.
    #Then I need to pull out the corresponding month in the transaction list at the same index.

    print(transaction_list[revenue_list.index(max(revenue_list))])
