#MIS285 - 3-11 - Book Club Points
#Author: Michael Shiiki-Morris
#This program will determine the number of points to award based on number of books purchased

print('\tBook Club Points')
# User input
books = int(input('Please enter the number of books purchased for this month:'))
# Checks books to determine output
if books < 2:
    print('You earned 0 points')
elif books >=2 and books < 4:
    print('You earned 5 points')
elif books >=4 and books < 6:
    print('You earned 15 points')
elif books >=6 and books < 8:
    print('You earned 30 points')
elif books >=8:
    print('You earned 60 points')