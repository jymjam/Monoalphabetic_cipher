'''
Author: HK
About: Implementation of monoalphabetic cipher
'''
import random, string

#func creates a random key value pair for encryption
def settingUpCipherKey():
    listAlpha = list(string.ascii_lowercase)
    cipherKey = listAlpha[:]
    random.shuffle(cipherKey)
    key = dict(zip(listAlpha, cipherKey))

    return key

print(settingUpCipherKey())