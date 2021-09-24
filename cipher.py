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

    return encCipher  #returns a dictionary of alpha: cipher

enckey = buildCipher()
deckey = enckey.copy()

revkey = dict(map(reversed, deckey.items()))

print(enckey)
print("---------")
print(revkey)




'''
file = open(sys.argv[1], 'r')
while 1:
    char = file.read(1)
    if not char:
        break
    print(char)

file.close()
'''
