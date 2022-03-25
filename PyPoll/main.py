# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

votes_for_candidates = []

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    # print(header)

    second_row = next(csvreader)
    # print(second_row)

    # Loop through looking for the video
    for row in csvreader:
        candidate = row[2]
        votes_for_candidates.append(candidate)

# print(votes_for_candidates)
total_votes = len(votes_for_candidates)
print(f"The total votes are {total_votes}")

election_results = {}

# election_results = {'Charles Casper Stockham': 5, 'Diana DeGette': 5, 'Raymon Anthony Doane': 5}

for i in votes_for_candidates:
    if i in election_results.keys():
        election_results[i] = 1 + election_results[i]
    else:
        election_results[i] = 1

print(election_results)