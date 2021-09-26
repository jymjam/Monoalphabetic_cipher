'''
Author: HK
About: Implementation of monoalphabetic cipher
'''
import random, string
import sys

#func creates a random key value pair for encryption
def buildCipher(key = None):
    keyPool = string.ascii_lowercase + string.digits
    alpha = list(keyPool)
    cipher = list(keyPool)
    random.shuffle(cipher)

    encCipher = dict(zip(alpha, cipher))

    return encCipher 

encryption_key_pair = buildCipher() 
decryption_key_pair = dict(map(reversed, encryption_key_pair.copy().items()))

print('key creation successful!')

def encrypt(text_to_encrypt, eKey):
    encrypted_text = []
    for i in text_to_encrypt:
        encrypted_text.append(eKey.get(i,i))
    return ''.join(encrypted_text)

def decrypt(text_to_decrypt, dKey):
    decrypted_text = []
    for i in text_to_decrypt:
        decrypted_text.append(dKey.get(i,i))
    return ''.join(decrypted_text)

oFile = open('./sample.txt', 'r')
fileContent = oFile.read()

tmp = encrypt(fileContent, encryption_key_pair)
print(tmp)

oFile.close()

print('---------------')

reveal = decrypt(tmp, decryption_key_pair)
print(reveal)
