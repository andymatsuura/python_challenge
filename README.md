# python_challenge
python hw wk3
PyBank Instructions
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
In addition, your final script should both print the analysis to the terminal and export a text file with the results.

PyPoll Instructions
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote

Your analysis should align with the following results:

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
In addition, your final script should both print the analysis to the terminal and export a text file with the results.

Used a variety of sources to help me with this homework. learning assistants helped me to zip my lists together in pypoll, to create optimized paths and correctly read csv, and how to write text files. 
https://www.pythontutorial.net/python-basics/python-write-text-file/ - learning assistant shared this with me and it was very helpful for outputting my text file. 
chatgpt helped me to identify an error in my code that was outputting a wrong value 
https://chat.openai.com/c/5e0c348e-4f7d-488a-988d-b9a534c174b2
it also helped me to write a function to iterate through my lists and find the differences in values in pybank. and understand how to use the index function to relate the correct month to the maximum monthly changes. 
https://chat.openai.com/c/dea97eba-4657-48e9-b2b5-8af180be1240
referenced this for the output of  percentage with 3 decimals 
https://www.askpython.com/python/string/print-format-3f
