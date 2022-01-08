"""
继承：
    子类可以继承父类非私有的属性，方法(无法访问属性以及私有方法)

派生属性(属性重写)
    子类中如果存在与父类中的同名属性，以子类为准

"""
class A:
    def __init__(self,a):
        self.__a=a#私有属性

    def __test1(self):
        print('A的私有方法')

class B(A):
    def test2(self):
        pass
# b=B(10)
# b = B(10)
# # # print(b.__a)
# # b.__test1()
# b.test2()



# 子类重写父类中属性
class C:
    def __init__(self):
        self.c = 10
class D(C):
    def __init__(self):
        super().__init__()
        self.c = 100

d = D()
print(d.c)