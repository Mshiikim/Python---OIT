#This program accesses a file named numbers and averages the values of the listed numbers in this file.
#MIS285 - 6.6 - Average Numbers
#Author: Michael Shiiki-Morris

def main():
    average = 0
    counter = 0
    infile = open('numbers.txt','r')
    for line in infile:
        counter += 1
        sub = int(line)
        average += sub
    average = average/counter
    print('The average of the numbers in the file is:', average)
    infile.close()
main()