"""
基于面向对象思想封装的回合制游戏：大话西游  梦话西游，问道，卡牌类
1、封装技能类
	属性：
		技能名
		技能伤害值
2、封装我方英雄类
	属性：
	    名字
		生命值
		攻击力
		技能列表 [技能1，技能2，技能3]
	行为：
		普通攻击(hero2)
		暴击(hero2)
		技能攻击(hero2)
		思路：对方损失生命值，损失多少取决于自身的攻击力，如果是技能攻击，则取决于
			技能伤害值
3、封装敌方英雄类
	属性：
	    名字
		生命值
		攻击力
		技能列表[技能1，技能2，技能3]
	行为：
		普通攻击(hero1)
		技能攻击(hero1)
		思路：对方损失生命值，损失多少取决于自身的攻击力，如果是技能攻击，则取决于
			技能伤害值
4、完成回合制的游戏设计
	while True:
		A->B
		if b 凉了：
			游戏结束，A赢了

		B->A
		if a 凉了：
			游戏结束，B赢了
"""

import random
import time


# 封装技能类
class Skill:
    def __init__(self, sk_name, sk_damage):
        self.skill_name = sk_name
        self.skill_damage = sk_damage


# 封装我方英雄
class OurHero:
    def __init__(self, name, hp, damage, sklist):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.sklist = sklist

    # 我方英雄攻击敌人的方法
    def attack(self, enemyhero):
        num = random.randint(1, 23)
        if 1 <= num <= 5:
            self.__attack_common(enemyhero)
        elif 6 <= num <= 9:
            self.__attack_double(enemyhero)
        elif 9 <= num <= 10:
            self.__attack_skill(enemyhero)

    # 普通攻击
    def __attack_common(self, enemyhero):
        rand_damage = random.randint(1, 10)
        real_damage = self.damage + rand_damage
        # 敌人掉血
        enemyhero.hp -= real_damage
        print(f'{self.name}攻击{enemyhero.name},{enemyhero.name}损失生命值{real_damage},{enemyhero.name}剩余血量{enemyhero.hp}')

    # 暴击
    def __attack_double(self, enemyhero):
        rand_damage = random.randint(1, 10)
        real_damage = (self.damage + rand_damage) * 2
        # 敌人掉血
        enemyhero.hp -= real_damage
        print(f'{self.name}\033[1;31m暴击 \033[0m {enemyhero.name},{enemyhero.name}损失生命值{real_damage},{enemyhero.name}剩余血量{enemyhero.hp}')

    # 技能攻击
    def __attack_skill(self, enemyhero):
        # 随机选择一个技能
        skill = random.choice(self.sklist)
        # 实际伤害为当前的基础伤害+技能伤害值
        real_damage = self.damage + skill.skill_damage
        # 敌方掉血
        enemyhero.hp -= real_damage
        print(
            f'{self.name}释放技能:\033[1;35m{skill.skill_name} \033[0m 攻击{enemyhero.name},{enemyhero.name}损失生命值{real_damage},{enemyhero.name}剩余血量{enemyhero.hp}')

skill_Q = Skill('横扫千军', 100)
skill_W = Skill('瞒天过海', 120)
skill_E = Skill('龙卷雨击', 150)
skill_R = Skill('偷天换日', 300)

skill_ourhero_list = [skill_Q, skill_W, skill_E, skill_R]

skill_q = Skill('神龙摆尾', 100)
skill_w = Skill('狂风暴雨', 120)
skill_e = Skill('夺命气息', 150)
skill_r = Skill('风雷迅驰', 280)
skill_enemyhero_list = [skill_q, skill_w, skill_e, skill_r]









# 封装敌方英雄
class EnemyHero:
    def __init__(self, name, hp, damage, sklist):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.sklist = sklist
    #攻击敌方的方法
    def attack(self,ourhero):
        num = random.randint(1, 10)
        if 1 <= num <= 7:
            self.__attack_common(ourhero)
        else:
            self.__attack_skill(ourhero)
        # 普通攻击

    def __attack_common(self, ourhero):
        rand_damage = random.randint(5, 20)
        real_damage = self.damage + rand_damage
        # 敌方掉血
        ourhero.hp -= real_damage
        print(f'{self.name}攻击{ourhero.name},{ourhero.name}损失生命值{real_damage},剩余血量{ourhero.hp}')

        # 技能攻击

    def __attack_skill(self, hero_light):
        # 随机选一个技能
        skill = random.choice(self.sklist)
        # 实际伤害为当前的基础伤害+技能伤害值
        real_damage = self.damage + skill.skill_damage
        # 敌方掉血
        hero_light.hp -= real_damage
        print(
            f'{self.name}释放技能:{skill.skill_name} 攻击{hero_light.name},{hero_light.name}损失生命值{real_damage},剩余血量{hero_light.hp}')

#创建我方英雄
our_hero=OurHero('帅气的毛毛',1000,100,skill_ourhero_list)
# 创建敌方英雄
enemy_hreo=EnemyHero('大胸长腿貌美肤白的妹妹',1200,70,skill_enemyhero_list)
count=1
while True:
    print(f'第{count}回合')
    our_hero.attack(enemy_hreo)
    if enemy_hreo.hp<0:
        print(our_hero.name+'获胜')
        break
    enemy_hreo.attack(our_hero)
    if our_hero.hp<0:
        print(enemy_hreo.name+'获胜')
        break
    count+=1
    time.sleep(1)

