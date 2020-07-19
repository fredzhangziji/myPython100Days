'''
Get suffix of files.
    12/27/2019
    written by Fred Zhang
'''

def getFileSuffix(fileName, hasDot=False):
    if '.' in fileName:
        # string.rfind() 返回字符串第一次出现的位置(从右向左查询)，如果没有匹配项则返回-1。
        # 和find()相反，find()是从左向右查询到的第一个结果
        # 所以此处应该用rfind()
        startIndex = fileName.rfind('.')    # fileName.find('.')
        if hasDot==False:
            return fileName[startIndex+1:]
        else:
            return fileName[startIndex:]
    else:
        return ''  

def main():
    testfile = 'word.exe'
    print(getFileSuffix(testfile, True))

if __name__ == '__main__':
    main()