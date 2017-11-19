#PyBank
import os, csv
csvpath = os.path.join('budget_data_2.csv')

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


    #From reveiewing the data in Excel, the max value was on Sep-15 and min value was on 08-14
    #print(revenue_list)
    #print(transaction_list)
    print(" ")
    print("Financial Summary")
    print("----------------------------------------")
    print("Total Revenue: ", revtotal)
    print("Minimin Revenue: ", min(revenue_list))
    print("Maximum Revneue: ", max(revenue_list))
    print("Total Number of Transactions: ", len(transaction_list))
    print("Average: ", float(int(revtotal)/int(len(transaction_list))))
    print("Month and year of the maximum revenue: ", transaction_list[revenue_list.index(max(revenue_list))])
    print("Month and year of the minimim revenue: ", transaction_list[revenue_list.index(min(revenue_list))])

    #Output for "budget_data_1"
    #     Financial Summary
    # ----------------------------------------
    # Total Revenue:  18971412
    # Minimin Revenue:  -1172384
    # Maximum Revneue:  977084
    # Total Number of Transactions:  41
    # Average:  462717.3658536585
    # Month and year of the maximum revenue:  Dec-13
    # Month and year of the minimim revenue:  Aug-14

    #Output for "budget_data_2"
    #     Financial Summary
    # ----------------------------------------
    # Total Revenue:  36973911
    # Minimin Revenue:  -1063151
    # Maximum Revneue:  998347
    # Total Number of Transactions:  86
    # Average:  429929.1976744186
    # Month and year of the maximum revenue:  Dec-2013
    # Month and year of the minimim revenue:  Sep-2010
