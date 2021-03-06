'''
访问可见性问题
对于上面的代码，有C++、Java、C#等编程经验的程序员可能会问，我们给Student对象绑定的
name和age属性到底具有怎样的访问权限（也称为可见性）。因为在很多面向对象编程语言中，我
们通常会将对象的属性设置为私有的（private）或受保护的（protected），简单的说就是不
允许外界访问，而对象的方法通常都是公开的（public），因为公开的方法就是对象能够接受的
消息。在Python中，属性和方法的访问权限只有两种，也就是公开(public)的和私有(private)
的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头，下面的代码可以验证这一点。
'''

class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')

    # only way to access private attributes and methods (but it's "illegal")
    print("\nIllegal access")
    test._Test__bar()
    print(test._Test__foo)
    print()


    # AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test.__foo)

    


if __name__ == "__main__":
    main()


'''
但是，Python并没有从语法上严格保证私有属性或方法的私密性，它只是给私有的属性和方法换
了一个名字来妨碍对它们的访问，事实上如果你知道更换名字的规则仍然可以访问到它们，下面的
代码就可以验证这一点。之所以这样设定，可以用这样一句名言加以解释，就是"We are all 
consenting adults here"。因为绝大多数程序员都认为开放比封闭要好，而且程序员要自己
为自己的行为负责。

在实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问（后面会讲到）。
所以大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护
的，本类之外的代码在访问这样的属性时应该要保持慎重。
'''


'''
Accessability
______________________________________________________________
|           │ Class │ Package │ Subclass │ Subclass │ World  |  python
|           │       │         │(same pkg)│(diff pkg)│        |
|───────────┼───────┼─────────┼──────────┼──────────┼────────|
|public     │   +   │    +    │    +     │     +    │   +    |  nothing
|───────────┼───────┼─────────┼──────────┼──────────┼────────|
|protected  │   +   │    +    │    +     │     +    │        |    _foo
|───────────┼───────┼─────────┼──────────┼──────────┼────────|
|no modifier│   +   │    +    │    +     │          │        | 
|───────────┼───────┼─────────┼──────────┼──────────┼────────|
|private    │   +   │         │          │          │        |   __foo
|___________|_______|_________|__________|__________|________|
 + : accessible         blank : not accessible
'''

'''
面向对象有三大支柱：封装(Encapsulation)、继承(Inheritance)和多态(Polymorphism)。后
面两个概念在下一个章节中进行详细的说明，这里我们先说一下什么是封装。我自己对封装的理解是"隐
藏一切可以隐藏的实现细节，只向外界暴露（提供）简单的编程接口"。我们在类中定义的方法其实就是
把数据和对数据的操作封装起来了，在我们创建了对象之后，只需要给对象发送一个消息（调用方法）就
可以执行方法中的代码，也就是说我们只需要知道方法的名字和传入的参数（方法的外部视图），而不需
要知道方法内部的实现细节（方法的内部视图）。

1. Encapsulation
2. Inheritance
3. Polymorphism
'''