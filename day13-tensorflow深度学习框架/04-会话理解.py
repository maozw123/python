# 会话---执行op的类
# 本质：连接前台程序与底层C++代码的纽带
# 两种形式
# tf.Session() ：用于完整的程序中
# tf.InteractiveSession() ：应用于交互环境

# 会话使用--完整流程
# 1、会话初始化
# __init__
# 2、会话执行
# ss.run()
# 3、关闭会话
# ss.close()

# 不使用上面的方式，使用with托管
import tensorflow as tf

con_a = tf.constant(3, name="con_a")
con_b = tf.constant(3, name="con_b")

con_sum = tf.add(con_a, con_b, name="add")

print("con_a:", con_a)
print("con_b:", con_b)
print("con_sum:", con_sum)

# 构建一个占位op
plt = tf.placeholder(shape=[2, 2], dtype=tf.int32)
hh = tf.placeholder(shape=[2, 2], dtype=tf.int32)

# c = 1.0
# a = "hello world"

# 开启会话 执行图
# 会话初始化的时候
# 参数 target : 可以指定云端的设备进行执行会话
# 参数 graph ：可以指定想要执行的图
# 参数 config： 可以打印设备信息
with tf.Session() as ss:
    # fetches 参数
    # print("运行结果：\n", ss.run(con_sum))
    # print("运行结果：\n", ss.run([con_a,con_b,con_sum]))
    # print("运行结果：\n", ss.run((con_a,con_b,con_sum)))
    # run 必须是一个op 或者是一个op列表、或者op元组
    # feed_dict  跟占位op一块使用对 占位op进行填值
    print(ss.run([plt, hh], feed_dict={plt: [[1, 2], [3, 4]], hh: [[1, 2], [3, 4]]}))
    # print("运行结果：\n", ss.run(c)) # 错误的
    # ss.run(a) # 错误的

# 如果安装GPU 的同学-设置使用GPU
# tf.DeviceSpec(device_type="GPU", device_index=0)

# with tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)) as ss:
#     print("运行结果：\n", ss.run(con_sum))
