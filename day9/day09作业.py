'''
能力强化(自主设计以下类)
1.封装狙击手类
	属性：
		名字
		枪 = None
	行为：
		捡枪(枪)
		装弹<创建弹夹，循环创建子弹，装进弹夹里，然后把弹夹装到墙上>

		瞄准(敌人)
		射击(敌人)<调用枪的射击方法>
2.封装枪类
	属性：
		型号
		弹夹=None
	行为：
		射击(敌人)<打出一颗子弹>
3.封装弹夹类
	属性：
		弹夹容量
		存储子弹的列表
4.封装子弹类
	属性：
		伤害值

	行为：
		移动
5.封装敌人类
	属性：
		名称
		生命值
	行为：
		是否死亡<根据生命值进行判断，如果<=0，应声倒下>

综合应用(尝试实现)
6.完成如下操作：
狙击手xxx捡起一把xx枪，装弹，瞄准敌人xxx，射击,敌人生命值归0，应声倒下
'''
class Player:
    def __init__(self,name):
        self.name=name
        self.gun=None
    #捡枪
    def pick_gun(self,gun):
        self.gun=gun
        print(f'{self.name}捡起了一把枪-{self.gun.type}')
    #装子弹
    def load(self):
        #创建一个容量为20空弹夹
        cilp=Cilp(20)
        print('开始装子弹')
        # 将多个子弹装循环进弹夹里（子弹，弹夹）
        for i in range(cilp.count):
        # 创建伤害为100的子弹，然后装到弹夹存储子弹的列表中
        bullet=Bullet(100)
        cilp.bullet_list.append(bullet)
            print(i+1)
#枪
class Gun:
    def __init__(self,type):
        self.type=type
#子弹
class Bullet:
    def __init__(self,damage):
        self.damage=damage
    def move(self):
        print('让子弹飞一会~~~')
#弹夹
class Cilp:
    def __init__(self,count):
        #弹夹容量
        self.count=count
        # 装子弹的列表
        self.bullet_list = []
#敌人
class Emery:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
    def get_shot(self,bullet):
        self.hp-=bullet.damage
        if self.hp<=0:
            print(f'{self.name}中弹身亡')
        else:
            print(f'{self.name}剩余生命值:{self.hp}')


player1=Player("毛十八")
# print(player1.__dict__)
gun=Gun('ak47')
player1.pick_gun(gun)