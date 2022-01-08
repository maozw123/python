import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

## 链接数据库
#   mysql+ pymysql://用户名：密码@主机地址/库名
db = sqlalchemy.create_engine("mysql+pymysql://root:11111111@localhost/demo")

# 创建一个继承基类
base = declarative_base(db)


### 映射
# 将 表名 映射为类名
# 将字段映射为  属性
#
class User(base):
    __tablename__ = 'student'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(32))


# if __name__ == '__main__':
#     #  根据写好的model模型  创建表
#     base.metadata.create_all(db)

# 操作数据库
# 对数据库的 增删改查
from sqlalchemy.orm import sessionmaker
# 绑定一个查询实例   pymysql 游标
session = sessionmaker(bind=db)
session = session()

## 插入 单条数据
# user =User(
#     id = 4,
#     name='python'
# )
# #
# session.add(user)
# session.commit()

# 插入多条数据
# session.add_all(
#     [
#         User(id=5,name='java'),
#         User(id=6,name='php')
#     ]
# )
# session.commit(),

#  查询
# all  返回多条数据  返回值是一个 列表
# data = session.query(User).all()
# print (data)
# print (data[0])
# print (data[0].name)
# for x in data:
#     print (x)
#     print (x.name)
#
# data = session.query(User).filter(User.name== 'laowang').all()
# print (data)
# #  first 返回值是一个 对象，是满足条件的第一条数据
# data = session.query(User).filter(User.name == 'xxxx').first()
# print (data)
# # filter 和filter by 的区别
# data = session.query(User).filter_by(name='laowang').all()
# print(data)
#
# # get 方法使用id 进行查询， 返回值是一个 对象
# data = session.query(User).get(ident = 10)
# print (data.name)
#

# 修改数据
# 查询到数据
# data = session.query(User).get(10)
# print (data)
# data.name = 'laoli'
# session.merge(data)
# session.commit()

# data = session.query(User).get(10)
# print (data.name)

# data = session.query(User).filter(User.name== 'laowang').all()
# for x in data:
#     x.name = 'laoli2'
#     session.merge(x)
#
# session.commit()
#
#
# data = session.query(User).all()
# for x in data:
#     print (x.name)


# session.query(User).filter(User.id == 10).update({User.name:"xxxxx",User.id:11})
# session.commit()


# 删除操作   delete
# data = session.query(User).filter(User.id == 11).first()
# session.delete(data)
# session.commit()
#
# data = session.query(User).get(6)
# session.delete(data)
# session.commit()


# data = session.query(User).all()
# for x in data:
#     if x.id == 2:
#         session.delete(x)
#
# session.commit()


session.query(User).filter(User.id == 3).delete()
session.commit()
