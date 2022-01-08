import pymysql

# 创建连接

db = pymysql.connect(host='127.0.0.1',#主机
                     port=3306,#端口
                     user='root',#用户
                     passwd='0321',#密码
                     db='student'#选入student库
                     )
# 拿到游标
cursor = db.cursor()
# test表插入
sql = "insert into test(id,name) value(10,'nihao');"
# 执行sql
cursor.execute(sql)
db.commit()
# 关闭链接
db.close()
