#This program displays the scores for an amateur golf club tournament players.
#MIS285 - 6.10 - Golf Scores part 2
#Author: Michael Shiiki-Morris

def main():
    infile = open('scores.txt', 'r')
    for line in infile:
        line = line.rstrip('\n')
        print(line)
    infile.close()
main()