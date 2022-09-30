#This program sums numbers entered from the user until a negative value is entered. 
#MIS285 - 4.8 - Sum of Numbers
#Author: Michael Shiiki-Morris

total = 0
input_num = 0
print('Sum of Numbers')
while input_num >= 0:
	input_num = float(input('Enter a positive number to continue, negative number to exit:'))
	if input_num > 0:
		total += input_num
print('The sum of the numbers entered is:', format(total,',.2f'))