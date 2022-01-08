'''
抽象类
抽象类不能创建对象包含
1.抽象类也是一个类，区别在于抽象方法的的类，才是抽象类
2.抽象方法  本质就是一个方法  必须用@abstrmethod装饰
3.创建一个抽象类
    1.需要引入（AbcMeta,abstractmethod）
    2.手动指定元类
    3.创建抽象方法
4.抽象类的作用
    一定意义上可以约束子类的行为，要求子类重写父类中抽象方法，如果子类不重写父类中的抽象方法
    则子类依旧是抽象类。



'''
from abc import ABCMeta,abstractclassmethod
class Anmial(metaclass=ABCMeta):
    def __init__(self,color):
        self.color=color
    @abstractclassmethod
    def shout(self):
        pass
class Dog(Anmial):
    def shout(self):
        print('汪汪汪')

# an1=Anmial

dog1=Dog('Yellow')
dog1.shout()