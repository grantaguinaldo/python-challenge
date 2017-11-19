import os, csv

filepath = os.path.join("election_data_1.csv")

with open(filepath) as f:
    readcsv = csv.reader(f,delimiter=",")
    next(readcsv)

    #Count the number of voters that cast votes.
    num_votes_cast = sum([1 for row in readcsv])
    print(num_votes_cast)

    #Return a list of unique canidates.
    canidate_list_all = [row[2] for row in readcsv]
    canidate_list_unique = []
    for i in canidate_list_all:
        if i not in canidate_list_unique:
            canidate_list_unique.append(i)
    #Print(canidate_list_unique) #['Vestal', 'Torres', 'Seth', 'Cordin']

    #Determine the number of votes for each canidate.
    votes_vestal = 0
    votes_torres = 0
    votes_seth = 0
    votes_cordin = 0
    votes_total = 0

    for row in readcsv:
        if row[2] == "Vestal":
            votes_vestal += 1

        elif row[2] == "Torres":
            votes_torres += 1

        elif row[2] == "Seth":
            votes_seth += 1
        else:
            votes_cordin += 1

    print(votes_vestal)
    print(votes_torres)
    print(votes_seth)
    print(votes_cordin)
    print(votes_seth + votes_torres + votes_cordin + votes_vestal)
