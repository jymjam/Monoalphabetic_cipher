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
    keyPool = string.ascii_letters + string.digits + string.punctuation + string.whitespace #only numbers and alpha;
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
#----------------------------------------DO NOT TOUCH ABOVE---------------------------------------

#function to count the frequency of the cipher 
def cryptAnalysis(plainText, cipher):
    pool = list(string.ascii_letters + string.digits + string.punctuation + string.whitespace)
    plainTextFrequencyCounter = Counter(plainText)
    cipherTextFrequencyCounter = Counter(cipher)
    plain_count_dict = {l: plainTextFrequencyCounter[l] for l in pool if l in plainTextFrequencyCounter}
    cipher_count_dict = {k: cipherTextFrequencyCounter[k] for k in pool if k in cipherTextFrequencyCounter}

    #finds unique values for keys in cipher dict
    cipher_count_tuple_pairs = [(key, val) for key,val in cipher_count_dict.items()]
    cipher_count_tuple_count = Counter(val for key,val in cipher_count_tuple_pairs)
    cipher_unique_keys = [key for key,val in cipher_count_tuple_count.items() if val == 1]
    cipher_unique_list = [(tupl_key,tupl_val) for tupl_key, tupl_val in cipher_count_tuple_pairs if tupl_val in cipher_unique_keys]
    cipher_unique_dict = {key:val for key,val in cipher_unique_list}
    sorted_cipher_unique_dict = dict(sorted(cipher_unique_dict.items(), key = lambda kv:kv[1]))

    #finds unique values for keys in plain dict
    plain_count_tuple_pairs = [(key, val) for key,val in plain_count_dict.items()]
    plain_count_tuple_count = Counter(val for key,val in plain_count_tuple_pairs)
    plain_unique_keys = [key for key,val in plain_count_tuple_count.items() if val == 1]
    plain_unique_list = [(tupl_key,tupl_val) for tupl_key, tupl_val in plain_count_tuple_pairs if tupl_val in plain_unique_keys]
    plain_unique_dict = {key:val for key,val in plain_unique_list}
    sorted_plain_unique_dict = dict(sorted(plain_unique_dict.items(), key = lambda kv:kv[1]))

    #returns dict certain guessed key; can be cross verified with true decryption key
    certainGuessDecryptionKey = dict(zip(sorted_cipher_unique_dict, sorted_plain_unique_dict))
    return [cipherTextFrequencyCounter, plainTextFrequencyCounter, certainGuessDecryptionKey]

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

    menu = ('''
    -------------------------------------------------------
    1: show true decryption key (for debug)
    2: decrypt cipher using true decryption key (for debug)
    3: show confident guessed key(s) using cryptanalysis
    4: show cipher (encryped text)
    5: show cipher text frequency count
    6: show plain text frequency count
    7: decrypt cipher using guessed key
    8: show encryption key used to encrypt
    -------------------------------------------------------
    h: Show this menu again
    ?: to get surprised!!
    0: exit the program
    -------------------------------------------------------
    ''')

    print(menu)

    while True:
        print('\n')
        userInput = str(input("root@win.dos:/root# "))
        print("\n")

        if userInput == '0':
            break
        elif userInput == 'h':
            print(menu)
        elif userInput == '1':
            print(decryption_key_pair)
        elif userInput == '2':
            print(decrypt(encryptedText, decryption_key_pair))
        elif userInput == '3':
            print('''
            Program confidently guesses following to be accurate 
            substitution for partial decryption using cryptanalysis

            can be cross verified with the encryption key (option 8)
            ''')
            print(cryptAnalysis(fileContent, encryptedText)[2])
        elif userInput == '4':
            print(encryptedText)
        elif userInput == '5':
            print(cryptAnalysis(fileContent, encryptedText)[1])
        elif userInput == '6':
            print(cryptAnalysis(fileContent,encryptedText)[0])
        elif userInput == '7':
            print(decrypt(encryptedText, cryptAnalysis(fileContent, encryptedText)[2]))
        elif userInput == '8':
            print(encryption_key_pair)
        elif userInput == '?':
            os.system("start \"\" https://www.youtube.com/watch?v=HIcSWuKMwOw")
        else:
            print('lol this is not a shell, (press h for help)!\n')

#if not imported
if __name__ == '__main__':
    main()
