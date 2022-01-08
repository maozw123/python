"""

面向对象：
1.封装
    类的封装：
        属性：
            __init__(self)
        方法：
            定义在类的内部，并且有一个必要参数self的函数

        私有属性：
            什么是私有属性？
                双下划开头的属性，被称为私有属性
            有哪些特性？
                只能在类的内部访问，不对外开放(无法在类外访问)
            为什么要用私有属性？
                控制属性的访问权限
            如果使用私有属性需要注意的事项？
                应该对外提供私有属性的访问方式：
                    1.提供获取私有属性值的方法(读)
                    2.提供设置私有属性值的方法(写)
            私有化的本质？
                python不是真正意义上的私有化，本质是进行名字重整(被改名)
                改名的规则：
                    _类名__属性名

        私有方法：
            定义形式：
                def __方法名(self)
            有哪些特性？
                只能在类的内部访问，不对外开放(无法在类外访问)

            什么时候使用？
                不需要对外开发的方法，就可以做成私有的，类似回合制游戏中的攻击方法
                只提供一个攻击入口，其他攻击方式，只在内部使用

            私有方法的本质：
                方法名重整
                规则：
                    _类名__方法名()
"""


class Student:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.__gender=gender
    # 提供读取私有属性的方式  get属性名
    def getGender(self):
        return self.__gender
    def introduce(self):
        #在类的内部可以访问私有属性
        print(f'姓名：{self.name}年龄：{self.age}性别：{self.__gender}')
        # 在类的内部，可以访问的当前类的私有方法
        self.__test1()

    #     提供设置私有属性的方式  set属性名（参数）
    def setGender(self,gender):
        if gender=='男' or gender=='女':
            self.__gender=gender
        else:
            self.__gender='男'
            print('性别有误，默认为设置成男')
            # 提供私有方法
    def __test1(self):
        print('我是Student的私有方法')
stu1=Student('小明',15,'男')
# stu1._Student__gender = '半男不女'
# 可以通过访问重整之后的名字，访问到私有属性，但是不提倡
# print(stu1._Student__gender)
# print(stu1.getGender())
print(stu1.name)
print(stu1.age)
# print(stu1.__gender)#报错  无法在类的外部访问私有属性
# stu1.introduce()
# print(stu1.getGender())
stu1.getGender()
print(stu1.getGender())
stu1.setGender('半男不女')


# 私有方法，无法在类外访问
# stu1.__test1()
print(dir(stu1))
# 通过改名之后的方法  可以访问到（不提倡）
stu1._Student__test1()