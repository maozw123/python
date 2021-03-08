import tensorflow as tf

# 创建一个变量--变量op
# 可以使用随机张量来初始化这个变量
# var1 = tf.Variable(
#     initial_value=tf.random_normal(
#         shape=[2, 2],
#         mean=0.0,
#         stddev=1.0
#     ),
#     trainable=True,  # 可用于指定被训练
#     name="var1"
# )
#
# var2 = tf.Variable(
#     initial_value=tf.random_normal(
#         shape=[2, 3],
#         mean=0.0,
#         stddev=1.0
#     ),
#     trainable=True,  # 可用于指定被训练
#     name="var2"
# )
# 变量用途---用于多次修改的值的地方----用于训练参数
# print("var1:\n", var1)
# print("var2:\n", var2)
#
# # 变量op需要经过显式的初始化
# init_op = tf.global_variables_initializer()
# # 开启会话 执行变量
# with tf.Session() as ss:
#     ss.run(init_op)
#     print(ss.run([var1, var2]))

# 思考？?
# python里面想要共享同一个变量----global
# 如何实现tensorflow里面的变量共享？？？
# 命名空间
# 命名空间的名称
# with tf.variable_scope("myscope"):
#     var1 = tf.Variable(
#         initial_value=tf.random_normal(
#             shape=[2, 2],
#             mean=0.0,
#             stddev=1.0
#         ),
#         trainable=True,  # 可用于指定被训练
#         name="var1"
#     )
#
#     var2 = tf.Variable(
#         initial_value=tf.random_normal(
#             shape=[2, 2],
#             mean=0.0,
#             stddev=1.0
#         ),
#         trainable=True,  # 可用于指定被训练
#         name="var1"
#     )
# print("var1:\n", var1)
# print("var2:\n", var2)

# (1)开启命名空间，指定命名空间里面的 reuse=tf.AUTO_REUSE
# (2)创建变量op的指定使用tf.get_variable
# (3)tf.get_variable里面的参数initializer必须以关键字形式传递
# (4)将指定空间的名称置为一样的
with tf.variable_scope("myscope", reuse=tf.AUTO_REUSE):
    var1 = tf.get_variable(
        initializer=tf.random_normal(
            shape=[2, 2],
            mean=0.0,
            stddev=1.0
        ),
        name="var"
    )
    var2 = tf.get_variable(
        initializer=tf.random_normal(
            shape=[2, 2],
            mean=0.0,
            stddev=1.0
        ),
        name="var"
    )

print("var1:", var1)
print("var2:", var2)
#
# 开启会话执行图
with tf.Session() as ss:
    # 变量op还是需要显式的初始化
    ss.run(tf.global_variables_initializer())

    #
    print(ss.run(var1))
    print(ss.run(var2))
