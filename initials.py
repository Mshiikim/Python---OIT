#This program will provide initials for a name entered by the user.
#MIS285 - 8.1 - Initials
#Author: Michael Shiiki-Morris

def main():
    user_name = str(input("Enter your name: "))
    word_list = user_name.split() #Split the user name into a list
    initial_list = [] #list for initial storage
    initials = '' #variable for output
    index = 0 #counter for loop
    while index < len(word_list): #Loop to pull first character of each value in word_list and place in new list
        initial = word_list[index] 
        initial_list += initial[0]
        index += 1
    for ch in initial_list: #Loop that assigns each value in initial_list to a variable for output
        initials += ch
        initials += '.'
    print(initials)
main()