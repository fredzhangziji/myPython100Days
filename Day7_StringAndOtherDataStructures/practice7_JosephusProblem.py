'''
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个
人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到
9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔
掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪
些位置是基督徒哪些位置是非基督徒。
'''

def location(num=30):
    locList = [True] * num
    counter = 0
    index = 0  
    while num > 15:
        if locList[index] == True:
            counter += 1
            if counter == 9:
                locList[index] = False
                num -= 1
                counter = 0
        index += 1
        index %= 30
    
    for element in locList:
        print('基' if element == True else '非',end='')

    print()

if __name__ == '__main__':
    location()