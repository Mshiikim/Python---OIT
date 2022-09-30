#MIS285 - 2.7 Miles-per-Gallon
#Author: Michael Shiiki-Morris
#This program computes a car's miles-per-gallon

print("This program will calculate a car's miles-per-gallon for you")
#User Inputs
miles_driven = int(input('Please enter the number of miles driven : '))
gallons_gas = int(input('Please enter the number of gallons of gas used : '))
#Calculations
average = miles_driven / gallons_gas
#Output
print('The vehicle averaged', format(average, '.2f'), 'miles-per-gallon.') 