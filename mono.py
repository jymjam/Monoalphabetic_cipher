'''PART 2 - Enhanced encryption security
Author: HK
About: Implementation of monoalphabetic cipher
'''
from collections import Counter
import random, string
import sys
#import os

superCharPool = string.ascii_letters + string.digits + string.punctuation + string.whitespace #obj contains all printable chars

#func creates a random key value pair for encryption
def buildKey():
    keyPool = superCharPool
    alpha = list(keyPool) # list of all printable chara. e.g ['a','b','c','d',...'8','9',...,'\n','\r',...]
    alphaCopy = list(keyPool) # creates another list same as alpha above
    random.shuffle(alphaCopy) # shuffles cipher list ['z','c','5','l',....,'6','k']
    encCipher = dict(zip(alpha, alphaCopy)) #creates a {alpha:cipher} dictionary {'a':'z','b':'c',...,'8':'6','9':'k'}
    return encCipher #returning encryption key

encryption_key_pair = buildKey() # returned dict of buildCipher is the encryption key 
decryption_key_pair = dict(map(reversed, encryption_key_pair.copy().items())) #copies encryption key and reverses it

def encrypt2_0(text_to_encrypt):
    plain_text_counter_dict = dict(Counter(text_to_encrypt))
    most_repetitive_char_count = 0
    for key, value in plain_text_counter_dict.items():
        if value > most_repetitive_char_count:
            most_repetitive_char_count = value
            most_repetitive_char = key

    sorted_plain_text_counter_dict = dict(sorted(plain_text_counter_dict.items(), key = lambda e:e[1])) 

    del sorted_plain_text_counter_dict[most_repetitive_char]

    padding_list = []
    for key,value in sorted_plain_text_counter_dict.items():
        while value < most_repetitive_char_count:
            padding_list.append(key)
            value += 1
    
    print(text_to_encrypt)


#function to encrypt ascii passed in the argument 
def encrypt(text_to_encrypt, eKey): #takes a text and the encryption key
    encrypted_text = []
    for i in text_to_encrypt:
        encrypted_text.append(eKey.get(i,i))
    return ''.join(encrypted_text) #returns the encrypted text (cipher)

#function to decrypt ascii passed in the argumetn; for testing
def decrypt(cipher, dKey): #takes a text and decryption key
    decrypted_text = []
    for i in cipher:
        decrypted_text.append(dKey.get(i,i))
    return ''.join(decrypted_text) #returned decyrpted text

#function to count the frequency of the cipher 
def cryptAnalysis(plainText, cipher):
    pool = superCharPool #pool of all printable chara, same as alpha list in buildcipher() 
    plainTextFrequencyCounter = Counter(plainText) #counts all chars in plaintext (frequency) 
    cipherTextFrequencyCounter = Counter(cipher) # counts all chars in cipher
    plain_count_dict = {l: plainTextFrequencyCounter[l] for l in pool if l in plainTextFrequencyCounter} #creates a dict of chars and it's frequency. e.g {'a':40, 'b':12,..., '\n':7}
    cipher_count_dict = {k: cipherTextFrequencyCounter[k] for k in pool if k in cipherTextFrequencyCounter} 

    #finds unique values for keys in cipher dict
    '''extracts unique values keys from the frequency dict. e.g (assume)
    cipher_count = {'a':1, 'b':5, 'c':7, 'd':5, 'e': 3 }
    after running the below block on cipher_count we get
    cipher_unique_dict = {'a':1, 'c':7, 'e':3 }
    '''
    cipher_count_tuple_pairs = [(key, val) for key,val in cipher_count_dict.items()]
    cipher_count_tuple_count = Counter(val for key,val in cipher_count_tuple_pairs)
    cipher_unique_keys = [key for key,val in cipher_count_tuple_count.items() if val == 1]
    cipher_unique_list = [(tupl_key,tupl_val) for tupl_key, tupl_val in cipher_count_tuple_pairs if tupl_val in cipher_unique_keys]
    cipher_unique_dict = {key:val for key,val in cipher_unique_list}
    # sorts dict: cipher_unique_dict = {'c':7,'e':3, 'a':1}
    sorted_cipher_unique_dict = dict(sorted(cipher_unique_dict.items(), key = lambda kv:kv[1]))

    #finds unique values for keys in plain dict (does the same as above 6 lines but on plain_text frequency dict)
    plain_count_tuple_pairs = [(key, val) for key,val in plain_count_dict.items()]
    plain_count_tuple_count = Counter(val for key,val in plain_count_tuple_pairs)
    plain_unique_keys = [key for key,val in plain_count_tuple_count.items() if val == 1]
    plain_unique_list = [(tupl_key,tupl_val) for tupl_key, tupl_val in plain_count_tuple_pairs if tupl_val in plain_unique_keys]
    plain_unique_dict = {key:val for key,val in plain_unique_list}
    sorted_plain_unique_dict = dict(sorted(plain_unique_dict.items(), key = lambda kv:kv[1]))

    #returns dict certain guessed key; can be cross verified with true decryption key
    ''' assume
    line 71: e.g. maps cipher_unique_dict = {'c':7, 'e':3, 'a':1 } --> plain_unique_dict = {'\n':7, 'x':3, '7':1 }
    we get certainGuessedDecryptionKey = { '\n':'c', 'e':'x', '7':'a' }
    '''
    certainGuessDecryptionKey = dict(zip(sorted_cipher_unique_dict, sorted_plain_unique_dict))
    return [cipherTextFrequencyCounter, plainTextFrequencyCounter, certainGuessDecryptionKey] # this func returns a list of dicts

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
    -------------------------------------------
    to show, press:

    1: Real decryption key
    2: Decrypt cipher using decryption key
    3: Guessed key(s) using cryptanalysis
    4: Cipher 
    5: frequency analysis on cipher text
    6: frequency analysis on plain text
    7: Decrypt cipher using guessed key
    8: Real encryption key 
    ------------------------------------------
    h: Show this menu again
    ?: To get surprised!!
    0: Exit
    ------------------------------------------
    ''')

    print(menu)

    # if else ladder
    while True:
        print('\n')
        userInput = str(input("root@win.dos:(h for help)# "))
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

            can be cross verified with the decryption key (option 1)
            \n''')
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
            #os.system("start \"\" https://www.youtube.com/watch?v=HIcSWuKMwOw")
            pass
        elif userInput == 't':
            encrypt2_0(fileContent)
        else:
            print('lol this is not a shell, (press h for help)!\n')

#if not imported
if __name__ == '__main__':
    main()
