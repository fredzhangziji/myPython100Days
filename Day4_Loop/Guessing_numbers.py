'''
Source code copied from the Internet
Added GUI with tkinter
    12/17/2019
    written by Fred Zhang
'''

import random
import tkinter
import tkinter.simpledialog

root = tkinter.Tk()
root.title("Guess A Number")

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = tkinter.simpledialog.askinteger('请输入', "0-100的数字")
    if number < answer:
        tkinter.messagebox.showinfo('提示', '大一点' )
    elif number > answer:
        tkinter.messagebox.showinfo('提示','小一点' )
    else:
        tkinter.messagebox.showinfo('提示','恭喜你猜对了!有点强哦～')
        break
tkinter.messagebox.showinfo('提示',"你总共猜了%d次" % counter)
if counter > 7:
    tkinter.messagebox.showinfo('提示','你的智商余额明显不足')

tkinter.mainloop()