#MIS285 - 2.3 Land Calculation
#Author: Michael Shiiki-Morris
#This program converts total square feet of a tract of land into acres.

print('This program converts square feet of a tract of land into acres.')
tract_feet = int(input('Enter the total square feet of the tract of land: '))
acres = tract_feet / 43560 
print('Total acres of the tract of land is: ', format(acres, '.2f'))