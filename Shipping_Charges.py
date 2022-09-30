#MIS285 - 3-13 - Shipping Charges
#Author: Michael Shiiki-Morris
#This program will determine shipping rates based on weight

print('FAST FREIGHT SHIPPING COMPANY')
print('\tShipping Charges')
# User input
weight = float(input('Enter the weight of the package in lbs:'))
# Checks weight to determine shipping charge
if weight > 0 and weight <= 2:
    print("\tIt'll cost you $1.50")
elif weight > 2 and weight <= 6:
    print("\tIt'll cost you $3.00")
elif weight > 6 and weight <= 10:
    print("\tIt'll cost you $4.00")
elif weight > 10:
    print("\tIt'll cost you $4.75")
else:
    print("\tIt can't be under zero...")