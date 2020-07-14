'''
Get Greatest Common Divisor and Least Common Multiple with functions
    12/20/2019
    written by Fred Zhang
'''

def LCM(a, b):
    if a > b:
        a, b = b, a
    for i in range(b, 0, -1):
        if b%i == 0 and a%i == 0:
            return i

def GCD(a, b):
    return a*b//LCM(a,b)

if __name__ == "__main__":
    a = int(input("Enter num1: "))
    b = int(input("Enter num2: "))
    print("LCM is: ", LCM(a, b))
    print("GCD is: ", GCD(a, b))
