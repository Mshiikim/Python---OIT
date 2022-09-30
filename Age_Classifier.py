#MIS285 - 3-3 - Age Classifier
#Author: Michael Shiiki-Morris
#This program asks user for age and informs them if they are an infant, child, teenager, or an adult.

print('\tAge Classifier')
#User input
user_age = float(input('Enter your age: '))
#Checks value entered and displays output, error message displayed if outside range
if user_age > 0 and user_age =< 1:
	print('You are an infant')
elif user_age > 1 and user_age < 13:
	print('You are a child')
elif user_age >= 13 and user_age < 20:
	print('You are a teenager')
elif user_age >= 20 and user_age < 120:
	print('You are an adult')
else: 
	print('Age entered is outside the allowable input')