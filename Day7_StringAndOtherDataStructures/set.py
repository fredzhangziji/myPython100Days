'''
Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算。
'''

# 可以按照下面代码所示的方式来创建和使用集合。

# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)     # {1, 2, 3}
print('Length =', len(set1))    # Length = 3
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)   # {1, 2, 3, 4, 5, 6, 7, 8, 9} {1, 2, 3}
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)


print('''----------------------------------------------------------------
''' * 3)

# 向集合添加元素和从集合删除元素。
set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1, set2)
print(set3.pop())
print(set3)

# remove()用于删除一个set中的元素，这个值在set中必须存在，如果不存在的话，会引发KeyError错误。
# discard()用于删除一个set中的元素，这个值不必一定存在，不存在的情况下删除也不会触发错误。
# set提供了一个pop()方法，这个函数随机返回一个元素值，然后把这个值删除，如果set为空，调用这个函数会返回Key错误。
# clear(),将set全部清空。


print('''----------------------------------------------------------------
''' * 3)


'''
集合的成员、交集、并集、差集等运算。
'''

# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))

# symmetric difference
# 对称差集：集合A与集合B的对称差集定义为集合A与集合B中所有不属于A∩B的元素的集合，
#          记为A△B,也就是说A△B={x|x∈A∪B,x∉A∩B}，即A△B=(A∪B)—(A∩B).也就是
#          A△B=（A—B）∪（B—A）

# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))