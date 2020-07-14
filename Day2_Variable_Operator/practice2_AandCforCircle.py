'''
A simple program to calculate area and perimeter
    12/17/2019
    written by Fred Zhang
'''

import math

radius = float(input("Enter the radius of the circle: \n"))
print('Area of the circle is: %.3f' % (radius * radius * math.pi))
print('Perimeter of the circle is: %.3f' % (2 * radius * math.pi))

