#import the necessary modules/libraries
import os
import csv

#creating an object out of the CSV file   
budget_data = os.path.join("/Users/georgialeigh/Desktop/PythonHomework/budget_data.csv")

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#open and read csv file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#read the header row
    csv_header = next(csvreader)

#read the first row (to track the changes properly)
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
#going through each row of data after the header & first row 
    for row in csvreader:
        
# keep track of the dates
        dates.append(row[0])
        
# calculate the change then add it to the list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
#total number of months
        total_months += 1

#total net amount of "Profit/Losses over entire period"
        total_pl = total_pl + int(row[1])

#greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

#greatest decrease in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

#average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    

#display information
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#export to .txt file
output = open("output_budget.txt", "w")

line1 = "Financial Analysis"
line2 = "------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
