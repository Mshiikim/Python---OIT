#This program calculates 6 months of weight loss by cutting 500 calories per month. 
#MIS285 - 4.11 - Weight Loss
#Author: Michael Shiiki-Morris

counter = 0 #Counter for months
print('Weight Loss Calculator')
weight = float(input('Please enter your weight:'))
for counter in range(0,6,1):
	weight -= 4
	counter += 1
	print('After',counter,'months your weight will be:',format(weight,'.2f'))