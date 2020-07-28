import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 定义方法，以便一会儿在窗口中调用
    # 修改标签上的文字
    def change_label_text():
        # 每次调用这个函数都会翻转flag的值，从而修改标签上的文字
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!') if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示','确定要退出吗？'):
            top.quit()


    # 创建顶层窗口
    # （相当于创建了一个对象，这个对象是一个窗口，所有的按钮和功能都是基于这个窗口的）
    top = tkinter.Tk()
    # 设置窗口大小 
    top.geometry('500x300')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, 大哥!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)

    # 创建按钮对象 指定添加到容器中 通过command参数绑定事件回调函数
    # 左边的按钮是“修改”，按一下会调用change_label_text()函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    # 右边的按钮是“退出”，按一下会调用confirm_to_quit()函数
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()

if __name__ == '__main__':
    main()