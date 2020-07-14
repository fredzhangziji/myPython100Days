'''
除了上面提到的生成器语法，Python中还有另外一种定义生成器的方式，
就是通过yield关键字将一个普通函数改造成生成器函数。下面的代码演
示了如何实现一个生成斐波拉切数列的生成器。所谓斐波拉切数列可以通
过下面递归的方法来进行定义：
'''

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a
        # 下一次call这个function的时候，从这一行继续run
        # 如果是return，直接结束function了
        # 所以是return的话，下次call，就从第一行开始run


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()