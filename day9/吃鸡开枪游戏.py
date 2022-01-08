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


# 创建人类
import time
class Player:
    def __init__(self,name):
        self.name=name
        self.gun=None
    # 捡枪
    def pick_gun(self,gun):
        self.gun=gun
        print(f'{self.name}捡到一把枪{self.gun.type}')
    # 装子弹
    def load(self):
        clip=Clip(20)
        print('开始装弹')
        # 将多个子弹装循环进弹夹里（子弹，弹夹）
        for i in range(clip.count):
            # 创建子弹，装到弹夹存储子弹的列表中
            bullet=Bullet(100)
            clip.bullet_list.append(bullet)
            print(i+1)
            time.sleep(0.1)
        #把弹夹装到枪上
        self.gun.clip=clip
        print('装弹完成')
    #射击敌人
    def shot(self,emery):
        print('扣动扳机')
        # 人需要调用枪的射击方法
        bullet=self.gun.shot(emery)
        # 调用子弹的移动方法
        bullet.move()
        emery.get_shot(bullet)
class Emery:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
    def get_shot(self,bullet):
        self.hp-=bullet.damage
        if self.hp <= 0:
            print(f'{self.name}中弹身亡')
        else:
            print(f'{self.name}剩余生命值:{self.hp}')





# 创建枪类
class Gun:
    def __init__(self,type):
        self.type=type
    def shot(self, emery):
        # 射出一颗子弹，同时存储子弹的列表减少一颗
        bullet = self.clip.bullet_list.pop()
        print(f'子弹剩余{len(self.clip.bullet_list)}')
        return bullet

# 创建弹夹类
class Clip:
    def __init__(self,count):
        self.count=count
        # 创建存储子弹的列表
        self.bullet_list=[]

# 创建子弹类
class Bullet:
    def __init__(self,damage):
        self.damage=damage
    def move(self):
        print('让子弹飞一会')

player1=Player('毛毛')
gun=Gun('m416')
player1.pick_gun(gun)
player1.load()
em=Emery('梁小秋',100,)
for i in range(10):
    player1.shot(em)