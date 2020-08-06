"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""

import re

def main():
    m1 = False
    m2 = False
    m3 = False
    while not (m1 and m2 and m3):
        print("欢迎来到qq号注册系统")
        username = input("请输入用户名：")
        qq = input("请输入QQ号：")
        pw = input("请输入密码：")
        # match函数的第一个参数是正则表达式字符串或正则表达式对象
        # 第二个参数是要跟正则表达式做匹配的字符串对象
        m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
        if not m1:
            print('请输入有效的用户名')
        
        m2 = re.match(r'^[1-9]\d{4,11}$', qq)
        if not m2:
            print('请输入有效的qq号')
        
        m3 = re.match(r'^.{6,12}$', pw)
        if not m3:
            print("请输入有效的密码")

    print('你输入的信息是有效的，注册成功！')
    print('你的用户名是：%s'% username)
    print('你的qq号是: %s'% qq)
    print('你的密码是：%s' % pw)

if __name__ == "__main__":
    main()