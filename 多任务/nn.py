# from time import sleep
#
#
# def sing():
#     for i in range(3):
#         print("正在唱歌...%d" % i)
#         sleep(1)
#
#
# def dance():
#     for i in range(3):
#         print("正在跳舞...%d" % i)
#         sleep(1)
#
#
# if __name__ == '__main__':
#     sing()  # 唱歌
#     dance()  # 跳舞

import threading
from time import sleep


def sing():
    while True:
    # for i in range(3):
        print("正在唱歌...%d-----------------")
        sleep(0.05)


def dance():
    while True:
    # for i in range(3):
        print("正在跳舞...%d" )
        sleep(0.05)


if __name__ == '__main__':
    # 创建线程1
    # "target" : 线程执行的目标函数
    my_thread1 = threading.Thread(target=sing)
    my_thread2 = threading.Thread(target=dance)
    # 开启线程执行任务
    my_thread1.start()
    my_thread2.start()