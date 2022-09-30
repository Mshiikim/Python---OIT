#This program opens a file named numbers.txt and displays all the numbers in the file.
#MIS285 - 6.1 - File Display
#Author: Michael Shiiki-Morris

def main():
	infile = open('numbers.txt', 'r')
	file_contents = infile.read()
	infile.close()
	print(file_contents)
	
main()