# 固定参数个数的函数
def add_single(a=0, b=0, c=0):
    print("a + b + c = %d" % (a+b+c))

# 未知参数个数的函数
# 在参数名前面的*表示args是一个可变参数
# 在最下方调用这个函数的时候， 可以传入0个或多个参数
def add_multiple(*args1):
    sum = 0
    ascii = 97
    output = ""
    for argument in args1:
        sum += argument
        output += str(chr(ascii)) + " + "
        ascii += 1
    output = output[:-2]
    output += "= " + str(sum)
    
    print(output)

add_single(5, 6, 7)

add_multiple(2,3,4,5,6,7,8)

add_multiple(6,7,10)


