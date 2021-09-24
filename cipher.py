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
    decCipher = dict(map(reversed, encCipher.items()))

    return [encCipher, decCipher] #returns a dictionary of alpha: cipher



print("dec cipher: " + buildCipher()[1])


'''
file = open(sys.argv[1], 'r')
while 1:
    char = file.read(1)
    if not char:
        break
    print(char)

file.close()
'''
