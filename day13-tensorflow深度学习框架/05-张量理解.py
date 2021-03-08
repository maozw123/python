import tensorflow as tf

# 张量 -----数据流图中的线-----数据传递----本质：多维数组

# 两个属性
# dtype---数据类型
# 将numpy里面的np.数据类型----变成了tf.数据类型
# 可以在创建张量的时候去指定dtype 参数来指定tensor的数据类型
#

# shape ---形状

# # 创建张量----创建固定值张量
# con_a = tf.constant(3, dtype=tf.float64, name="con_a")
# con_a = tf.to_int32(con_a)  # 数据类型可以强制转换
#
#
# # res = tf.to_int32(True)
# # res = tf.to_int32(False)
# # print("res:\n",res)
#
# # 数据类型转换 cast
# # 参数1  将要转化的tensor
# # 参数2  新的数据类型
# con_a = tf.cast(con_a,dtype=tf.float64)
# con_a = tf.cast(con_a,dtype=tf.int64)
# print("con_a:\n", con_a)
#
#
#
#
# # 创建一个全为0 的张量
# zeros = tf.zeros(shape=[2, 3], dtype=tf.int32, name="zeros")
# print("zeros:\n", zeros)
#
# # 创建一个全部为1 的张量
# ones = tf.ones(shape=[2, 2], dtype=tf.int32, name="ones")
# print("ones:\n", ones)
#
# # 创建随机张量---创建一个符合标准正态分布的随机张量
# hh = tf.random_normal(
#     shape=[2, 3],
#     mean=0.0,
#     stddev=1.0,
#     name="hh",
#     dtype=tf.float64
# )
# print("hh:\n", hh)
# 获取 tensor里面包含的值
# 开启会话执行图
# with tf.Session() as ss:
#     print(ss.run(fetches=[con_a, zeros, ones, hh]))
#     # print(ss.run(res))


# 形状的更改
# gg = tf.random_normal(
#     shape=[2, 2],
#     mean=0.0,
#     stddev=1.0,
#     name="gg"
# )
# None 行None列的2阶张量
gg = tf.placeholder(shape=[None, None], dtype=tf.int32, name="gg")
print("gg:\n", gg)
# 确定其形状
# 静态形状改变，只能将未知的形状确定，不能夸阶更改
# gg.set_shape(shape=[2, 2])
# gg.set_shape(shape=[1, 2, 2])
# 也能将未知的形状确定
# 而且可以夸阶更改
# 只要元素确定，想怎么改就怎么改
gg = tf.reshape(gg, shape=[1, 2, 2])
# gg = tf.reshape(gg, shape=[1, 2, 3]) # 错误的
print("gg:\n", gg)

with tf.Session() as ss:
    # print(ss.run(gg, feed_dict={gg: [[1, 2], [3, 4]]}))
    # print(ss.run(gg, feed_dict={gg: [[[1, 2], [3, 4]]]})) # 静态形状更改时错误的不能夸阶更改
    print(ss.run(gg, feed_dict={gg: [[[1, 2], [3, 4]]]})) # reshape能夸阶更改
    # print(ss.run(gg)) # 错误的不能夸阶更改
