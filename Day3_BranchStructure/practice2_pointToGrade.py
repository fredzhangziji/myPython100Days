'''
Convert 100-point scale to grade scale
    12/17/2019
    written by Fred Zhang
'''

print('\n\nYo this is a grade converter you sucker!\n')
point = int(input('put in your stupid-ass points here: '))
print()
if point <= 100 and point >= 90:
    print('You got a fucking A. Greate fucking job!')

elif point < 90 and point >= 80:
    print("B. Hmm. Can't you fucking do a lil better than dat?")

elif point < 80 and point >= 70:
    print("You got a C. Did you take Dr. Canas' class?")

elif point <70 and point >= 60:
    print("D. Noob.")

elif point < 60:
    print("Go home kid. You fucking failed.")

else:
    print("How'd fuck you get over 100 points? Reported.")

print()