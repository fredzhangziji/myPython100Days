'''
To check if a num is a prime and a palindrome at the same time by modules.
    12/20/2019
    written by Fred Zhang
'''

import practice2_isPalindromewithDef as isPal
import practice3_isPrimewithDef as isPri

if __name__ == "__main__":
    a = int(input("Enter an integer: "))

    # this if condition can be written as below:
    # if isPal.isPalindrome(a) and isPri.isPrime(a):
    if isPal.isPalindrome(a) == True and isPri.isPrime(a) == True:
        print("%d is a prime and a palindrome." % a)
    
    else: 
        print("%d is not a prime and a palindrome at the same time." % a)