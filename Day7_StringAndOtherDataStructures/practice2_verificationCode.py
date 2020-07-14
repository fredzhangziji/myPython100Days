'''
Generate a verification code with certain length.
    12/27/2019
    written by Fred Zhang
'''

import random

def generateCode(length=3):
    database = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    code = ''
    while len(code) < length:
        code = code + database[random.randint(0, 61)]
    
    return code

if __name__ == '__main__':
    print(generateCode())
        