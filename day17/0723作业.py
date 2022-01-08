'''1.查资料理解并行与并发的区别
2.查资料理解同步与异步的区别
3.查资料理解进程与线程的区别
4.使用进程池完成一部电视剧的下载(模拟下载任务，下载完成时，在回调函数中给出对应的结果)
5.使用进程池完成一个文件夹中多个文件的复制，复制出来的文件名为旧文件名-复件.后缀
6.使用多线程完成售票的模拟案例(注意线程锁的使用)
'''
# 4.使用进程池完成一部电视剧的下载(模拟下载任务，下载完成时，在回调函数中给出对应的结果)
# from multiprocessing import Pool
# import time
#
#
# def download(name):
#     for i in range(6):
#         print(f'{name}下载{i * 20}%')
#         time.sleep(1)
#     return name
#
#
# def alert(name):
#     print(f'{name}下载完成')
#
#
# list1 = [f'乡村爱情第{i}集' for i in range(1, 11)]
# if __name__ == '__main__':
#     pool=Pool(2)
#     for a in list1:
#         pool.apply_async(func=download,args=(a,),callback=alert)
#     pool.close()
#     pool.join()
# 5.使用进程池完成一个文件夹中多个文件的复制，复制出来的文件名为旧文件名-复件.后缀
import os
import time
from multiprocessing import Pool


def copyallfile(fliebag):
    files = os.listdir(fliebag)
    for i in files:
        pool.apply_async(func=copyfile, args=(fliebag + '/' + i,), callback=alert)


def copyfile(file):
    f1 = open(file, 'r', encoding='utf-8')
    t = file.rpartition('.')
    new_name = t[0] + '_复件' + t[1] + t[2]
    f2 = open(new_name, 'w', encoding='utf-8')
    for i in f1:
        f2.write(i)
    f1.close()
    f2.close()
    return file


def alert(i):
    print(f'{i}复制完成')


if __name__ == '__main__':
    pool = Pool()
    copyallfile(r'E:\python\study\python基础\第二周练习')
    pool.close()
    pool.join()

# copyallfile('E:\python\study\python基础\第二周练习')
# 6.使用多线程完成售票的模拟案例(注意线程锁的使用)
# import time
# import threading
# tickets=100
# lock=threading.Lock()
# def sale(name):
#     global tickets
#     while tickets>0:
#         if lock.acquire():
#             if tickets>0:
#                 tickets-=1
#                 time.sleep(0.01)
#                 print(f'{name}售出1张票，剩余{tickets}张')
#             lock.release()
# t1 = threading.Thread(target=sale,args=('窗口1',))
# t2 = threading.Thread(target=sale,args=('窗口2',))
# t1.start()
# t2.start()
