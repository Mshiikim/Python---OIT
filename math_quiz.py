#This program creates a simple math quiz to solve and will let you know if you answered correctly. 
#MIS285 - 5.11 - Math Quiz
#Author: Michael Shiiki-Morris

# Library needed for random number generator
import random

#Generage random numbers
number1 = random.randint(1,1000)
number2 = random.randint(1,1000)
answer = number1 + number2
print('\tMath Quiz')
user_guess = int(input(f'What is {number1} + {number2}?'))
if user_guess == answer:
    print("Congratulations, you are correct!")
else:
    print("Sorry, try again.")