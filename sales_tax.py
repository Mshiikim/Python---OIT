#This program calculates sales tax for the state and county for a retail company.
#MIS285 - 5.9 - Monthly Sales Tax
#Author: Michael Shiiki-Morris

sales = float(input('Enter the total monthly sales: $'))
county_tax = sales * .025
state_tax = sales * .05
total_tax = county_tax + state_tax
print('The total county tax liability for this month is: $', format(county_tax,'.2f'))
print('The total state tax liability for this month is: $', format(state_tax,'.2f'))
print('Your total tax liability for this month is: $', format(total_tax,'.2f'))