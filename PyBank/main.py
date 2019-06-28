import os
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline ='') as profit_data:
    profit_data = csv.reader(profit_data, delimiter=',')
    next(profit_data)
    list_data = tuple(profit_data)

total_months = 0
total = 0
total_change = 0
pre_row = 0
max_profit = 0
max_loss = 0

for row in list_data:
    total_months = total_months + 1
    rev = int(row[1])
    total = total + rev
    change = rev-pre_row
    if change > max_profit:
        max_profit = change
        profit_month = row[0]
    if change < max_loss:
        max_loss = change
        loss_month = row[0]
    total_change = total_change + change
    pre_row = rev
total_change = total_change - int(list_data[0][1])
print(total_change)
average_change = total_change/(total_months-1)

string = (f"Financial Analysis\n\
----------------------------\n\
Total Months: {total_months}\n\
Total: {total}\n\
Average Change: {average_change}\n\
Greatest Increase in Profits: {profit_month} (${max_profit})\n\
Greatest Decrease in Profits: {loss_month} (${max_loss})")

print(string)
print(string,file = open('report.txt','a'))