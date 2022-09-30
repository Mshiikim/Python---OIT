#This program is a Rock, Paper, Scissors game against a computer.
#MIS285 - 5.21 - Rock, Paper, Scissors Game
#Author: Michael Shiiki-Morris

import random

def main():
    #Intro text
    print("\tRock, Paper, or Scissors Game")
    repeat = 'y' #set repeat loop
    while repeat == 'y' or repeat == 'Y': #check if program repeats
        cpu_choice = cpu_picker() #determines cpu selection
        user_choice = str(input('Rock, paper or scissors? (enter in all lowercase)')) #user input
        print('The cpu picked',cpu_choice) #cpu choice displayed
        winner(cpu_choice, user_choice) #checks for the winner
        repeat = input('Would you like to play again? (y for yes)') #repeat program check
    
#function to create a random number that determines cpu choice
def cpu_picker(): 
    number = random.randint(1,3)
    if number == 1:
        choice = 'rock'
    elif number == 2: 
        choice = 'paper'
    elif number == 3:
        choice = 'scissors'
    return choice

#function to check results to determine winner
def winner(cpu_choice, user_choice):
    if cpu_choice == 'rock' and user_choice == 'scissors':
        print('Rock smashes scissors, CPU wins!')
    elif cpu_choice == 'scissors' and user_choice == 'paper':
        print('Scissors cut paper, CPU wins!')
    elif cpu_choice == 'paper' and user_choice == 'rock':
        print('Paper wraps rock, CPU wins!')
    elif cpu_choice == 'rock' and user_choice == 'rock' or cpu_choice == 'scissors' and user_choice == 'scissors' or cpu_choice == 'paper' and \
                        user_choice == 'paper':
        print("It's a tie, please play again.")
    elif cpu_choice == 'scissors' and user_choice == 'rock':
        print('Rock smashes scissors, you win!')
    elif cpu_choice == 'paper' and user_choice == 'scissors':
        print('Scissors cut paper, you win!')
    elif cpu_choice == 'rock' and user_choice == 'paper':
        print('Paper wraps rock, you win!')
    else:
        print('Error check')

main()