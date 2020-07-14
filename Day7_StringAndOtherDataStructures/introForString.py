s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
# 三引号内换行等于\n
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')

s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')

print("\t\t\t\\t represents tab.")

# print("\a what does this do")
# this makes the system alarm once (depends on the system)

myName = '\u7ae0\u5b50\u4f76'
print(myName)

'''
如果不希望字符串中的backslash表示转义，我们可以通过在字符串的最前面加上字母r来加以说明，
再看看下面的代码又会输出什么。
'''

# adding r in front of the quotation mark means that backslash is just backslash
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

'''
Python为字符串类型提供了非常丰富的运算符，我们可以使用+运算符来实现字符串的拼接，
可以使用*运算符来重复一个字符串的内容，可以使用in和not in来判断一个字符串是否包
含另外一个字符串（成员运算），我们也可以用[]和[:]运算符从字符串取出某个字符或某
些字符（切片运算），代码如下所示。
'''

s1 = 'hello ' * 3
print(s1) # hello hello hello 
s2 = 'world'
s1 += s2
print(s1) # hello hello hello world
print('ll' in s1) # True
print('good' in s1) # False
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2]) # c
# 字符串切片(从指定的开始索引到指定的结束索引)
# 第一个冒号前后表示从index几到index几；不输入就是默认从[0]到[最后]
# 第二个冒号后表示隔几个index；不输入就是默认连续
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[::-1]) # 654321cba
print(str2[-3:-1]) # 45
print(str2[::]) # abc123456
print(str2[:])  # abc123456
