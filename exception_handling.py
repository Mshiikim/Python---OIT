#This program adds exception handling to exercise 6.6
#MIS285 - 6.9 - Exception Handling
#Author: Michael Shiiki-Morris

def main():
    average = 0
    counter = 0
    try:
        infile = open('numbers.txt','r')
        for line in infile:
            counter += 1
            sub = int(line)
            average += sub
        average = average/counter
        print('The average of the numbers in the file is:', average)
    except IOError:
        print('An error occured trying to access the file.')
    except ValueError:
        print('Non-numeric data found in the file.')
    except:
        print('An error occured.')
    finally:
        infile.close()
main()