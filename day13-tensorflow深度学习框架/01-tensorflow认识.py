# tensorflow 是一个开源的数值型计算库
# 采用数据流图结构
# 数据流图里面 点---节点（op）---数学计算单元
# 数据流图里面 线---张量(tensor)---用来联系计算的多维数组

# 优点：
# 1、高度灵活---采用数据流图
# 2、语言多样---C++底层，Python封装
# 3、设备支持---CPU  GPU  TPU
# 4、可视化---将程序可以以数据流图的形式来展示

# Python中的加法
# a = 3
# b = 4
# c = a + b
# print("c:\n", c)

# 导包
import tensorflow as tf


import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# 先定义一个变量
con_a = tf.constant(3)
con_b = tf.constant(4)

# 变量相加
con_sum = tf.add(con_a, con_b)

# 返回一个tensor  ，tensor里面包含着op
print("con_a:\n", con_a)
print("con_b:\n", con_b)
print("相加结果为：\n", con_sum)

# 开启会话---执行图
with tf.Session()  as ss:
    print(ss.run(con_a))
    print(ss.run(con_b))
    print(ss.run(con_sum))

# 数据流图
# （1）构建图阶段
# （2）执行图

