'''
Author: HK
About: Implementation of monoalphabetic cipher
'''
import random, string
import sys
from collections import Counter

#func creates a random key value pair for encryption
def buildCipher(key = None):
    keyPool = string.ascii_lowercase + string.digits + string.punctuation#only numbers and alpha; need to add symbols
    alpha = list(keyPool) # list of alphabets ['a','b','c','d',....'8','9']
    cipher = list(keyPool) # creates another list same as alpha above
    random.shuffle(cipher) # shuffles cipher list ['z','c','5','l',....,'6','k']

    encCipher = dict(zip(alpha, cipher)) #creates a {alpha:cipher} dictionary {'a':'z','b':'c',...,'8':'6','9':'k'}

    return encCipher #returns the pair (encryption key)

encryption_key_pair = buildCipher() # returned dict of buildCipher is the encryption key 
decryption_key_pair = dict(map(reversed, encryption_key_pair.copy().items())) #copies encryption key and reverses it

#function to encrypt ascii passed in the argument 
def encrypt(text_to_encrypt, eKey): #takes a text and the encryption key
    encrypted_text = []
    for i in text_to_encrypt:
        encrypted_text.append(eKey.get(i,i))
    return ''.join(encrypted_text) #encypted text is returned

#function to decrypt ascii passed in the argumetn
def decrypt(cipher, dKey): #takes a text and decryption key
    decrypted_text = []
    for i in cipher:
        decrypted_text.append(dKey.get(i,i))
    return ''.join(decrypted_text)

#function to count the frequency of the program
def frequencyCounter(cipher):
    return Counter(cipher) #returns character count

def keyGuess(freq):
    pass

#main func 
def main():
    #check if file in argument
    if len(sys.argv) < 2: #checks if the argumetn has a passed file to encrypt
        print("example: python3 ./cipher ./encrypt_this.java")
        quit()

    oFile = open(sys.argv[1], 'r') #if passed; the file is opened to read
    fileContent = oFile.read()

    tmp = encrypt(fileContent, encryption_key_pair) #content of the opend file is encrypted
    print(tmp)

    oFile.close()

    frequencyCounter(tmp)

#check if not a module: don't worry about this section
if __name__ == '__main__':
    main()
