'''
python内置的 @property装饰器 (Decorators)
之前我们讨论过Python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，
但是如果直接将属性暴露给外界也是有问题的，比如我们没有办法检查赋给属性的值是否有效。
我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议
外界直接访问，那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）
方法进行对应的操作。如果要做到这点，就可以考虑使用@property包装器来包装getter和
setter方法，使得对属性的访问既安全又方便，代码如下所示。
'''

class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property   # python内置的装饰器@property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        # 在setter里可以用下面的方法来限定input
        if not isinstance(age, int):    # check if the input is an integer
            raise ValueError('Age must be an integer!')
        if age < 0 or age > 1000:       # check if the input is in range 0-1000
            raise ValueError('That\'s not a human\'s age!')

        self._age = age

    # @name.setter
    # def name(self, name):
    #     self._name = name

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22          # 这边能set成功是因为上面有@age.setter
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute
                             # 因为@name.setter在上面被comment掉了
    print(person.name)
    print(person.age)
    person.length = '18cm'
    person.money = '$999999'
    # person.age = -1       # ValueError will be raised
    # person.age = 1001     # ValueError will be raised


if __name__ == '__main__':
    main()

