#This program calculates rainfall statistics for a year based on values entered by the user. 
#MIS285 - 7.3 - Rainfall Statistics
#Author: Michael Shiiki-Morris

months = 12

def main():
    index = 0
    rainlist = [0]*months
    total = 0
    while index < months:
        print('Enter the total rainfall for month',index + 1,':')
        rainlist[index] = float(input())
        index += 1
    for value in rainlist:
        total += value
    print ('The total rainfall for the year is', format(total,'.2f'),'inches')
    average = total / len(rainlist)
    print ('The average monthly rainfall is ', format(average,'.2f'),'inches')
    min_rain = min(rainlist)
    min_months = []
    counter = 0
    for value in rainlist:
        counter += 1
        if value == min_rain:
            min_months.append(counter)
    print ('The month(s) with the lowest rainfall are month(s)', min_months)
    max_rain = max(rainlist)
    max_months = []
    counter = 0
    for value in rainlist:
        counter += 1
        if value == max_rain:
            max_months.append(counter)
    print ('The month(s) with the highest rainfall are month(s)', max_months)
main()