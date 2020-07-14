'''
Get the max and the second max element in the list.
    12/27/2019
    written by Fred Zhang
'''

def max2(list):
    max1 = max(list)
    list.remove(max1)
    max2 = max(list)
    list.remove(max2)
    return max1, max2

if __name__ == '__main__':
    print(max2([1,2,3,4,5,7,8]))