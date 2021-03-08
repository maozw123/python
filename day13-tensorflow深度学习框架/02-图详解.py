import tensorflow as tf

# 构建图
# 图结构---包含至少一组op与tensor的结构
con_a = tf.constant(3)
con_b = tf.constant(4)

con_sum = tf.add(con_a, con_b)

print("con_sum:\n", con_sum)
print("con_a:\n", con_a)
print("con_b:\n", con_b)

# 也可以获取op所在的图
print("a所在的图：", con_a.graph)
print("b所在的图:", con_b.graph)
print("sum所在的图:", con_sum.graph)

# 创建一个图
# g = tf.Graph()
#
# # 使用g图
# with g.as_default():
#     g_a = tf.constant(5.0)
#
#     print("g_a所在的图：", g_a.graph)

# 执行图--执行默认的图
with tf.Session() as ss:
    # # 默认只有一张图
    # 获取会话所执行的默认的图
    # print("tensorflow默认的图：", tf.get_default_graph())
    # print("会话执行的图：", ss.graph)
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
    # print(ss.run(g_a)) # 错误的 # g_a不是默认图中的op

# 执行g图
# with tf.Session(graph=g) as ss:
#     # # 默认只有一张图
#     # 获取会话所执行的默认的图
#     print("tensorflow默认的图：", tf.get_default_graph())
#     print("会话执行的图：", ss.graph)
#     # print(ss.run(con_sum)) # 错误的，con_sum 不在g图中
#     print(ss.run(g_a))


# 只在默认的图中进行操作
