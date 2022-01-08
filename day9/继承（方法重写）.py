'''
方法重写：
    子类重写父类的方法
什么时候重写？
    父类中方法无法满足子类需求的时候，需要进行方法重写

其中一个子类想增加新的属性：
    子类中实现__init__()方法
    在方法添加属性
    可以super().__init__()调用父类中的init方法
'''
class Animal(object):
    def __init__(self,name,color,age):
        self.name=name
        self.color=color
        self.age=age
    def eat(self):
        print('会吃')
    def sleep(self):
        print('趴着睡')
    def shout(self):
        print('动物叫')
class Dog(Animal):
    def __init__(self,name,color,age,breed):
        # self.name=name
        # self.color=color
        # self.age=age
        super().__init__(name,color,age)
        self.breed=breed
    def lookafter_house(self):
        print('守护家园')
    def shout(self):
        print('汪汪汪~~~')
class Cat(Animal):
    def climb_tree(self):
        print('爬树')
    def shout(self):
        print('喵喵喵~~~')
dog1=Dog('大黄','Black',3,'吉娃娃')
dog1.shout()

cat1 = Cat('汤姆','Blue',2)
cat1.eat()
cat1.sleep()
cat1.climb_tree()
cat1.shout()
#
# print(dir(object))