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
commodity=session.query(Commodity).all()
person=session.query(Person).all()
print('用户：詹姆斯，杜篮子，卡哇伊，安东尼')
y=input('请输入用户：')
print('商品为：鞋，篮球，足球')
x=input('请输入您要买的商品')
for person_name in person:
    if y==person_name.name:
        for i in commodity:
            # print(i.name)
            if x==i.name:
                # print(i.name,i.price,i.num)
                a=int(input('请输入要购买的个数'))
                if person_name.money>=i.price and a>0:
                    print('可以购买')
                    person_name.money-=i.price*a
                    i.num-=a
                    b=(f'{person_name.name}买了{i.name}后还剩钱{person_name.money}，{i.name}的库存还有{i.num}个')
                    print(b)
                    log=Log(
                        # msg=f'{person_name.name}买了{i.name}后还剩钱{person_name.money}，{i.name}库存还有{i.num}个'
                        msg=f'{b}'
                    )
                    session.add(log)
                    if i.num<0:
                        session.rollback()
                        print('存货不足，请减少您要购买的数量')
                        break
                    else:
                        session.commit()
                        print('购买成功，欢迎下次光临')
                        break