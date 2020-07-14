'''
简单的说，类是对象的蓝图和模板，而对象是类的实例。这个解释虽然有
点像用概念在解释概念，但是从这句话我们至少可以看出，类是抽象的概
念，而对象是具体的东西。在面向对象编程的世界中，一切皆为对象，对
象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类
（型）。当我们把一大堆拥有共同特征的对象的静态特征（属性）和动态
特征（行为）都抽取出来后，就可以定义出一个叫做“类”的东西。
'''

'''
定义类
在Python中可以使用class关键字定义类，然后在类中通过之前学习过的
函数来定义方法，这样就可以将对象的动态特征描述出来，代码如下所示。
'''

class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    # 可以设置默认值
    def __init__(self, name='A normal student', age=18):
        self.name = name
        self.age = age
    
    def study(self,courseName):
        print("%s is studying %s..." % (self.name, courseName))
    
    def watchMovie(self):
        if self.age < 18:
            print("You can only watch SpongeBob.")
        else:
            print("logging in pornhub.com")
    

def main():
    # create an object

    Student1 = Student("Sbdongxi", 15)
    Student2 = Student("Fred", 20)
    Student3 = Student()    # 没有argument就使用默认值创建

    Student1.study("CSC211")
    Student2.study("CSC999")
    Student3.study("JPN101")

    Student3.watchMovie()

    # 输出object的attributes
    print(Student3.age)
    print(Student3.name)

if __name__ == "__main__":
    main()
