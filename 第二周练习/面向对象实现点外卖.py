"""
2.基于面向对象思想分析实现：
小明通过xxApp叫了一份xx商家的外卖，外卖小哥很快将外卖送到了小明手里，并求小明给五星好评

2.1. 分析(封装类)
    顾客：
        属性：
            名字
            地址
            电话
        行为：
            点外卖(App)

    App：
        属性：
            名字
            商家列表
        行为：
            下单(商家)
            派单(外卖小哥)
    商家：
        属性：
            名字
            菜单列表
        行为：
            接单(顾客)

    外卖小哥：
        属性：
            名字
            电话
        行为：
            接餐(商家，客户)
            送餐(客户)
            求好评(顾客)
2.2  处理类与类之间的交互关系

"""
class Customer:
    def __init__(self,name,phone,home):
        self.name=name
        self.phone=phone
        self.home=home
    def orders(self,app):
        print(f'{self.name}打开{app.appname}')
        app.orders_merchant()
class App:
    def __init__(self,appname):
        self.appname=appname
        self.merchant_list=['北京饭店','全聚德','老北京火锅']
    #下单给商家
    def orders_merchant(self):
        print(f'商家列表:{self.merchant_list}')
        merchant_name1=input('请选择你要下单的商家名')
        # 根据选择的商家索引值，创建对应的商家对象
        merchant=Merchant(merchant_name1)
        print(f'你选择的商家为{merchant.merchant_name}')
        print(f'商家菜单如下：{merchant.caidan}')
        choice=eval(input('请输入选择的菜品'))
        print(f'你选择的菜品为：{merchant.caidan[choice]}')
        print('下单成功')
        # 调用商家里的接单方法
        merchant.order_receiving()
    def send_meal(self,xiaoge)
        print(f'派单成功，小哥信息为：{xiaoge.name}')

class Merchant:
    def __init__(self,merchant_name):
        self.merchant_name=merchant_name
        self.caidan=['烤鸭','自助','海鲜']
    def order_receiving(self):
        print('商家已接单')
class SendMeal:
    def __init__(self,name):
        self.name=name
    def take_meal(self):
        # 接餐操作，需要知道商家跟顾客
        pass
    def send_meal(self,customer):
        # 为顾客送餐
        print(f'外卖小哥正在前往{customer.phone},为：{customer.name}送餐')
    def good_reputation(self,customer):
        # 求顾客给好评
        print(f'外卖小哥{self.name}请求{customer.name}给一好评')
customer=Customer('毛十八',13619566823,'北京市XXX')
app=App('美团外卖')
customer.orders(app)
xiaoge=SendMeal('王忠明')
app.orders_merchant()
xiaoge.take_meal()
xiaoge.good_reputation(customer)