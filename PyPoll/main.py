import os
import csv

election1CSV= os.path.join('Resource','election_data_1.csv')

# List to store data from excel files

total_votes = []

with open(election1CSV, 'r')as csvfile1:
    csvreader = csv.reader(csvfile1, delimiter=',')
    next(csvreader)
    for row in csvreader:
        total_votes.append(row[2])

# used set(total_votes) to get unique candidates in data

c_set = set(total_votes)
c_list = list(c_set) # used to get candidate index and name

# Calculate Total Votes

total_votes_count = len(total_votes)

#Calculate Total Votes per Candidate

candidate_1_votes = total_votes.count(c_list[0])
candidate_2_votes = total_votes.count(c_list[1])
candidate_3_votes = total_votes.count(c_list[2])
candidate_4_votes = total_votes.count(c_list[3])

# Variable for Candidate to Print

candidate_1 = c_list[0]
candidate_2 = c_list[1]
candidate_3 = c_list[2]
candidate_4 = c_list[3]

# Calculate percentage % candidate counts

c1_percent = (candidate_1_votes / total_votes_count)*100
c2_percent = (candidate_2_votes / total_votes_count)*100
c3_percent = (candidate_3_votes / total_votes_count)*100
c4_percent = (candidate_4_votes / total_votes_count)*100

# Determine Winner

if candidate_1_votes > candidate_2_votes and candidate_1_votes > candidate_3_votes and candidate_1_votes > candidate_4_votes:
    winner = candidate_1
elif candidate_3_votes > candidate_1_votes and candidate_3_votes > candidate_2_votes and candidate_3_votes > candidate_4_votes:
    winner = candidate_3
elif candidate_2_votes > candidate_1_votes and candidate_2_votes > candidate_3_votes and candidate_2_votes > candidate_4_votes:
    winner = candidate_2
else: 
    winner = candidate_4

# Print out Results

print("Election Results\n")
print("----------------------------\n")
print("Total Votes: " + str(total_votes_count))
print("\n----------------------------\n")
print(candidate_1 + ": " + str(c1_percent) + "% " + "(" + str(candidate_1_votes) +")\n")
print(candidate_2 + ": " + str(c2_percent) + "% " + "(" + str(candidate_2_votes) +")\n")
print(candidate_3 + ": " + str(c3_percent) + "% " + "(" + str(candidate_3_votes) +")\n")
print(candidate_4 + ": " + str(c4_percent) + "% " + "(" + str(candidate_4_votes) +")\n")
print("----------------------------\n")
print("Winner: " + winner + "\n")
print("----------------------------\n")

# Print out to a textfile

output_file = open("outputPyPoll.txt","w")

output_file.write("Election Results\n")
output_file.write("----------------------------\n")
output_file.write("Total Votes: " + str(total_votes_count))
output_file.write("\n----------------------------\n")
output_file.write(candidate_1 + ": " + str(c1_percent) + "% " + "(" + str(candidate_1_votes) +")\n")
output_file.write(candidate_2 + ": " + str(c2_percent) + "% " + "(" + str(candidate_2_votes) +")\n")
output_file.write(candidate_3 + ": " + str(c3_percent) + "% " + "(" + str(candidate_3_votes) +")\n")
output_file.write(candidate_4 + ": " + str(c4_percent) + "% " + "(" + str(candidate_4_votes) +")\n")
output_file.write("----------------------------\n")
output_file.write("Winner: " + winner + "\n")
output_file.write("----------------------------\n")