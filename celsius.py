#This program provides a table showing Celsius temperatures 0 to 20 and the conversions to Fahrenheit.
#MIS285 - 4.6 - Celsius to Fahrenheit Table
#Author: Michael Shiiki-Morris

celsius = 0
print('Celsius to Fahrenheit')
for celsius in range(0, 21, 1):
	fahrenheit = (celsius * 1.8) + 32
	print(celsius,'C° \t', format(fahrenheit,'.1f'),'F°')