import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline ='') as election_data:
    votes = csv.reader(election_data, delimiter=',')
    next(votes)
    votes = tuple(votes)

    candidates = []
    candidate_index = 0
    vote_counts = []
    total = 0

for count in votes:
    total += 1
    if count[2] not in candidates:
        candidates.append(count[2])
        vote_counts.append(0)
    i = candidates.index(count[2])
    vote_counts[i] += 1
    
tally = ""
for index, member in enumerate(candidates):
    tally = tally + (f"{member}: {round(100*(vote_counts[index]/total),2)}% ({vote_counts[index]})\n")

max = 0
for index, amounts in enumerate(vote_counts):
    if amounts > max:
        max = amounts
        winner = candidates[index]  

string = f"Election Results\n\
-------------------------\n\
Total Votes: {total}\n\
-------------------------\n\
{tally}\
-------------------------\n\
Winner: {winner}"

print(string)
print(string,file = open('report.txt','a'))