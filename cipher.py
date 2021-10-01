'''
Author: HK
About: Implementation of monoalphabetic cipher
'''
import random, string
import sys

#func creates a random key value pair for encryption
def buildCipher(key = None):
    keyPool = string.ascii_lowercase + string.digits #only numbers and alpha; need to add symbols
    alpha = list(keyPool) # list of alphabets {'a','b','c',....,'9'}
    cipher = list(keyPool)
    random.shuffle(cipher) # shuffle all numbers and slphabets

    encCipher = dict(zip(alpha, cipher)) #{'a':'z', 'b':'y','9':'i'}

    return encCipher #returing the pair

encryption_key_pair = buildCipher() #encryption key 
print(encryption_key_pair)
decryption_key_pair = dict(map(reversed, encryption_key_pair.copy().items()))
print(decryption_key_pair)

#function to encrypt ascii passed in the argument 
def encrypt(text_to_encrypt, eKey):
    encrypted_text = []
    for i in text_to_encrypt:
        encrypted_text.append(eKey.get(i,i))

    return ''.join(encrypted_text)

#function to decrypt ascii passed in the argumetn
def decrypt(text_to_decrypt, dKey):
    decrypted_text = []
    for i in text_to_decrypt:
        decrypted_text.append(dKey.get(i,i))

    return ''.join(decrypted_text)

#main func 
def main():
    #check if file in argument
    if len(sys.argv) < 2:
        print("example: python3 ./cipher ./encrypt_this.java")
        quit()

    oFile = open(sys.argv[1], 'r')
    fileContent = oFile.read()

    tmp = encrypt(fileContent, encryption_key_pair)
    print(tmp)

    oFile.close()

    print('---------------')

    reveal = decrypt(tmp, decryption_key_pair)
    print(reveal)

#check if not a module
if __name__ == '__main__':
    main()
