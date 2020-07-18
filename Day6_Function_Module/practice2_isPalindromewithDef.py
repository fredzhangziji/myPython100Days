'''
To determine if a number is a palindrome with functions.
    12/20/2019
    written by Fred Zhang
'''

def isPalindrome(a):
    aOri = a
    rev = 0
    while a > 0 :
        rev = rev * 10 + a % 10
        a //= 10
    if aOri == rev:
        return True

def main():
    num = int(input("Enter an interger: "))
    if isPalindrome(num):
        print("%d is a Palindrome." % num)
    else:
        print("%d is not a Palindrome." % num)
    pass

if __name__ == "__main__":
    main()