import csv

print("Script started")

# Initialize variables
total_months = 0
net_total = 0
previous_profit = None
profit_change = []
greatest_increase = {"date": "", "profit": 0}
greatest_decrease = {"date": "", "profit": 0}

# Open and read the CSV file
with open('/Users/NP/Documents/python-challenge/PyBank/Resources/budget_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row

    for row in reader:
        date = row[0]
        profit = int(row[1])

        # Increment the total months and net total profit
        total_months += 1
        net_total += profit

        # Calculate the change in profit from the previous month
        if previous_profit is not None:
            change = profit - previous_profit
            profit_change.append(change)

            # Check if this change is a new greatest increase or decrease
            if change > greatest_increase["profit"]:
                greatest_increase = {"date": date, "profit": change}
            elif change < greatest_decrease["profit"]:
                greatest_decrease = {"date": date, "profit": change}

        previous_profit = profit

# Calculate the average change in profit
average_change = sum(profit_change) / len(profit_change)

# Prepare the financial analysis
results = [
    "Financial Analysis",
    "----------------------------",
    f"Total Months: {total_months}",
    f"Total: ${net_total}",
    f"Average Change: ${average_change:.2f}",
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['profit']})",
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['profit']})"
]

# Print the financial analysis to the terminal
for line in results:
    print(line)

# Write the financial analysis to a text file
with open('/Users/NP/Documents/python-challenge/PyBank/analysis/financial_analysis.txt', 'w') as file:
    for line in results:
        file.write(line + "\n")

print("Script finished")