'''
Find perfect number within range 0 to 10000.
    12/20/2019
    written by Fred Zhang
'''

for i in range(1,10001):
    num = 0
    for j in range(1, i//2+1):      # int(sqrt(i))+1
        if i % j == 0:
            num = num + j
    if num == i:
        print(i, end=' ')

print()
