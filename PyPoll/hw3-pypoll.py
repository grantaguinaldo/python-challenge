#Standard Imports
import os, csv

#Directory of the CSV file.
filepath = os.path.join("election_data_1.csv")

#Open the CSV file and read the data while skipping the first row (that contains the headers)
with open(filepath) as f:
    readcsv = csv.reader(f,delimiter=",")

    next(readcsv)
    #Count the number of voters that cast votes.
    total_votes_cast = sum([1 for row in readcsv])
    print("Number of votes casted: ", total_votes_cast)

    f.seek(0)
    next(readcsv)
    #Return a list of unique canidates.
    canidate_list_all = [row[2] for row in readcsv]
    canidate_list_unique = []
    for i in canidate_list_all:
        if i not in canidate_list_unique:
            canidate_list_unique.append(i)
    print(canidate_list_unique) #['Vestal', 'Torres', 'Seth', 'Cordin']

    f.seek(0)
    next(readcsv)
    #Determine the number of votes for each canidate by summing.
    votes_vestal = 0
    votes_torres = 0
    votes_seth = 0
    votes_cordin = 0

    for row in readcsv:
        if row[2] == "Vestal":
            votes_vestal += 1

        elif row[2] == "Torres":
            votes_torres += 1

        elif row[2] == "Seth":
            votes_seth += 1
        else:
            votes_cordin += 1

    #Determine the percentages for each canidate.
    pct_votes_vestal = (float(votes_vestal/total_votes_cast)) * 100
    pct_votes_torres = (float(votes_torres/total_votes_cast)) * 100
    pct_votes_seth = (float(votes_seth/total_votes_cast)) * 100
    pct_votes_cordin = (float(votes_cordin/total_votes_cast)) * 100

    results_dict = {'cordin': votes_cordin, 'seth': votes_seth, 'torres': votes_torres, 'vestal': votes_vestal}

    print("Seth Received " , pct_votes_seth, "%")
    print(pct_votes_cordin , "%")
    print(pct_votes_torres, "%")
    print(pct_votes_vestal, "%")

    print("---")
    print(votes_seth)
    print(votes_cordin)
    print(votes_torres)
    print(votes_vestal)



    #Notes.
    #Create dictionary with results.
    #Send individual results to a list or dictionary and pair with the canidates.
    #Figure out how to format the data so that it shows up like the example.
    #Figure out how to get all lists in a the for loops to print.
