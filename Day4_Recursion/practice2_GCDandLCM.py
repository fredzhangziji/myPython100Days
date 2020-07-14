'''
Greatest Common Divisor and Least Common Multiple of two numbers.
    12/18/2019
    written by Fred Zhang
'''

userInput1 = int(input("Enter the first number: "))
userInput2 = int(input("Enter the second number: "))

# This can be replaced by code below:
# if x > y:
#   x, y = y, x     (this equals to temp = x; x = y; y = temp; It swaps the values of two)
# So the bigger one is always y.
bigger = max(userInput1, userInput2)

# for i in range(1, bigger+1):
#     if userInput1 % i == 0 and userInput2 % i == 0:
#         GCD = i

# LCM = userInput1 / GCD * userInput2

# Compare the code below with the commented code above.
# The code below has lower runtime complexity.
# The code below is smarter.
for i in range(bigger, 0, -1):
    if userInput1 % i == 0 and userInput2 % i == 0:
        print("For %d and %d: " % (userInput1, userInput2))
        print("The greatest common divisor is %d." % i)
        print("The least common multiple is %d." % (userInput1 * userInput2 / i))
        break
