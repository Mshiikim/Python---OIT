#This program creates 100 random numbers and counts how many are even versus odd.
#MIS285 - 5.16 - Odd/Even Counter
#Author: Michael Shiiki-Morris

import random

def main():
    counter = 100
    even_count = 0
    odd_count = 0
    for counter in range(0,100,1):
        number = random.randint(1,10)
        if is_even(number):
            even_count += 1
        else:
            odd_count += 1
    print('Even numbers:',even_count)
    print('Odd numbers:',odd_count)

def is_even(number):
    #Checks number to see if it's even.
    if (number % 2) == 0:
        status = True
    else:
        status = False
    return status
main()