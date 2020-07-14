'''
To determine if a year is a leap year
    12/17/2019
    written by Fred Zhang
'''

year = int(input("Enter the year: \n"))
yearStr = str(year)

if yearStr[2] == '0' and yearStr[3] == '0':
    if year % 400 == 0:
        print('Year %d is a leap year.' % year)
    else:
        print('Year %d is NOT a leap year.' % year)

else:
    if year % 4 == 0:
        print('Year %d is a leap year.' % year)
    else:
        print('Year %d is NOT a leap year.' % year)


'''
There is actually no need to convert the year into str to check if it's
multiple of 100. Just % 100 to check like below.

year = int(input('请输入年份: '))
如果代码太长写成一行不便于阅读 可以使用slash对代码进行折行
is_leap = (year % 4 == 0 and year % 100 != 0) or slash
year % 400 == 0
print(is_leap)
'''