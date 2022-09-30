#This program checks budget versus expenses and uses a loop for entering expenses. 
#After user is done entering expenses calculates over/under budget amount for user.
#MIS285 - 4.3 Budget Analysis
#Author: Michael Shiiki-Morris

total_expenses = 0
expense = 1
print('Budget Analysis')
budget = float(input('Please enter your monthly budget amount:'))
while expense != 0:
	expense = float(input('Please enter your expense amount (Enter 0 to end):'))
	total_expenses += expense
budget -= total_expenses
if budget > 0:
	print('You have $', format(budget, ',.2f'),'remaining in your budget this month.')
else:
	print('You are $', format(abs(budget), ',.2f'),'over your budget this month.')