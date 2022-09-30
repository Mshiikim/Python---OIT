#This program displays calories burned per minute at intervals of 5 minutes up to 30 minutes.
#MIS285 - 4.2 Calories Burned
#Author: Michael Shiiki-Morris


burnt = 0
print('Calories burned running on a treadmill')
for calories in range(10, 31, 5):
    burnt = calories * 4.2;
    print('Calories burned at', calories, 'minutes:', burnt)