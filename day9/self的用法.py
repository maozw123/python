"""
self 的用法：
    1.self就是一个必要的形参
    2.一定是当前类的一个对象（哪个对象调用方法，参数self就是这个对象）
    3.可以访问当前类的属性，也可以调用当前类的方法
需求：创建一个学生类
属性：
    姓名，年龄，性别
方法：
    学习
    玩游戏
    睡觉
    自我介绍
"""
class Student:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def study(self):
        print('我超爱学习')
    def play_game(self,game_name):
        print(f'{self.name}爱玩游戏-{game_name}')
    def sleep(self):
        self.play_game('吃鸡')
        print(f'{self.name}躺床上睡')
    def introduce(self):
        print(f'我叫{self.name} 性别{self.gender} 今年{self.age}')
        print(id(self))

stu1 = Student('如花',18,'女')
# print(id(stu1))
stu1.introduce()
stu1.sleep()


stu2 = Student('似玉',19,'女')
stu2.introduce()