"""
v1.1.5
    实现墙壁类

"""
import pygame
import sys
import random
import time
SCRREN_WIDHT = 1200
SCRREN_HEIGHT = 650
# COLOR_GREEN = pygame.color.Color('green')
COLOR_GREEN = pygame.color.Color('#00FA9A')
# COLOR_GREEN = pygame.color.Color(0,255,0)
# load = pygame.image.load
# 坦克父类
class BaseTank:
    def __init__(self,x,y):
        self.images = {
            'U': pygame.image.load('E:\python\study\python基础\\tank_img\p1tankU.gif'),
            'D': pygame.image.load('E:\python\study\python基础\\tank_img\p1tankD.gif'),
            'L': pygame.image.load('E:\python\study\python基础\\tank_img\p1tankL.gif'),
            'R': pygame.image.load('E:\python\study\python基础\\tank_img\p1tankR.gif'),
        }
        self.direction = 'U'#D,L,R
        self.image = self.images[self.direction]
        # 获取图片占据的矩形区域
        self.rect = self.image.get_rect()
        # 根据传入的参数，决定坦克的位置
        self.rect.x = x
        self.rect.y = y
        #移动速度
        self.speed = 3
        # 是否活着
        self.live = True
    # 改坐标
    def move(self):
        if self.direction == 'U':
            if self.rect.y > 0:
                self.rect.y -= self.speed
        elif self.direction == 'D':
            if self.rect.y < SCRREN_HEIGHT - self.rect.height:
                self.rect.y += self.speed
        elif self.direction == 'L':
            if self.rect.x > 0:
                self.rect.x -= self.speed
        elif self.direction == 'R':
            if self.rect.x < SCRREN_WIDHT - self.rect.height:
                self.rect.x += self.speed
    # v1.1.1 实现发射方法
    def shot(self):
        return Bullet(self)
    # 将坦克加到窗口中
    def display_tank(self):
        self.image = self.images[self.direction]
        #在窗口指定的位置绘制对应的图片
        MainGame.window.blit(self.image,self.rect)
# 我方坦克
class HeroTank(BaseTank):
    def __init__(self,x,y):
        super(HeroTank, self).__init__(x,y)
        self.speed = 4
    def move(self):
        # 获取所有案件的状态
        keys_status = pygame.key.get_pressed()
        if keys_status[pygame.K_UP]:
            # 第一个改方向
            self.direction = 'U'
            #调用父类已经实现的移动方法
            super().move()
        elif keys_status[pygame.K_DOWN]:
            self.direction = 'D'
            super(HeroTank, self).move()
        elif keys_status[pygame.K_LEFT]:
            self.direction = 'L'
            super(HeroTank, self).move()
        elif keys_status[pygame.K_RIGHT]:
            self.direction = 'R'
            super(HeroTank, self).move()

# 敌方坦克
class EnemyTank(BaseTank):
    def __init__(self,x,y):
        super(EnemyTank, self).__init__(x,y)
        self.images = {
            'U': pygame.image.load('E:\python\study\python基础\\tank_img\enemy1U.gif'),
            'D': pygame.image.load('E:\python\study\python基础\\tank_img\enemy1D.gif'),
            'L': pygame.image.load('E:\python\study\python基础\\tank_img\enemy1L.gif'),
            'R': pygame.image.load('E:\python\study\python基础\\tank_img\enemy1R.gif'),
        }
        # 随机方向
        self.direction = self.random_direction()
        self.image = self.images[self.direction]
        # 随机速度
        self.speed = random.randint(2,4)
        # v1.0.8 记录步数(在每个方向走的步数)
        self.step = 50

        # v1.1.1 发射子弹的计算器
        self.count = 1

    def random_direction(self):
        directions = ['U','D','L','R']
        return random.choice(directions)
    #v1.1.1
    def shot(self):
        self.count += 1
        if self.count == 50:
            b = super(EnemyTank, self).shot()
            MainGame.bullet_enemy_list.append(b)
            self.count = 1

    #v1.0.8 重写父类中move方法
    def move(self):
        if self.step > 0:
            super(EnemyTank, self).move()
            self.step -= 1
        else:
            # 重新生成方向
            self.direction = self.random_direction()
            self.step = (5-self.speed)*random.randint(40,60)

# 子弹类
class Bullet:
    def __init__(self,tank):
        # 图片
        if isinstance(tank,HeroTank):
            self.image = pygame.image.load('E:\python\study\python基础\\tank_img/tankmissile.gif')
        else:
            self.image = pygame.image.load('E:\python\study\python基础\\tank_img/enemymissile.gif')
        # 是否活着
        self.live = True
        # 移动速度
        self.speed = 10
        # 方向
        self.direction = tank.direction
        # 设置子弹的位置
        self.rect = self.image.get_rect()
        #v1.1.0 优化子弹初始化的位置
        if self.direction == 'U':
            self.rect.centerx = tank.rect.centerx
            self.rect.centery = tank.rect.centery - tank.rect.height // 2 - self.rect.height//2
        elif self.direction == 'D':
            self.rect.centerx = tank.rect.centerx
            self.rect.centery = tank.rect.centery + tank.rect.height // 2 + self.rect.height // 2
        elif self.direction == 'L':
            self.rect.centery = tank.rect.centery
            self.rect.centerx = tank.rect.centerx - tank.rect.height // 2 - self.rect.height // 2
        elif self.direction == 'R':
            self.rect.centery = tank.rect.centery
            self.rect.centerx = tank.rect.centerx + tank.rect.height // 2 + self.rect.height // 2
    # 子弹的移动
    def move(self):
        if self.direction == 'U':
            if self.rect.centery > self.rect.height // 2:
                self.rect.centery -= self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            if self.rect.centery < SCRREN_HEIGHT - self.rect.height//2:
                self.rect.centery += self.speed
            else: self.live  = False
        elif self.direction == 'L':
            if self.rect.centerx > self.rect.width // 2:
                self.rect.centerx -= self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.centerx < SCRREN_WIDHT - self.rect.width // 2:
                self.rect.centerx += self.speed
            else:
                self.live = False
    # v1.1.2 是否打中敌方坦克
    def hit_enemy_tank(self):
        for e_tank in MainGame.enemy_tank_list:
            if pygame.sprite.collide_rect(self,e_tank):
                self.live = False
                e_tank.live = False
                # v1.1.4 创建爆炸对象，存储到爆炸列表中
                bomb = Bomb(e_tank)
                MainGame.bomb_list.append(bomb)

    # v1.1.3 是否打中我方坦克
    def hit_hero_tank(self):
        if pygame.sprite.collide_rect(self,MainGame.P1):
            self.live = False
            MainGame.P1.live = False
            #v1.1.4 被敌方打中产生爆炸效果
            bomb = Bomb(MainGame.P1)
            MainGame.bomb_list.append(bomb)
    def display_bullet(self):
        MainGame.window.blit(self.image,self.rect)

#爆炸类
# v1.1.4 完善爆炸效果类
class Bomb:
    def __init__(self,tank):
        self.images = [
            pygame.image.load('E:\python\study\python基础/tank_img/blast0.gif'),
            pygame.image.load('E:\python\study\python基础/tank_img/blast1.gif'),
            pygame.image.load('E:\python\study\python基础/tank_img/blast2.gif'),
            pygame.image.load('E:\python\study\python基础/tank_img/blast3.gif'),
            pygame.image.load('E:\python\study\python基础/tank_img/blast4.gif'),
            pygame.image.load('E:\python\study\python基础/tank_img/blast5.gif'),
        ]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = tank.rect
        self.live = True
    def display_bomb(self):
        if self.image_index < len(self.images):
            self.image = self.images[self.image_index]
            MainGame.window.blit(self.image,self.rect)
            self.image_index += 1
        else:
            self.live = False
            self.image_index = 0


#墙壁类
#v1.1.5 实现墙壁类
class Wall:
    def __init__(self,x,y):
        self.image=pygame.image.load('E:\python\study\python基础\\tank_img\walls.gif')
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.hp=5
    def display_wall(self):
        MainGame.window.blit(self.image,self.rect)
#主业务类
class MainGame:
    window = None
    P1 = None
    # v1.0.7 存储敌方坦克的列表
    enemy_tank_list = []
    # v1.1.0 存储所有我方子弹的列表
    bullet_hero_list = []
    # v1.1.1 存储敌方子弹列表
    bullet_enemy_list = []
    # v1.1.4 存储所有爆炸效果的列表
    bomb_list = []
    #v1.1.5  存储所有的墙壁
    wall_list=[]
    def creat_window(self):
        pygame.display.init()
        # 创建窗口
        MainGame.window = pygame.display.set_mode((SCRREN_WIDHT,SCRREN_HEIGHT))
    #v1.1.5  创建墙壁类
    def creat_wall(self):
        wall=Wall(300,300)
        MainGame.wall_list.append(wall)
    #v1.1.5  加载墙壁类
    def load_wall(self):
        for wall in MainGame.wall_list:
            if wall.hp>0:
                wall.display_wall()
            else:
                MainGame.wall_list.remove(wall)

    # 创建我方坦克
    def creat_hero_tank(self):
        if not MainGame.P1:
            MainGame.P1 = HeroTank(500,400)
    #加载我方坦克
    def load_hero_tank(self):
        if MainGame.P1 and MainGame.P1.live:
            MainGame.P1.display_tank()
            # v1.1.3 优化调用移动方法的位置
            MainGame.P1.move()
        # v1.1.3 从内存中删除我方坦克
        else:
            del MainGame.P1
            # 增加类属性，属性值为None
            MainGame.P1 = None
    #v1.0.7 创建敌方坦克
    def creat_enemy_tank(self):
        for i in range(5):
            e_tank = EnemyTank(random.randint(1,10)*100,100)
            MainGame.enemy_tank_list.append(e_tank)
    #v1.0.7 加载敌方坦克
    def load_enemy_tank(self):
        for e_tank in MainGame.enemy_tank_list:
            if e_tank.live:
                e_tank.display_tank()
                e_tank.move()
                #v1.1.1 调用优化后的射击方法
                e_tank.shot()
            else:
                MainGame.enemy_tank_list.remove(e_tank)
    # v1.1.0 加载所有我方子弹
    def load_bullet_hero(self):
        for b in MainGame.bullet_hero_list:
            if b.live:
                b.display_bullet()
                b.move()
                # v1.1.2 调用是否打中敌方坦克的方法
                b.hit_enemy_tank()
            else:
                MainGame.bullet_hero_list.remove(b)
    # v1.1.1 记载所有敌方子弹
    def load_bullet_enemy(self):
        for b in MainGame.bullet_enemy_list:
            if b.live:
                b.display_bullet()
                b.move()
                # v1.1.3 调用是否打中我方坦克的方法
                if MainGame.P1 and MainGame.P1.live:
                    b.hit_hero_tank()
            else:
                MainGame.bullet_enemy_list.remove(b)
    # v1.1.4 加载所有爆炸效果
    def load_bomb(self):
        for bomb in MainGame.bomb_list:
            if bomb.live:
                bomb.display_bomb()
            else:
                MainGame.bomb_list.remove(bomb)
    # 事件处理
    def deal_events(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                print('退出')
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if MainGame.P1 and MainGame.P1.live:
                        if len(MainGame.bullet_hero_list)<3:
                             # 创建一个子弹，存储到列表中
                             b = Bullet(MainGame.P1)
                             # 将子弹存储到列表中
                             MainGame.bullet_hero_list.append(b)
                        else:
                            print('最多只能发射3发')
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
    def start_game(self):
        #调用创建窗口的功能
        self.creat_window()
        #v1.1.5调用创建墙壁的方法
        self.creat_wall()
        # 调用创建坦克方法
        self.creat_hero_tank()
        #v1.0.7 调用创建敌方坦克
        self.creat_enemy_tank()
        #别让程序结束
        while True:
            # 给窗口持续填充颜色
            MainGame.window.fill(COLOR_GREEN)
            #v1.1.5 调用加载墙壁的方法
            self.load_wall()
            # 调用加载坦克的方法
            self.load_hero_tank()
            # v1.1.0 调用加载我方子弹的方法
            self.load_bullet_hero()
            #v1.0.7 调用加载敌方坦克的方法
            self.load_enemy_tank()
            # v1.1.1 调用加载敌方子弹方法
            self.load_bullet_enemy()
            # v1.1.4 调用加载爆炸效果的方法
            self.load_bomb()
            # 调用事件处理方法
            self.deal_events()
            # 让屏幕持续刷新
            pygame.display.update()
            #v1.0.8增加休眠操作
            pygame.time.delay(10)
    def game_over(self):
        pass
MainGame().start_game()
