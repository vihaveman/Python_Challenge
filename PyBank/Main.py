#PyBank Code Script

import csv

# Choosing input file path
input_file = "PyBank/Resources/budget_data.csv"

# Defining the output file path for results
output_file = "PyBank/Resources/Analysis"

# Declaring variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change = 0
profit_loss_changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', 999999999999999]

# Opening the input CSV file
with open(input_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Retriving data below header row
    header = next(csv_reader)
    
    # Looping through the data rows
    for row in csv_reader:
        
        # Calculating total number of months
        total_months += 1
        
        # Calculating profit/losses net total 
        total_profit_loss += int(row[1])
        
        # Calculating profit/losses changes
        if previous_profit_loss != 0:
            profit_loss_change = int(row[1]) - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
        
        # Updating previous profit/loss value
        previous_profit_loss = int(row[1])
        
        # Determining greatest increase in profits
        if profit_loss_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss_change
        
        # Determining greatest decrease in profits
        if profit_loss_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss_change

# Calculating average change in profit/losses
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Formating results as a string
results = f"""
Financial Analysis\n
----------------------------\n
Total Months: {total_months}\n
Total: ${total_profit_loss}\n
Average Change: ${average_change:.2f}\n
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n
"""

# Printing results to the terminal
print(results)

# Writing the results to a text file
with open(output_file, "w") as text_file:
    text_file.write(results)
