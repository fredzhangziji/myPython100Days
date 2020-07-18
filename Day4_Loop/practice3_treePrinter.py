'''
Print out trees.
    12/19/2019
    written by Fred Zhang
'''

row = int(input("Enter the number of rows: "))

for i in range(0, row):
    for j in range(0, i+1):
        print("*", end="")
    print()

for i in range(0, row):
    for k in range(row, i+1, -1):
        print(" ", end="")
    for j in range(0, i+1):
        print("*", end="")
    print()

for i in range(0, row):
    for j in range(0, row-i-1):
        print(" ", end="")
    for l in range(row-i-1, row+i):
        print("*", end="")
    # No need to print out those spaces
    # for k in range(row+i, row*2):
    #     print(" ", end="")
    print()
