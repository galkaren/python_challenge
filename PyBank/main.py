import os
import csv
csvpath = os.path.join('..', 'Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",") 
    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header

    # Start the count here to avoid counting the header.
    # Each month only appears once in each year. That automatically makes each month unique. Therefore, to find the total number of months, you just need to do a count.
    count = 0
    profit = 0
    loss = 0
    for row in csvreader:
        print(row)
        # This count += 1 will allow the loop to move to the next row
        count += 1
        if int(row[1]) > 0: # access row 1 and column 2
            profit += int(row[1])
        else:
            loss -= int(row[1])
    # net profit
    net_profit = profit - loss
    print("Total Months:", count)
    print("Total:", net_profit)


print("------Change over time--------")
greatest_increase_profit = 0
greatest_increase_profit_rows = None
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",") 
    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    previous = next(csvreader)[1]
    change = 0
    for row in csvreader:
        diff = int(row[1]) - int(previous)
        if diff > greatest_increase_profit:
            greatest_increase_profit = diff
            greatest_increase_profit_rows = row
        previous = int(row[1])
        print("Diff", diff)
        change += diff
    avg_change = change/(count - 1)
    print("Average  Change:", avg_change)
    print("Greatest increase in profit:", greatest_increase_profit_rows[0], "("+ str(greatest_increase_profit) +")")


# print("------Greatest Increase in Profit--------")
# with open(csvpath) as csvfile:
#     csvreader=csv.reader(csvfile, delimiter=",") 
#     print(csvreader)

#     # Read the header row first (skip this step if there is no header)
#     csv_header = next(csvreader)
#     profits = []
#     losses = []
#     for row in csvreader:
#         current_val = int(row[1])
#         if current_val > 0:
#             profits.append(row)
#         else:
#             losses.append(row)
    
#     greatest_diff = int(profits[1][1]) - int(profits[0][1])
#     previous = int(profits[1][1])
#     greatest_diff_row = profits[0]
#     for row in profits[1:]:
#         diff = int(row[1]) - int(previous)
#         if greatest_diff < diff:
#             greatest_diff = diff
#             greatest_diff_row = row[1]
#         previous = int(row[1])
#     print("greatest", row)