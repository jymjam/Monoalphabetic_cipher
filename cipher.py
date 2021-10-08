'''
Author: HK
About: Implementation of monoalphabetic cipher
'''
from collections import Counter
import random, string
import sys
import os

#func creates a random key value pair for encryption
def buildCipher():
    keyPool = string.ascii_lowercase + string.digits + string.punctuation + string.whitespace #only numbers and alpha;
    alpha = list(keyPool) # list of alphabets ['a','b','c','d',....'8','9']
    alphaCopy = list(keyPool) # creates another list same as alpha above
    random.shuffle(alphaCopy) # shuffles cipher list ['z','c','5','l',....,'6','k']
    encCipher = dict(zip(alpha, alphaCopy)) #creates a {alpha:cipher} dictionary {'a':'z','b':'c',...,'8':'6','9':'k'}
    return encCipher 

encryption_key_pair = buildCipher() # returned dict of buildCipher is the encryption key 
decryption_key_pair = dict(map(reversed, encryption_key_pair.copy().items())) #copies encryption key and reverses it

#function to encrypt ascii passed in the argument 
def encrypt(text_to_encrypt, eKey): #takes a text and the encryption key
    encrypted_text = []
    for i in text_to_encrypt:
        encrypted_text.append(eKey.get(i,i))
    return ''.join(encrypted_text)

#function to decrypt ascii passed in the argumetn; for testing
def decrypt(cipher, dKey): #takes a text and decryption key
    decrypted_text = []
    for i in cipher:
        decrypted_text.append(dKey.get(i,i))
    return ''.join(decrypted_text)
#-----------------------------------------------------DO NOT TOUCH ABOVE--------------------------------

#function to count the frequency of the cipher 
def cryptAnalysis(plainText, cipher):
    pool = list(string.ascii_lowercase + string.digits + string.punctuation + string.whitespace)

    cipherTextFrequencyCounter = Counter(cipher)
    plainTextFrequencyCounter = Counter(plainText)

    cipher_count_dict = {k: cipherTextFrequencyCounter[k] for k in pool if k in cipherTextFrequencyCounter}
    plain_count_dict = {l: plainTextFrequencyCounter[l] for l in pool if l in plainTextFrequencyCounter}


#main func 
def main():
    #check if file in argument
    if len(sys.argv) < 2: #checks if the argumetn has a passed file to encrypt
        print("example: python3 ./cipher ./file_to_encrypt")
        quit()

    oFile = open(sys.argv[1], 'r') #if passed; the file is opened to read
    fileContent = oFile.read() #plain text content
    encryptedText = encrypt(fileContent, encryption_key_pair) #content of the opend file is encrypted
    oFile.close()

    guessedKey = {"a":'7', "b": '5'}

    while True:
        print('''
        ------------------------MENU---------------------------
        1: show true decryption key (for debug)
        2: decrypt cipher using true decryption key (for debug)
        3: show guessed key(s) using cryptanalysis
        4: show cipher/encryped text
        0: exit the program
        ?: to get surprised!!
        -------------------------------------------------------
        ''')
        userInput = str(input("enter your choice: "))
        print("\n")

        if userInput == '0':
            break
        elif userInput == '1':
            print(decryption_key_pair)
        elif userInput == '2':
            print(decrypt(encryptedText, decryption_key_pair))
        elif userInput == '3':
            #print(decrypt(encryptedText, guessedKey))
            print(guessedKey)
        elif userInput == '4':
            print(encryptedText)
        elif userInput == '?':
            os.system("start \"\" https://www.youtube.com/watch?v=HIcSWuKMwOw")
        else:
            print('unknown input, try again!')

#if not imported
if __name__ == '__main__':
    main()
