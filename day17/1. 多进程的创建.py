"""
进程与线程
网络编程
数据结构与算法
周五：测试

多进程与多线程以及协程（实现多任务）

多任务：
    同时执行多个任务

同时：
    并行与并发（课下查询）
    并行：
        两个任务同时执行
        两个老师同时为两个学生解答问题
    并发：（高并发）
        两个任务交替执行
        一个老师同时为两个学生解答问题

多任务：
1.多进程
    进程？
        针对操作系统来讲的，
        运行中的程序程序(代码)，
        一个程序默认情况下，只有一个进程(主进程)

    进程，需要向系统申请单独的内存



    开启多任务：
        使用多进程
        创建子进程：
        multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={})
        target: 指定在子进程中执行的任务
        name:  为子进程创建的名字
        args: 表示为函数传递的参数

    注意：
        手动开启的子进程，会将主进程中所有的资源复制一份（更消耗内存）

        用空间换时间


2.多线程

3.协程

"""
import time
import multiprocessing


def download1(t):
    for i in range(5):
        print(f'{t}进行{i * 25}%')
        time.sleep(1)


def download2():
    for i in range(5):
        print(f'下载任务2进行{i * 25}%')
        time.sleep(1)


# while True:
#     download1()
#     download2()
# 创建两个子进程
# Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
if __name__ == '__main__':
    p1 =multiprocessing.Process(target=download1,name='子进程',args=('毛毛毛11',))
    print(p1)
    print(p1.name)
    p2 = multiprocessing.Process(target=download2, name='子进程2')
    print(p2.name)
    p1.start()
    p2.start()
