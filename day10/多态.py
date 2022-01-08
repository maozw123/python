# 方法的多态
# 调用的同样名字的方法，但是实现的形式有可能是多样的
# 1.继承
# 2.方法重写
# 案例：
#     不同国家的人
class Person:
    def eat(self):
        print('人都需要吃饭')
class Chinese(Person):
    def eat(self):
        print('中国人用筷子吃饭')
class English(Person):
    def eat(self):
        print('英国人用刀叉吃饭')
class Indian(Person):
    def eat(self):
        print('神奇的阿三用手吃饭')

person=Person()
person.eat()
person=Chinese()
person.eat()
person=Indian()
person.eat()