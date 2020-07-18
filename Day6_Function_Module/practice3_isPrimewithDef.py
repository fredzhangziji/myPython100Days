'''
To determine if a number is a prime number with functions.
    12/20/2019
    written by Fred Zhang
'''

import math

def isPrime(a):
    if a <= 0:
        print("Invalid input.")
    elif a == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(a))+1):
            if a % i == 0:
                return False
        return True

def main():
    num = int(input("Enter an integer: "))
    if isPrime(num) == True:
        print("%d is a prime number." % num) 
    else:
        print("%d is not a prime number." % num)
    pass

if __name__ == "__main__":
    main()