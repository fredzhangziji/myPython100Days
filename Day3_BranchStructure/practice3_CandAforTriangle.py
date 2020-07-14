'''
To calculate the perimeter and area of a triangle with 3 edges
    12/17/2019
    written by Fred Zhang
'''

import math

a = float(input("Enter the first edge: "))
b = float(input("Enter the second edge: "))
c = float(input("Enter the third edge: "))

if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c

    # using Heron's Formula to calculate triangle's area using 3 edges
    p = perimeter / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    # the above line can also be written as:
    #   area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    # without importing the math lib

    print('Perimeter is %.2f.' % perimeter)
    print("Area is %.2f." % area)

else: 
    print("Those edges can't form a triangle.")