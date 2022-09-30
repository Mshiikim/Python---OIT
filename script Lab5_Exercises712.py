#This program will display all prime numbers below a user entered value
#MIS285 - 7.12 - Prime Number Generation
#Author: Michael Shiiki-Morris

def main():
    #user input
    user_int = int(input('Enter an integer greater than 1:'))
    #counter for value - starts at 1 to adjust for 0 index
    value = 1
    #loop for list creation
    my_list = []
    for index in range(2, user_int+1): 
        value += 1
        my_list.append(value)
    #loop for running prime_check function on each element in the list
    for index in range(len(my_list)):
        element = my_list[index] #assign current index value
        prime_check(element)
        
#function to check if element is a prime number
def prime_check(element):
    flag = False #flag for prime check
    for index in range (2, element):
        if (element % index) == 0: #check if element is prime, if true break loop
            flag = True
            break
    if flag:  #check flag and output message
        print(element,' is not a prime number.')
    else:
        print(element,' is a prime number.')
main()