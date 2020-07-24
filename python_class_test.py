class Test(object):
    # 只是创建了一个class，没有方法也没有属性
    pass

def main():
    Test1 = Test()  # 用class创建一个object
    Test1.name = "object 1"
    Test1.use = "testing for attributes"

    print("The object's name is %s." % Test1.name)
    print("The use of this object is %s." % Test1.use)


if __name__ == "__main__":
    main()


