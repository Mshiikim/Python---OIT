#This program calculates the monthly and yearly cost of owning an automobile.
#MIS285 - 5.4 - Automobile Costs
#Author: Michael Shiiki-Morris

loan = float(input("Enter your monthly loan payment:"))
insurance = float(input("Enter your monthly insurance payment:"))
gas = float(input("Enter how much you spend on gas per month:"))
oil = float(input("Enter how much you spend on oil per month:"))
tires = float(input("Enter how much you spend on tires per month:"))
maintenance = float(input("Enter how much you spend on vehicle maintenance per month:"))
total_monthly = loan + insurance + gas + oil + tires + maintenance
total_yearly = total_monthly * 12
print('The total monthly cost to own your automobile is $:', format(total_monthly,'.2f'))
print('The total yearly cost to own your automobile is $:', format(total_yearly,'.2f'))