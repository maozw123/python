import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

# mysql+pymysql://用户名:密码@主机地址/库名
db = sqlalchemy.create_engine('mysql+pymysql://root:0321@localhost/mao')

# 创建一个继承基类
base = declarative_base(db)


# 映射
# 将表名 映射为类名
# 将字段映射为  属性
class User(base):
    __tablename__ = 'stu'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(32))


if __name__ == '__main__':
    # 根据写好的model模型  创建表
    base.metadata.create_all(db)

# 对数据库的增删改查
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=db)
session = session()

# 插入单条数据
# user = User(
#     id=1,
#     name='python'
# )
# session.add(user)
# session.commit()

# 插入多条数据

# session.add_all(
#     [
#         User(id=2, name='java'),
#         User(id=4, name='php')
#     ]
# )
# session.commit()


# 查询
# all 返回多条数据  返回值是一个列表
# data = session.query(User).all()
# print(data)
# print(data[0])
# print(data[0].name)
# for x in data:
#     print(x)
#     print(x.id, x.name)


# data=session.query(User).filter(User.name == 'java').all()
# print(data)
#  first 返回值是一个 对象，是满足条件的第一条数据

# data=session.query(User).filter(User.name=='XXXX').first()
# print(data)
# filter 和filter by 的区别
# data = session.query(User).filter_by(name='java').all()
# print(data)
#
# get 方法使用id进行查询，返回值是一个对象
# get 方法查询的条件必须是主键
# data = session.query(User).get(ident=4)
# print(data.name)

# 修改数据
# 首先要查询到数据是否存在然后再进行修改
# data = session.query(User).get(4)
# print (data)
# data.name='lvmao'
# session.merge(data)
# session.commit()

# data = session.query(User).filter(User.name== 'java').all()
# for x in data:
#     x.name = 'maomao'
#     session.merge(x)
#
# session.commit()

# data = session.query(User).all()
# for x in data:
#     print (x.name)

# session.query(User).filter(User.id == 6).update({User.name:"xxxxx",User.id:11})
# session.commit()


# 删除操作  delete

# data=session.query(User).filter(User.id==11).first()
# session.delete(data)
# session.commit()

# data=session.query(User).all()
# for x in data:
#     if x.id==2:
#         session.delete(x)
# session.commit()

session.query(User).filter(User.id==3).delete()
session.commit()

