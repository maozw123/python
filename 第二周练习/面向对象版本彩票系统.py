'''
1.完成面向对象版本彩票系统：彩票只需要实现最简单的彩票玩法就行
(购买1-10的之内的3个数，可以重复，没有顺序要求，只要3个号码与开奖号码一致，就算中奖，中奖金额200)

彩票类：
	属性：
		彩票号码
		彩票价格
	行为：
		展示彩票信息
系统类：

	行为：
		生成彩票
		彩票开奖
人类：
	属性：
		名字
		金钱
		已购彩票
	行为：
		购买彩票
		兑奖
		剩余金钱展示
交互：
	实现张三花xx钱买了1注彩票，去兑奖，展示中奖结果，以及张三的剩余钱数
'''

# 类与类之间的联系
import random


class People:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.my_lottey_list = []

    # 买彩票
    def buy_lottey(self):
        # 调用彩票类
        lottey = Lottey()
        print('请输入你要买的彩票号码')
        for i in range(1, 4):
            a = eval(input(f'请输入第{i}个号码'))
            lottey.numbers.append(a)
        self.my_lottey_list.append(lottey)
        self.money -= lottey.lottey_price
        print(f'您买的彩票号码为{lottey.numbers},钱剩余{self.money}')

    # 查看开奖
    def check(self):
        s = System()
        s.open_lottey()
        # for l in self.my_lottey_list:
        if self.my_lottey_list == s.open_lottey:
            print('您中奖了')
            self.money+=200
        else:
            print('很遗憾，您没中奖')
    def show_info(self):
        print(f'钱剩余{self.money}')


# 生成彩票的系统，并可以查看开奖
class System:
    def open_lottey(self):
        open_list = []
        # 随机生成开奖号码并和人买的彩票对比，一样则中奖，否则很遗憾没中奖
        for i in range(3):
            b = random.randint(0, 9)
            open_list.append(b)
        print(f'开奖号码为{open_list}')
        return open_list
# 彩票类
class Lottey:
    def __init__(self):
        self.lottey_price = 2
        self.numbers=[]
    def show_number(self):
        print(self.numbers)
    def __eq__(self, other):
        return self.numbers==other.numbers
people = People('毛十八', 100)
people.buy_lottey()
people.show_info()
people.check()
people.show_info()
# s=System()
# s.open_lottey()
