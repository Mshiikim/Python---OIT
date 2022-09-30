#This program calculates how much insurance coverage a property owner should have. 
#MIS285 - 5.3 - How Much Insurance?
#Author: Michael Shiiki-Morris

amount = float(input("Enter the replacement cost of the building you want to insure:"))
amount *= .8
print('You should have at least $', format(amount,'.2f'), 'of insurance coverage.')