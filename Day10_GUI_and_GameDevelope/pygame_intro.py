'''FIX ME'''

import pygame

def main():
    # 初始化导入的pygame中的模块
    pygame.init()

    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800,600))

    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')

    # 屏幕坐标系是将屏幕左上角设置为坐标原点(0, 0)，向右是x轴的正向，向下是y轴的正向，
    # 在表示位置或者设置尺寸的时候，我们默认的单位都是像素。


    x, y = 100, 100
    running = True

    # 开启一个时间循环处理发生的时间
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # 通过指定的文件名加载图像
        # rem_image = pygame.image.load('C:/Users/zhang/Desktop/timg.gif')
        # rem_image = pygame.transform.scale(rem_image, (222,217))    # 缩放图片
            
        # 设置窗口的背景色（RGB）
        screen.fill((242,242,242))

        # 绘制一个圆 下面的数字分别代表：图案的rgb颜色，坐标，大小，和中空
        pygame.draw.circle(screen,(255,0,255),(x,y),30, 0)

        # 刷新当前窗口（渲染窗口将绘制的图像呈现出来）
        pygame.display.flip()

        # 每隔30毫秒就改变球的位置再刷新窗口
        pygame.time.delay(30)
        x, y = x + 5, y + 5

if __name__ == "__main__":
    main()

