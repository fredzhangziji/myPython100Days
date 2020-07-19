'''
Print out Pascal's Triangle (杨辉三角).
    12/27/2019
    written by Fred Zhang
'''

def printPascalsTriangle(row):
    print('1')
    print('1 1')
    preRow = [1, 1]
    for x in range(2, row):
        curRow = [1]
        for y in range(1, x+1):
            if y <= x-1:
                curRow.append(preRow[y-1] + preRow[y])
            else:
                curRow.append(1)

        for element in curRow:
            print(element, end=' ')
        preRow = curRow
        print()
    
def main():
    printPascalsTriangle(10)

if __name__ == '__main__':
    main()