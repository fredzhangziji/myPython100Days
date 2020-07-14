'''
Convert between cm and inch
    12/17/2019
    written by Fred Zhang
'''

while True:
    print("-------Welcome to cm/inch Converter Version 1.0-------")
    print("Enter 'cm' for converting inch to cm;")
    print("Enter 'inch for converting cm to inch;")
    print("Enter 'e' for exiting the program.")
    print("Select option: ")
    selection = input()

    if selection == 'cm':
        inch = float(input('Enter inch: '))
        cm = inch * 2.54
        print("%.2f inches = %.2f cm" % (inch, cm))

    elif selection == 'inch':
        cm = float(input("Enter cm: "))
        inch = cm / 2.54
        print('%.2f cm = %.2f inch' % (cm, inch))

    elif selection == 'e':
        break

    else:
        print("Invalid input.")