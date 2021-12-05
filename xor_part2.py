import string # A list of printable characters to validate against
import os, sys, random
from collections import Counter

def cryptAnalysis(plainText, cipher):
    #CrypAnalysis
    pool = list(string.ascii_letters + string.digits + string.punctuation + string.whitespace) #pool of all printable chara, same as alpha list in buildcipher() 
    plainTextFrequencyCounter = Counter(plainText) #counts all chars in plaintext (frequency) 
    cipherTextFrequencyCounter = Counter(cipher) # counts all chars in cipher
    plain_count_dict = {l: plainTextFrequencyCounter[l] for l in pool if l in plainTextFrequencyCounter} #creates a dict of chars and it's frequency. e.g {'a':40, 'b':12,..., '\n':7}
    cipher_count_dict = {k: cipherTextFrequencyCounter[k] for k in pool if k in cipherTextFrequencyCounter} 

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

def buildCipher():
    #This function generates a list of keys for mono alphabetic encryption
    keyPool = string.ascii_letters + string.digits + string.punctuation + string.whitespace #contains all printable characters;
    alpha = list(keyPool) # list of all printable chara. e.g ['a','b','c','d',...'8','9',...,'\n','\r',...]
    alphaCopy = list(keyPool) # creates another list same as alpha above
    random.shuffle(alphaCopy) # shuffles cipher list ['z','c','5','l',....,'6','k']
    encCipher = dict(zip(alpha, alphaCopy)) #creates a {alpha:cipher} dictionary {'a':'z','b':'c',...,'8':'6','9':'k'}
    return encCipher #returning encryption key

encryption_key_pair = buildCipher() # returned dict of buildCipher is the encryption key 
decryption_key_pair = dict(map(reversed, encryption_key_pair.copy().items())) #copies encryption key and reverses it

#function to encrypt ascii passed in the argument 
def encrypt(text_to_encrypt, eKey): #takes a text and the encryption key
    #Encyption for Monoalphabetic encryption
    encrypted_text = []
    for i in text_to_encrypt:
        encrypted_text.append(eKey.get(i,i))
    return ''.join(encrypted_text) #returns the encrypted text (cipher)

#function to decrypt ascii passed in the argumetn; for testing
def decrypt(cipher, dKey): #takes a text and decryption key
    #Decryption for Monoalphabetic encryption
    decrypted_text = []
    for i in cipher:
        decrypted_text.append(dKey.get(i,i))
    return ''.join(decrypted_text) #returned decyrpted text
"""
def generate_key(length) :
    text_random_cipher = ""
    #generation of the random key until the length of the cipher text after the encrypt function

    random_key = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + string.whitespace, k = length))
    text_random_cipher=str(random_key)# converts the key into string
    return text_random_cipher
"""
def generate_key(length) :
    #generation of the key 
    key = "apple"
    len_key=len(key)
    num=length
    text_random_cipher=[]
    while num >=0:
        for element in key[0:num:1]:
            
            
            text_random_cipher += (element)
            #print( text_random_cipher )    
                
        num=num-len_key
    text_random_cipher=str(text_random_cipher)
    return ''.join(text_random_cipher)

def encrypt_after_mono(text, text_random_cipher):
    """In this function we will be encrypting the text after the encrypt funcation"""

    ciphertext = [] #list of the cipher text characters will be stored 
    combine = zip(text, text_random_cipher)#accepts iterable items and merges them into a single tuple of text_random_cipher and text
    for char_of_text, char_of_pad in combine:
        ciphertext_character = chr(ord(char_of_text) ^ ord(char_of_pad))#ord returns the unicode value of each text and ^ does XOR for the both unicode value
        #chr gets the string representation of the int value from the XOR operation
        ciphertext += (ciphertext_character)
        
    return ''.join(ciphertext)# combines the list to a string and then returns it to the main

def decrypt_after_mono(text_random_cipher, ciphertext):
    """In this function we will be decrypting the text after the decrypt funcation"""
    plaintext = [] #list of the plain text characters will be stored 
    combine=zip(text_random_cipher, ciphertext)#accepts iterable items and merges them into a single tuple of text_random_cipher and text
    for char_of_text, ciphertextstring in combine:
        #ord returns the unicode value of each text and ^ does XOR for the both unicode value
        #chr gets the string representation of the int value from the XOR operation
        
        plaintext += chr(ord(char_of_text) ^ ord(ciphertextstring))

    return ''.join(plaintext)# combines the list to a string and then returns it to the main



def main():

    #check if file in argument
    if len(sys.argv) < 2: #checks if the argumetn has a passed file to encrypt
        print("example: python3 ./cipher ./file_to_encrypt")
        quit()

    oFile = open(sys.argv[1], 'r') #if passed; the file is opened to read
    text = oFile.read() #plain text content
    text_random_cipher = generate_key(len(text))
    encryptedText = encrypt(text, encryption_key_pair) #content of the opened file is encrypted
    ciphertext= encrypt_after_mono(encryptedText, text_random_cipher) #content of the opened file is encrypted
    
    oFile.close()
    plaintext = decrypt_after_mono(text_random_cipher, ciphertext)
 
    menu = ('''
    -------------------------------------------
    to show, press:
    1: Padded Text Strings
    2: Plaintext after  One time pad encryption
    3: ciphertext after monoalphabetic decryption and one time pad encrytption
    4: cipher frequency after monoaplabetic encryption
    5: plain text frequency
    6: cryptanakysis of unqie key after monoaplabetic encryption and one time pad encryption
    7: cryptalysis after monoaplabetic encryption and one time pad encryption
    8: Decrytption of monoalphabetic 
    h: Show this menu again
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
            print(text_random_cipher)
        elif userInput == '2':
            print(plaintext)
        elif userInput == '3':
            print(ciphertext)#one time pad encryption
        elif userInput == '4':
            print(cryptAnalysis(text,ciphertext)[0])
        elif userInput == '5':
            print(cryptAnalysis(text,ciphertext)[1])
        elif userInput == '6':
            print(cryptAnalysis(text,ciphertext)[2])
        elif userInput == '7':
            print(decrypt(ciphertext, cryptAnalysis(text, ciphertext)[2]))
        elif userInput == '8':
            print(decrypt(encryptedText, decryption_key_pair))
        elif userInput == 't':
            pass
        else:
            print('(press h for help)!\n')

#if not imported
if __name__ == '__main__':
    main()



