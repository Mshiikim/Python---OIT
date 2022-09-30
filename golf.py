#This program tracks the scores for an amateur golf club tournament players.
#MIS285 - 6.10 - Golf Scores part 1
#Author: Michael Shiiki-Morris

def main():
    repeat = 'y' # variable for repeat loop
    scores = open('scores.txt','w') # opens / creates a file for storing data
    while repeat == 'y' or repeat == 'Y':
        print('Enter the following player information: ')
        name = input('Name:')
        score = input('Score:')
        scores.write('Name: '+ name + '\n')
        scores.write('Score: ' + score + '\n')
        print('Do you want to add another player?')
        repeat = input('Enter Y or y for yes, anything else for no: ')
    scores.close()
main()
