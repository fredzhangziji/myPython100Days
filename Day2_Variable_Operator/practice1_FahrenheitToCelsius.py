'''
A simple program to convert between Fahrenheit and Celsius degrees.
    12/17/2019
    written by Fred Zhang
'''

while True:
    print('**************************************************')
    print('**************************************************')
    print('Welcome to Fahrenheit and Celsius degree converter')
    print('Enter the option:')
    print('c for Fahrenheit to Celsius degree;')
    print('f for Celsius to Fahrenheit degree;')
    print('e for exiting the program.')
    print('**************************************************')
    print('**************************************************')
    userInput = input()

    if userInput == 'c':
        DegreeF = float(input('Enter the Fahrenheit degree: '))
        DegreeC = (DegreeF - 32) / 1.8
        print('The Celsius degree is: ', DegreeC)
    
    if userInput == 'f':
        DegreeC = float(input('Enter the Celsius degree: '))
        DegreeF = 1.8 * DegreeC + 32
        print('The Fahrenheit degree is: ', DegreeF)
    
    if userInput == 'e':
        break

    if userInput != 'c' and userInput != 'f' and userInput != 'e':
        print('userInput at this point is: ', userInput)
        print("Invalid input. Please enter a valid input.")