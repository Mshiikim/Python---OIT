#This program decrypts the file created in encrypt.py
#MIS285 - 9.3 - File Decryption
#Author: Michael Shiiki-Morris

def main():
    encrypt={
    'a':'*','A':'$','b':'^','B':'#','c':'m','C':'R','D':'q',
    'd':'1','E':'b','e':'`','F':'x','f':'j','G':'/','g':'{',
    'H':'4','h':'|','I':'#','i':'.','J':'v','j':'9','K':'Z',
    'k':'}','L':'?','l':'U','M':'-','m':']','N':'"','n':'E',
    'O':';','o':'_','P':'^','p':'S','Q':'>','q':'2','R':'3',
    'r':'!','S':'<','s':'g','T':'W','t':'=','U':'c','u':'y',
    'V':'a','v':'T','W':'C','w':'L','X':'8','x':'7','Y':'[',
    'y':'/','Z':'k','z':'i',' ':'Y'}
    decrypt ={} #Was lazy and decided to write this loop to switch the values in the encrypt dictionary 
    for key in encrypt: #loop through encrypt dictionary and swap key : value into new dictionary
        letter = key
        letter2 = encrypt[key]
        decrypt[letter2] = letter
    infile = open('encrypt_test.txt','r') #open encryped file, encrypt.py saves to this format
    file_contents = infile.read()
    file_decrypted = '' #variable to store decrypted characters
    index = 0 #counter
    while index < len(file_contents):
        word = file_contents[index] #convert indexed position value to word variable
        for ch in word: #cycle through each character in word variable
            enc = str(decrypt.get(ch)) #pull from library
            file_decrypted += enc #add converted value to output variable
        index += 1
    infile.close()
    print(file_decrypted) 
    
main()