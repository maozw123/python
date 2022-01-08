import pymysql

## 创建链接
db = pymysql.connect(host='127.0.0.1',port=3306,
                     user='root',passwd='11111111',
                     db='demo')
# (主机，端口，用户名，密码，操作的库）
## 拿到游标
cursor = db.cursor()
sql = "insert into test(id,name,age) values(3,'hello',19);"
## 执行sql
cursor.execute(sql)
db.commit()
## 关闭链接
db.close()










