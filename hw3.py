#PyBank
#Part 1: Sum all revenue values and return a single total.

import os, csv
csvpath = os.path.join('budget_data_1.csv')

with open(csvpath) as f:
    readcsv = csv.reader(f, delimiter=',')

    #Part 1: Sum all revenue values and return a single total.
    total = 0
    for row in readcsv:
        total = total + int(row[1])
    print(total)  #Need to figure out how to exclude the header from the total

    #Part 2: Determine the total number of transactions in the data set.
