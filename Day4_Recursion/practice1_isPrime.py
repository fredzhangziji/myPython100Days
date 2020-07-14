'''
To check is a number a prime number.
    12/18/2019
    written by Fred Zhang
'''

userInput = int(input("Enter a number: "))
isPrime = True

if userInput <= 0:
    print("Invalid input.")

elif userInput == 1:
    print("1 is neither a prime number nor a composite number.")

else:
    # Here we don't actually need the whole range from 2 to userInput.
    # We can use range from 2 to sqrt(userInput)+1 to save space.
    for i in range(2, userInput):
        if userInput % i == 0:
            isPrime = False
            print("%d is a composite number." % userInput)
            break

    if isPrime == True:
        print("%d is a prime number." % userInput)
