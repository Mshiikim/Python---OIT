#This program calculates what values in a list are greater than a user entered value.
#MIS285 - 7.6 - Larger Than n
#Author: Michael Shiiki-Morris

def main():
    #test list and value for arguments for larger_check function
    test_list = [1,2,3,4,3,2,1]
    test_value = 1
    #call function to test
    larger_check(test_list, test_value)

#function to check if list has values above user inputed value
def larger_check(list, n):
    size = len(list) #set size for range
    for index in range(size): #loop through list
        value = list[index] #assign new value at next index position
        if value > n: #greater than check, print value if true
            print(value) 
main()