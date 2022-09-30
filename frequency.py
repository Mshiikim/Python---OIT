#This program reads contents from a text file and will create dictionary and count the number of times each word appears.
#MIS285 - 9.5 - Word Frequency
#Author: Michael Shiiki-Morris

def main():
    words = {} #empty library to store key : value
    infile = open('word_test.txt') #open test file
    file_contents = infile.read()
    infile.close()
    file_words = file_contents.split() #seperate each word and store in new variable
    index = 0 #Look! A counter!
    while index < len(file_words): 
        new_key = file_words[index] #store current indexed key
        word_counter = 0 #Counter for word count
        for new_key in file_words: #Check if indexed key is already in library
            if new_key == file_words[index]: #If key is in dictionary adds 1 to counter
                word_counter +=1
            words[new_key] = word_counter #stores count for key in dictionary
        index +=1
    print(words)

main()