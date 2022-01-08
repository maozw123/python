
'''
反射函数
    1.hasattr()
    判断是否包含某个属性
    2.getattr()
    获取某个属性
    3.setattr
    修改属性值
    4.delattr()
    删除属性
反射系统模块中的方法：
方法=getattr(模块名，‘方法名’)

'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showInFo(self):
        # print(self.name,self.age)
        return self.name,self.age
stu=Student('学生1',19)
stu.name='学生2'
print(stu.showInFo())
#判断某个对象是否包含某个属性
if hasattr(stu,'name'):
    setattr(stu,'name','学生3')
    #通过反射函数获取对象中某个属性的值
    v1=getattr(stu,'name')
if hasattr(stu,'age'):
    v2 = getattr(stu,'age')
print(v1,v2)
# 使用反射调用系统模块中方法
import time
print(time.time())

# 使用反射函数完成类似的调用
t = getattr(time,'time')
print(t)
print(t())
import random
#通过反射拿到系统模块random的中randint方法
r = getattr(random,'randint')
#r就是反射到的系统方法
print(r)
num = r(1,6)
print(num)

import sys
#sys.modules 系统预加载到内存中的模块名(其中有一个特殊的就是'__main__',表示的是当前模块),一个字典
# print(list(sys.modules.keys()))

# 使用反射函数拿到当前模块中，Student类
S = getattr(sys.modules['__main__'],'Student')
print(S)
stu3 = S('学生名123',18)
print(stu3.name,stu3.age)