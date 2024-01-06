#import modules, named this main2 so I don't get confused with pybank main file
import os
import csv
from pathlib import Path

#path to find csv location
pypoll_csv = "Resources/election_data.csv"

#create variables for the  output. starting with empty lists for each candidate
total_votes = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0

#opening and reading csv
with open(pypoll_csv, newline="", encoding="utf-8") as votes_csv:
    csvreader = csv.reader(votes_csv, delimiter=",")

#skipping header 
    csv_header = next(csvreader)

#iterate through the csv file 
    for row in csvreader:

#add each vote to the total votes list
        total_votes +=1

#add up the vote totals for each candidate with an if statement
        if row[2] == "Charles Casper Stockham":
            stockham_votes +=1
        elif row[2] == "Diana DeGette":
            degette_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            doane_votes +=1

#created a list for the candidates name and their vote count. initally tried them as dictionaries with {} but it didn't output correctly 
#s/o to chatgpt for identifying this mistake
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
candidate_votes = [stockham_votes, degette_votes, doane_votes]

#zipped lists together into dictionary to attribute the highest vote count to the persons name
combined_dictionary = dict(zip(candidates, candidate_votes))

#max function to find the winner
winner = max(combined_dictionary, key=combined_dictionary.get)

#finding percentages like the analysis
stockham_percent = stockham_votes/total_votes * 100
degette_percent = degette_votes/total_votes * 100
doane_percent = doane_votes/total_votes * 100

#print summary for terminal. needed to look up the :.3f to make the percentage 3 digits
print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")
print(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
print(f"Diana Degette: {degette_percent:.3f}% ({degette_votes})")
print(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
print("-----------------------")
print(f"Winner: {winner}")

#output text file
pypoll_analysis = "analysis/Election_Results.txt"           

#write text file with \n to separate lines
with open(pypoll_analysis, "w") as file: 
    file.write("Election Results")
    file.write("\n")
    file.write("-----------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write("-----------------------")
    file.write(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
    file.write("\n")
    file.write(f"Diana Degette: {degette_percent:.3f}% ({degette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
    file.write("\n")
    file.write("-----------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")



