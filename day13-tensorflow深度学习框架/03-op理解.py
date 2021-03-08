import tensorflow as tf

# op ---指令
# op指令
# 返回tensor 里面包含的op名称为op指令空间内的名称
# 名称不允许重复，如果重复，+_i来加以区别
# 可以通过构建op的时候，来指定name参数来修改op在指令空间内的名称

# 构建图
# 图结构---包含至少一组op与tensor的结构
con_a = tf.constant(3, name="con_a")
con_b = tf.constant(4, name="con_b")

con_sum = tf.add(con_a, con_b, name="con_sum")

print("con_sum:\n", con_sum)
print("con_a:\n", con_a)
print("con_b:\n", con_b)

# 也可以获取op所在的图
print("a所在的图：", con_a.graph)
print("b所在的图:", con_b.graph)
print("sum所在的图:", con_sum.graph)

# 执行图--执行默认的图
with tf.Session() as ss:
    # 开启可视化 ---
    # （1）序列化events文件
    # 参数1 events文件的路径
    # 参数2 需要保存的内容--保存会话执行的图
    # 返回FileWriter对象
    # events 文件---本质：关于本机名称、时间戳的文件
    tf.summary.FileWriter("./tmp/", graph=ss.graph)
    # （2）开启tensorboard后台服务器
    # tensorboard --logdir="./tmp/" --host=127.0.0.1
    # （3）在浏览器验证
    # http://127.0.0.1:6006
    print(ss.run(con_sum))
