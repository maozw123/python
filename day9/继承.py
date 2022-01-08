"""
面向对象：
    1.封装
    2.继承
        类与类之间建立关系的一种方式   （课下查资料，类与类之间的关系）
        父类(基类，根类，超类)
        子类(孩子类，派生类)
    语法：
        旧式类(经典类)
        class 类名:
            pass
        新式类：
        class 类名(父类):
            pass

        1.如果一个类，没有明确指明父类是谁，那么默认父类是object，
        2.object是所有类的父类

    特性：
        子类可以继承父类中所有非私有的属性跟方法

    使用继承的必要性：

"""
# class Dog:
#     def __init__(self,name,color,age):
#         self.name=name
#         self.color=color
#         self.age=age
#     def eat(self):
#         print('会吃')
#     def sleep(self):
#         print('趴着睡')
#     def lookafter_house(self):
#         print('守护家园')
# class Cat(object):
#     def __init__(self,name,color,age):
#         self.name = name
#         self.color = color
#         self.age = age
#     def eat(self):
#         print('会吃')
#     def sleep(self):
#         print('趴着睡')
#     def climb_tree(self):
#         print('爬树')
#
# dog1=Dog('小白','Black',3)
# dog1.eat()
# dog1.sleep()
# dog1.lookafter_house()
#
# cat1=Cat('汤姆','Blue',2)
# cat1.eat()
# cat1.sleep()
# cat1.climb_tree()

# 类Dog和类Cat可以把共同点归到类Animal
class Animal:
    def __init__(self,name,color,age):
        self.name = name
        self.color = color
        self.age = age
    def eat(self):
        print('会吃')
    def sleep(self):
        print('趴着睡')
class Dog(Animal):
    def lookafter_house(self):
        print('守护家园')
class Cat(Animal):
    def climb_tree(self):
        print('爬树')


dog1=Dog('大黄','Black',3)
dog1.eat()
dog1.sleep()
dog1.lookafter_house()

