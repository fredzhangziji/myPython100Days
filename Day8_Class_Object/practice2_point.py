'''
Make a class about a point to:
    1. describe it
    2. move it
    3. calculate the distance between it and another point

    1/3/2020
    written by Fred Zhang
'''

from math import sqrt


class point(object):
    
    def __init__(self, name, x=0.0, y=0.0):
        self._name = name
        self._x = x
        self._y = y
    
    def info(self):
        print("%s's coordinates are (%.3f, %.3f)" % (self._name, self._x, self._y))
    
    def move(self, x=0.0, y=0.0):
        self._x = x
        self._y = y
    
    def distance(self, anotherP):
        return sqrt((self._x-anotherP._x)**2+(self._y-anotherP._y)**2)

    def __str__(self):
        return '(%s, %s)' % (str(self._x), str(self._y))

    # 定义__repr__偷懒的方法    
    __repr__ = __str__


def main():
    P1 = point('P1')
    P2 = point('P2',5,5)
    P1.info()
    P2.info()
    P1.move()
    P1.info()
    P2.move(3,4)
    P2.info()
    print("-------------__str__")
    print(P2)
    print("-------------__str__")

    print('The distance between P1 and P2 is: %.3f.' % P1.distance(P2))

if __name__ == '__main__':
    main()


# def __str__(self):
#   return xxxxxx
# 用在class里面，用于直接print一个obj
# 如果不定义__str__或者__repr__的话，打印出来的是对象的内存地址
# eg: print(p2) -> 见本文件45行

# 两者的差别：__str__只在print的时候会调用，单独一个object的话，return的还是object的地址。
# __repr__在直接调用object和print(object)的时候都会return定义里的格式。