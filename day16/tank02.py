import pygame
import sys
import random
import time
SCRREN_WIDHT = 1200
SCRREN_HEIGHT = 650
# COLOR_GREEN = pygame.color.Color('green')
COLOR_GREEN = pygame.color.Color('#00FA9A')


# COLOR_GREEN = pygame.color.Color(0,255,0)

# 坦克类
class BsaeTank:
    def __init__(self, x, y):
        self.images = {
            'U': pygame.image.load('E:\python\study\python基础\\tank_img\p1tankU.gif'),
            'D': pygame.image.load('E:\python\study\python基础\\tank_img\p1tankD.gif'),
            'L': pygame.image.load('E:\python\study\python基础\\tank_img\p1tankL.gif'),
            'R': pygame.image.load('E:\python\study\python基础\\tank_img\p1tankR.gif'),
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        # 获取图片占据的矩形区域
        self.rect = self.image.get_rect()
        # 根据传入的参数，决定坦克的位置
        self.rect.x = x
        self.rect.y = y
        # 移动速度
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

    def shot(self):
        pass

    # 将坦克加到窗口中
    def display_tank(self):
        self.image = self.images[self.direction]
        # 在窗口指定的位置绘制对应的图片
        MainGame.window.blit(self.image, self.rect)


# 我方坦克
class HeroTank(BsaeTank):
    def __init__(self, x, y):
        super(HeroTank, self).__init__(x, y)
        self.speed = 2

    def move(self):
        # 获取所有按键状态
        keys_status = pygame.key.get_pressed()
        if keys_status[pygame.K_UP]:
            # 第一个改方向
            self.direction = 'U'
            # 调用父类已经实现的移动方法
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
class EnemyTank(BsaeTank):
    def __init__(self, x, y):
        super(EnemyTank, self).__init__(x, y)
        self.images = {
            'U': pygame.image.load('E:\python\study\python基础\\tank_img\enemy1U.gif'),
            'D': pygame.image.load('E:\python\study\python基础\\tank_img\enemy1D.gif'),
            'L': pygame.image.load('E:\python\study\python基础\\tank_img\enemy1L.gif'),
            'R': pygame.image.load('E:\python\study\python基础\\tank_img\enemy1R.gif'),
        }
        # 出生时面对的方向(随机）
        self.direction = self.random_direction()
        self.image = self.images[self.direction]
        # 随机速度
        self.speed = random.randint(1, 2)
        #记录步数（在每个方向走的步数）
        self.step=50

    def random_direction(self):
        directions = ['U', 'D', 'L', 'R']
        return random.choice(directions)
    #重写父类中move方法
    def move(self):
        if self.step>0:
            super(EnemyTank,self).move()
            self.step-=1
        else:
            #重新生成方向
            self.direction=self.random_direction()
            self.step=random.randint(50,100)


# 子弹类
class Bullet:
    def __init__(self,tank):
        #图片
        self.image=pygame.image.load('E:\python\study\python基础\\tank_img\\tankmissile.gif')
        #是否活着
        self.live=True
        #移动速度
        self.speed=6
        #方向
        self.direction=tank.direction
        #设置子弹的位置
        self.rect=self.image.get_rect()
        self.rect.centerx=tank.rect.centerx
        self.rect.centery=tank.rect.centery
    #子弹的移动
    def move(self):
        if self.direction=='U':
            if self.rect.centery>self.rect.height//2:
                self.rect.centery-=self.speed
            else:
                self.live=False
        elif self.direction=='D':
            if self.rect.centery<SCRREN_HEIGHT-self.rect.height//2:
                self.rect.centery-=self.speed
        elif self.direction=='L':
            if self.rect.centerx>self.rect.width//2:
                self.rect.centerx-=self.speed
            else:
                self.live=False
        elif self.direction=='R':
            if self.rect.centerx<SCRREN_WIDHT-self.rect.width//2:
                self.rect.centerx+=self.speed
            else:
                self.live=False



# 爆炸类
class Bomb:
    pass


# 墙壁类
class Wall:
    pass


# 主业务类
class MainGame:
    window = None
    P1 = None
    # 存储敌人坦克的列表
    enemy_tank_list = []

    def creat_window(self):
        pygame.display.init()
        # 创建窗口
        MainGame.window = pygame.display.set_mode((SCRREN_WIDHT, SCRREN_HEIGHT))

    # 创建我方坦克
    def creat_hero_tank(self):
        if not MainGame.P1:
            MainGame.P1 = HeroTank(500, 400)

    # 加载我方坦克
    def load_hero_tank(self):
        if MainGame.P1 and MainGame.P1.live:
            MainGame.P1.display_tank()

    # 创建敌方坦克
    def creat_enemy_tank(self):
        for i in range(10):
            e_tank = EnemyTank(random.randint(1, 10) * 100, 100)
            MainGame.enemy_tank_list.append(e_tank)

    # 加载敌方坦克
    def load_enemy_tank(self):
        for e_tank in MainGame.enemy_tank_list:
            if e_tank.live:
                e_tank.display_tank()
                e_tank.move()
            else:
                MainGame.enemy_tank_list.remove(e_tank)

    # 事件处理
    def deal_events(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                print('退出')
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print('按下键盘')

    def start_game(self):
        # 调用创建窗口的功能
        self.creat_window()
        # 调用创建坦克方法
        self.creat_hero_tank()
        # 调用创建敌方坦克
        self.creat_enemy_tank()
        # 别让程序结束
        while True:
            # 给窗口持续填充颜色
            MainGame.window.fill(COLOR_GREEN)
            # 调用加载坦克方法
            self.load_hero_tank()
            # 调用移动方法
            MainGame.P1.move()
            # 调用加载敌方坦克方法
            self.load_enemy_tank()
            # 调用事件处理方法
            self.deal_events()
            # 让屏幕持续刷新
            pygame.display.update()

    def game_over(self):
        pass


MainGame().start_game()
