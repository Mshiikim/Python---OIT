#MIS285 - 3-1, Day of the Week
#Author: Michael Shiiki-Morris
#This program asks user for a number and converts it to a day of the week.

print('\tDay of the Week')
#User input / variables
user_number = int(input('Enter a number between 1 and 7:'))
#Checks value entered and displays output, error message displayed if outside range
if user_number == 1:
	print('Monday')
elif user_number == 2:
	print('Tuesday')
elif user_number == 3:
	print('Wednesday')
elif user_number == 4:
	print('Thursday')
elif user_number == 5:
	print('Friday')
elif user_number == 6:
	print('Saturday')
elif user_number == 7:
	print('Sunday')
else:
    print('Sorry, that number is outside the range allowed.')