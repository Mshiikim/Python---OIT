#This program will reformat a date entered in mm/dd/yyyy to month day, year.
#MIS285 - 8.3 - Date Printer
#Author: Michael Shiiki-Morris

def main():
    date_string = input('Enter a date in the format of mm/dd/yyyy: ')
    date_list = date_string.split('/') #use / from user input to split day, month, year
    month = date_list[0] #assign month value after split
    month = month_converter(month) #convert int to string with function
    day = date_list[1] #pull day date value from date_list
    year = date_list[2] #pull year date value from date_list
    output_date = month + ' ' + day + ',' + year #combine variables above to required output format
    print(output_date)
    
def month_converter(month): #convert value of month to string for output format. ?? for outside range allowed.
    if month == '1':
        month = 'January'
    elif month == '2':
        month = 'February'
    elif month == '3':
        month = 'March'
    elif month == '4':
        month = 'April'
    elif month == '5':
        month = 'May'
    elif month == '6':
        month = 'June'
    elif month == '7':
        month = 'July'
    elif month == '8':
        month = 'August'
    elif month == '9':
        month = 'September'
    elif month == '10':
        month = 'Octoboer'
    elif month == '11':
        month = 'November'
    elif month == '12':
        month = 'December'
    else:
        month = '??'
    return month

main()