#This program uses a dictionary to assign values to act like an encryption.
#MIS285 - 9.3 - File Encyption
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
    
    infile = open('test.txt','r') #open test file to encrypt
    file_contents = infile.read()
    file_encrypted = '' #storage for encrypted data
    index = 0 #Counter for loop
    while index < len(file_contents):
        word = file_contents[index] #get current key at indexed position
        for ch in word: #loops through each character in key converting value to key
            enc = str(encrypt.get(ch)) 
            file_encrypted += enc
        index += 1
    infile.close()
    outfile = open('encrypt_test.txt','w') #open or create new file for encrypted data
    outfile.write(file_encrypted)
    outfile.close()
    print('Encryption Complete') #little output to make sure user knows script ran and is completed
main()