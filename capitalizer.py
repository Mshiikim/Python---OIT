#This program takes a user entered string and will capitalize each letter of each word.
#MIS285 - 8.9 - Sentence Capitalizer
#Author: Michael Shiiki-Morris

def main():
    input_string = str(input('Enter a sentence please: '))
    word_list = input_string.split() #split user entry into a list
    index = 0 #counter
    output = '' #variable for output
    while index < len(word_list): #loop to capitalize each word in word_list
        word1 = word_list[index].capitalize() 
        output += word1 #add capitalized word to new variable for output
        output += ' ' #add after each word for proper format
        index += 1
    print(output)
main()