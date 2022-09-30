#This program asks a user for a file name and displays the content of the file with line numbering.
#MIS285 - 6.3 - Line Numbers 
#Author: Michael Shiiki-Morris

def main():
    # ask for file name to open
    user_file = input('Enter the name of the file to open: (include file type) ')
    infile = open(user_file,'r') #open file and assign to infile variable
    counter = 0 # counter for line numbers
    for line in infile:
        counter += 1
        line = line.rstrip('\n') # remove additional new line for cleaner output
        print(counter,':',line) 
    infile.close() # close file
main()