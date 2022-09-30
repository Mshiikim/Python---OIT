#MIS285 - 3-7 - Color Mixer
#Author: Michael Shiiki-Morris
#This program will calculate the result of mixing two primary colors

print('\t Color Mixer')
print('Enter two primary colors to mix (red, blue, yellow): ')
# User inputs
color_1 = input('First color: ')
color_2 = input('Second color: ')
# Check color_1 and color_2 and display output
if color_1 == 'red' and color_2 == 'blue' or color_1 == 'blue' and color_2 == 'red':
	print('You have made purple')
elif color_1 == 'red' and color_2 == 'yellow' or color_1 == 'yellow' and color_2 == 'red':
	print('You have made orange')
elif color_1 == 'blue' and color_2 == 'yellow' or color_1 == 'yellow' and color_2 == 'blue':
	print('You have made green')
else: 
	print('Error, cannot calculate basad on your input. Please try again.')