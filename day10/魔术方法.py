'''
魔术方法：
    1.系统定义的__方法__（）
    2.特点是，在一定场景下系统自动触发
__init__()
    创建对象时，系统自动调用
__str__
__repr__
两个方法都会在打印对象时，默认调用，优先调用__str__,如果没有，则执行__repr__如果都没有则找父类
__del__
    删除方法
    在一个对象，被系统回收时，会触发
'''

# class Dog:
#     def __init__(self,name):
#         self.name=name
# dog1=Dog('十八')
# print(dog1.name)

# class Student(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# 重写父类的__str__方法
# def __str__(self):
#     print('str')
#     return f'姓名：{self.name} 年龄:{self.age}'
# def __repr__(self):
#     print('repr')
#     return f'姓名：{self.name} 年龄:{self.age}'
# def __del__(self):
#     print(f'{self.name}被系统收走了')
# stu=Student('学生1',18)
# # print(stu)
# stu2=stu
# del stu
# while True:
#     pass

'''
魔法方法：
__call__:
    触发场景：
        如果一个对象，被当成函数/方法来调用，__call__方法会自动执行
__new__:
    触发场景:
        创建对象时，自动触发，先与__init__
        new方法中的返回值，固定的
        作用：负责开辟内存

运算符重载：
    对于自定义对象的运算，本质会调用魔法方法：
    比如：__add__
    两个对象求和时，会触发
'''


class Student(object):
    def __new__(cls, *args, **kwargs):
        print('__new__')
        return super().__new__(cls)

    def __init__(self, name, age):
        print('__init__')
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        pass
        print('__call__')

    def __add__(self, other):
        print('__add__被触发')
        # return self.age+other.age
        return self.name + other.name


# stu1 = Student('aa', 18)  # Student.__new__().__init__()
# stu1()
# print(stu1)
# print(type(stu1))
# print(dir(object))
#
# stu2 = Student('bb', 20)
# print(stu1 + stu2)

