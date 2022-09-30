#MIS285 - 2.11 Male and Female Percentages
#Author: Michael Shiiki-Morris
#This program will compute the percentage of males and females in the class.

print('This program will calculate the percentage of males and females registered for this class')
males = int(input('Enter the number of males registered for this class: '))
females = int(input('Enter the number of females registered for this class: '))
total = males + females
males = males / total
females = females / total
print('The percentage of males registered for this class is: ', format(males, '.0%'))
print('The percentage of females registered for this class is: ', format(females, '.0%'))
print('The total number of students registered for this class is: ', total)