'''
Generate the first 20 numbers of Fibonacci sequence.
    12/19/2019
    written by Fred Zhang
'''

previous = 1
fibNum = 1
print("1", end=' ')
for i in range(20):
    print("%d" % fibNum, end=' ')
    temp = fibNum + previous
    previous = fibNum
    fibNum = temp

    # a, b = b, a + b
    