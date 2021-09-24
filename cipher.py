'''
Author: HK
About: Implementation of monoalphabetic cipher
'''
import random, string
import sys

#func creates a random key value pair for encryption
def settingUpCipherKey():
    listAlpha = list(string.ascii_lowercase)
    cipherKey = listAlpha[:]
    random.shuffle(cipherKey)
    key = dict(zip(listAlpha, cipherKey))

    return key

file = open(sys.argv[1], 'r')
while 1:
    char = file.read(1)
    if not char:
        break
    print(settingUpCipherKey())
    print(char)

file.close()