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

def encrypt(eKey):
    etext = []
    usertext = input("enter someshit: ")
    for i in usertext:
        etext.append(eKey.get(i,i))
    return ''.join(etext)

secretmsg = encrypt(encryption_key_pair)
print("encryption: " + secretmsg)

def decrypt(secret, dKey):
    dtext = []
    for i in secret:
        dtext.append(dKey.get(i,i))
    return ''.join(dtext)

print("decryption: " + decrypt(secretmsg, decryption_key_pair))
