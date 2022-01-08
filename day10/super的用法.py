# # class A:#python2中的旧式类，搜索按深度优先
# class A(object):#python2的新式类，搜索按广度优先
#     def testA(self):
#         print('A.testA')
# class B(A):
#     pass
# class C(A):
#     def testA(self):
#         print('C.testA')
# class D(B,C):
#     pass
#
# d = D()
# d.testA()


'''
super的用法：
    可以调用父类中的方法
#super(B,self).__init__(a)可以在类外使用
'''


# class A:
#     def __init__(self,a):
#         self.a=a
#     def test1(self):
#         print('A.test')
# class B(A):
#     def __init__(self,a,b):
#         super(B, self).__init__(a)
#         self.b=b
#     def test1(self):
#         print(('B.test'))
# b=B(1,2)
# print(b.__dict__)
# 可以在类外直接调用父类中的方法
# super(B,b).test1()
# 这种写法只能在类内使用
# super().test1()

# 在多继承中，super的本质
class A:
    def test1(self):
        print('a')


class B(A):
    def test1(self):
        print('b')
        print(self)
        super(B, self).test1()


class C(A):
    def test1(self):
        print('c')
        super(C, self).test1()


class D(B, C):
    def test1(self):
        print('d')
        super(D, self).test1()


d = D()
# print(D.mro())  # 取决于D.mro()
d.test1()  # 广度优先
