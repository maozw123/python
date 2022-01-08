'''
基础题：
1.创建函数，可以完成一个视频的复制(注意视频读写使用的mode为rb,wb)，新视频的名字为视频名_副本.后缀，
如果被复制的视频文件>10M 则抛出自定义异常(目标文件太大),提示(os.path.getsize(file)可以获取文件大小)
2.创建学生类，设置私有属性_age, 提供对应的set，get方法，set方法中如果给的数据不合理，抛出
自定义异常 AgeError

提升题：
3.基于购物车的业务逻辑，实现一个单例模式的购物车类

4.查阅资料熟悉工厂模式(简单工厂，抽象工厂)

'''

# 如何查看一个文件的编码方式
import chardet


# with open('E:\python\study\python基础\day14\手动抛出自定义异常.py', 'rb') as file:
# print(chardet.detect(file.read())) # {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
# 1.创建函数，可以完成一个视频的复制(注意视频读写使用的mode为rb,wb)，
# 新视频的名字为视频名_副本.后缀，如果被复制的视频文件>10M 则抛出自定义异常(目标文件太大),
# 提示(os.path.getsize(file)可以获取文件大小)
class FileError(Exception):
    def __init__(self):
        self.errMsg='文件过大'
    def __str__(self):
        return f'FileError{self.args}'
import os
def copy_video(file):
    if os.path.getsize(file)<10*1024*1024:
        f1 = open(file, 'rb', )
        a = file.rpartition('.')
        new_name = a[0] + '_副本' + a[1] + a[2]
        f2 = open(new_name, 'wb', )
        for i in f1:
            f2.write(i)
        f1.close()
        f2.close()
    else:
        raise FileError()


# copy_video('E:\python\study\python基础\day14\梁小秋.mp4')
# 2.创建学生类，设置私有属性_age, 提供对应的set，get方法，set方法中如果给的数据不合理，抛出
# 自定义异常 AgeError
class Student:
    def __init__(self,age):
        self.set_age(age)
    def set_age(self,age):
       if 0<age<18:
           self.__age=age
       else:
           raise AgeError
    def get_age(self,age):
        return self.__age

class AgeError(Exception):
    def __init__(self):
        self.errMsg = '参数有误'
    def __str__(self):
        return self.errMsg


# 3.基于购物车的业务逻辑，实现一个单例模式的购物车类
class ShoppingCart:
    __has = None
    __first_init = True

    def __new__(cls, *args, **kwargs):
        if not cls.__has:
            cls.__has = super().__new__(cls)
        return cls.__has

    def __init__(self):
        if self.__first_init:
            self.cart = []
            ShoppingCart.__first_init = False

# cart1 = ShoppingCart()
# cart2 = ShoppingCart()
# cart1.cart.append('kt4')
# cart1.cart.append('科比毒液')
# print(cart2.cart)
# print(id(cart1))
# print(id(cart2))

# 4.查阅资料熟悉工厂模式(简单工厂，抽象工厂)

