"""
商品表    id（int 主键）   name（char）  num（int）  price（int）
​							鞋                           10                  100
用户表   person    id（主键）   name（姓名）   money（int）

​								 张三               10000
日志表   log   id(int)  msg(varchar)

if __name__== '__main__':
​		用户买商品
​        买一件     生成一条日志    用户金额 减去    商品库存  减去
​       事务

1. 拿到用户的资金，拿到商品的价格，比较用户的资金 是否可以买商品，如果可以  减去相对应的值，生成购买成功的日志

2. 直接减用户的资金，判断商品的库存，如果 库存为0 ，这个  时候 做一个  回滚



session.commit

session.rollback
"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

db = sqlalchemy.create_engine('mysql+pymysql://root:0321@localhost/mao')
base = declarative_base(db)


class Commodity(base):
    __tablename__ = 'commodity'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(32))
    num = sqlalchemy.Column(sqlalchemy.Integer)
    price = sqlalchemy.Column(sqlalchemy.Integer)


class Person(base):
    __tablename__ = 'person'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(32))
    money = sqlalchemy.Column(sqlalchemy.Integer)


class Log(base):
    __tablename__ = 'log'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    msg = sqlalchemy.Column(sqlalchemy.String(32))


if __name__ == '__main__':
    base.metadata.create_all(db)

from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=db)
session = session()
# session.add_all(
#     [
#         Commodity(id=1, name='鞋', num=10, price=100),
#         Commodity(id=2, name='篮球', num=5, price=200),
#         Commodity(id=3, name='足球', num=8, price=500),
#     ]
# )
# session.add_all(
#     [
#         Person(id=1,name='詹姆斯',money=10000),
#         Person(id=2,name='杜篮子',money=1000),
#         Person(id=3,name='卡哇伊',money=5000),
#         Person(id=4,name='安东尼',money=8000)
#     ]
# )

# session.commit()

commodity=session.query(Commodity).all()
person=session.query(Person).all()
# for x in data:
a=int(input('请输入要购买的个数'))
if person[0].money>=commodity[0].price and a>0:
    print('可以购买')
    person[0].money-=commodity[0].price*a
    commodity[0].num-=a
    b=(f'{person[0].name}买了{commodity[0].name}后还剩钱{person[0].money}，{commodity[0].name}库存还有{commodity[0].num}个')
    print(b)
    log=Log(
        msg=f'{person[0].name}买了{commodity[0].name}后还剩钱{person[0].money}，{commodity[0].name}库存还有{commodity[0].num}个'
    )
    session.add(log)
    if a>commodity[0].num:
        session.rollback()
        print('存货不足，请减少您要购买的数量')
    else:
        session.commit()
