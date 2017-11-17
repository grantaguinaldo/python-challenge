#PyBank
#Part 1: Sum all revenue values and return a single total.

import os, csv
csvpath = os.path.join('budget_data_1.csv')

with open(csvpath) as f:
    readcsv = csv.reader(f, delimiter=',')

    #Part 1: Sum all revenue values and return a single total.
    revtotal = 0
    for row in readcsv:
        revtotal = revtotal + int(row[1])
    print(total)  #Need to figure out how to exclude the header from the total

    #Part 2: Determine the total number of transactions in the data set.
    monthtotal = 0
    for row in readcsv:
        monthtotal += 1
    print(monthtotal - 1)


    #Part X: Print the summary table.
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: ")
    print("Total Revenue: ")
    print("Average Revenue Change: ")
    print("Greatest Increse in Revenue: ")
    print("Greatest Decrese in Revenue: ")
