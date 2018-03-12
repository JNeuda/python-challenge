import os
import csv

budget1CSV= os.path.join('Resource','budget_data_1.csv')
budget2CSV= os.path.join('Resource','budget_data_2.csv')

# List to store data from excel files

total_months_list = []
total_revenue_list = []
avg_revenue = []
greatest_revenue = []
greatest_decrese = []

## total_revenue_list.remove()

with open(budget1CSV, 'r')as csvfile1:
    csvreader = csv.reader(csvfile1, delimiter=',')
    for row in csvreader:
        total_revenue_list.append(row[1])

with open(budget2CSV, 'r')as csvfile2:
    csvreader = csv.reader(csvfile2, delimiter=',')
    for row in csvreader:
        total_revenue_list.append(row[1])

# Cleansing List to get Revenue gained over the entire period
    # to change from string to int
        # total_revenue1 = [int(i) for i in total_revenue]

total_revenue_list.remove("Revenue")
total_revenue_list.remove("Revenue")
total_revenue_list = [int(i) for i in total_revenue_list]
total_revenue = sum(total_revenue_list)

# to change from string to int
# total_revenue1 = [int(i) for i in total_revenue]

print("Finanacial Analysis")
print("----------------------------")
print("Total Months: ")
print("Total Revenue: " + "$" + str(total_revenue))
print("Average Revenue Change: " + "$")
print("Greatest Increase in Revenue: ")
print("Greetest Decrease in Revenue: ")