#Import Modules
import os
import csv
from pathlib import Path

#path to find csv location, learning assistant showed me how to path like this
pybank_csv = "Resources/budget_data.csv"

#create variables for the output. starting with empty lists 
total_months = []
net_total = []
monthly_change = []

#opening and reading csv
with open(pybank_csv, newline="", encoding="utf-8") as csv_budget:
    csvreader = csv.reader(csv_budget, delimiter=",")

#skip the header
    csv_header = next(csvreader)

#iterate through the csv file and add values to the list using .append method
    for row in csvreader:

        total_months.append(row[0])
        net_total.append(int(row[1]))

#use a loop to find the monthly change, linked chatgpt code assistance, append monthly_change value
    for i in range(len(net_total)-1):
        monthly_change.append(net_total[i+1]-net_total[i])

#min and max values of monthly change
max_monthly_change = max(monthly_change)
min_monthly_change = min(monthly_change)

#month of min and max monthly change found with index. added +1 because it was outputting the month prior without it.
max_month = monthly_change.index(max(monthly_change))+1
min_month = monthly_change.index(min(monthly_change))+1

#print results, trying to make it match the example sheet with --- round and dollar signs
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_month]} (${max_monthly_change})")
print(f"Greatest Decrease in Profits: {total_months[min_month]} (${min_monthly_change})")

# output txt file, included link for how-to from LA
pybank_analysis = "analysis/Financial_Analysis.txt"

#write into text file, \n because it didn't otherwise separate the codes.
with open(pybank_analysis, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(net_total)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_month]} (${max_monthly_change})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[min_month]} (${min_monthly_change})")
