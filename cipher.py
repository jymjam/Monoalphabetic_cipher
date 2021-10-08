'''
Author: HK
About: Implementation of monoalphabetic cipher
'''
from collections import Counter
import random, string
import sys

#func creates a random key value pair for encryption
def buildCipher():
    keyPool = string.ascii_lowercase + string.digits + string.punctuation + string.whitespace #only numbers and alpha;
    alpha = list(keyPool) # list of alphabets ['a','b','c','d',....'8','9']
    cipher = list(keyPool) # creates another list same as alpha above
    random.shuffle(cipher) # shuffles cipher list ['z','c','5','l',....,'6','k']
    encCipher = dict(zip(alpha, cipher)) #creates a {alpha:cipher} dictionary {'a':'z','b':'c',...,'8':'6','9':'k'}
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
    print('cipher is : ')
    print(encryptedText)

    while True:
        print('''
        1 : show true decryption key
        2: decrypt cipher using true decryption key
        3: show guessed key(s)
        0: exit the program
        ''')
        userInput = str(input("enter your choice: "))
        if userInput == '0':
            break
        elif userInput == '1':
            print(decryption_key_pair)
        elif userInput == '2':
            print(decrypt(encryptedText, decryption_key_pair))
        elif userInput == '3':
            print(decrypt(encryptedText, guessedKey))
        else:
            print('unknown input, try again!')

#if not imported
if __name__ == '__main__':
    main()
