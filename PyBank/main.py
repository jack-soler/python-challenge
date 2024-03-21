import csv
import os

# Construct the path to the CSV file
csv_file = os.path.join("/Users", "jacksoler1", "Bootcamp Modules", "python-challenge", "PyBank", "Resources", "budget_data.csv")

# Open the CSV file
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    csv_title = next(reader) # Saves csv title and skips that row
    header_fields = next(reader)  # Saves header fields and skips the header row

    greatest_increase_index = -1
    profit = []
    dates = [] # declares empty list
    profit_differences = []
    greatest_increase = 0
    greatest_decrease = 0
    for row in reader: # for each row in the file
        dates.append(row[0])  # Date is in the first column of the CSV
        profit.append(row[1]) # Profit is in second column
    profit = [int(value) for value in profit]
    for i in range(1, len(profit)):
        difference = profit[i] - profit[i - 1]  # Calculate the difference between current profit and the one above it
        profit_differences.append(difference)  # Append the difference to the profit_differences list
        if profit[i] - profit[i - 1] > greatest_increase:
            greatest_increase = profit[i] - profit[i - 1]
            greatest_increase_index = i
        if profit[i] - profit[i - 1] < greatest_decrease:
            greatest_decrease = profit[i] - profit[i - 1]
            greatest_decrease_index = i
            


# Count the number of unique months
total_months = len(dates)
total_profit = sum(int(profit) for profit in profit)
average_difference = sum(int(profit_differences) for profit_differences in profit_differences)/len(profit_differences)
average_difference = round(average_difference, 2)

print("Financial Analysis")
print("Total Months:", total_months)
print("Total: $", total_profit)
print("Average Change: $",average_difference)
print(f'Greatest Increase in Profits: {dates[greatest_increase_index]}, (${greatest_increase})')
print(f'Greatest Decrease in Profits: {dates[greatest_decrease_index]}, (${greatest_decrease})')