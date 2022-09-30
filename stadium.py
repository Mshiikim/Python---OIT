#This program calculates the total sales for three seating assignments for a stadium.
#MIS285 - 5.7 - Stadium Seating
#Author: Michael Shiiki-Morris

a_seats = float(input("Enter the number of Class A seat tickets sold:"))
a_seats *= 20
b_seats = float(input("Enter the number of Class B seat tickets sold:"))
b_seats *= 15
c_seats = float(input("Enter the number of Class C seat tickets sold:"))
c_seats *= 10
sales = a_seats + b_seats + c_seats
print("Total income from ticket sales: $", format(sales,'.2f'))
